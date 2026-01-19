# Orbit and attitude propagator for a spacecraft that performs proximity maneuvers
# around a tumbling debris. 

# This code sample shows the propagator developed for the servicer orbiting around the 
# debris by holding a fixed position with respect to the debris body frame.

# Attitude is represented using Modified Rodrigues Parameters (MRP)
# Reference is obtained through relative position and velocity
# in the Hill frame of the debris

# Brief explanation of the parameters included in the propagation:
# K, P: control gains
# u: control action
# mu: gravitational constant of the Earth
# t: actual time
# tvec: vector that contains the time intervals of the whole duration of the mission    
# X: State vector, including the position and velocity of the servicer in the Hill frame of the debris
# X = [x, y, z, x_dot, y_dot, z_dot] in the Hill frame of the debris
# Re: Radius of the Earth
# wH_0: Mean angular velocity of the debris
# r1: Radius of the circular orbit of the debris
# rhoB_ref: Reference position in the body frame of the debris
# DCM_act: DCM from Hill frame to debris body frame

# Main simulation loop: propagate relative orbit and attitude of the debris,
# compute control, integrate relative dynamics of the servicer

# Other proximity maneuvers (drifting inspection or final approach) follow the same 
# propagation and control structure.
# Only the reference generation (rhoB_ref, rhoDotB_ref) differs.
# This sample is shown as the most representative case.

# This design enables reuse of the same propagator and controller across different
# proximity operation phases by modifying only the reference definition.
    
for t in time_vector:
    
    #Time Step
    dt = t - prev_t
    
    #Previous time
    prev_t = t
   
    # Update the control action every second
    if abs((t % 1.0)) < 1e-6:  

        #Reference calculation

        # Position reference in the Hill frame of the debris
        rhoH_ref = np.dot(DCM_act.T,rhoB_ref)

        # Velocity reference in the Hill frame of the debris
        rhoDotH_ref = np.dot(DCM_act.T,np.cross(WBH.T,rhoB_ref.T).T)

        # Actual position and velocity of the servicer in the Hill frame of the debris   
        Xact =  np.array([X[0],X[1],X[2]])
        Vact =  np.array([X[3],X[4],X[5]])
        
        # Error calculation for the position in the Hill frame of the debris   
        deltaX = Xact-rhoH_ref
        
        # Error calculation for the velocity in the Hill frame of the debris
        deltaV = Vact - rhoDotH_ref
        
        # Calculate the control action according to the errors calculated previously
        # and the control gains K and P
        u = control(K, P, Xact, Vact, deltaX, deltaV)

                    
    # Propagation of the Servicer dynamics in the Hill frame of the debris          
    X = X + dt*EOM_Relative(X,mu,Re,u)

    
    #Tumbling body rotation dynamics of the debris
    # Attitude integration with MRP of the debris
    MRP = MRP + dt*mrp_dot(MRP,WBH)

    # Angular rates integration of the debris
    W = W + dt*wdot(W, I, urot, L)
            
    # DCM from Hill frame to debris body frame
    DCM_act = mrp_to_dcm(MRP)

    # Angular rate of the debris in the Hill frame
    WBH = W - np.dot(DCM_act,wH_0)   
        
    # Change to MRP shadow set to avoid singularities
    if np.linalg.norm(MRP) > 1:
            MRP = mrp_shadow(MRP)
 
    # Get coordinate of the servicer in the Hill frame of the debris
    x = X[0]
    y = X[1]
    z = X[2]
        
    # Calculate radial separation between the servicer and the debris
    delta_r = np.sqrt((r1+x)**2+y**2)-r1
    
    # Calculate the angular separation between the servicer and the debris
    deltaTheta = y/(r1+delta_r)
    
    # Calculate the along-track distance between the servicer and the debris
    delta_s = r1*deltaTheta


        
        

        