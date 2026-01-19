# Proximity-Operations-Tumbling-Debris
Capstone project for the Spacecraft Formation Relative Orbits Specialization offered by the University of Boulder, Colorado via Coursera

The simulation is about a mission of a servicer spacecraft approaching a tumbling debris object in low Earth orbit. The mission profile presented a series of proximity maneuvers that used continuous feedback control.

# Drifting Spiral Trajectory

The drifting elliptical relative orbit enables a full-angle inspection of the debris. The reference trajectories were computed using relative orbital elements (ROEs), with all dynamics modeled in the LVLH frame.

![task5](https://github.com/user-attachments/assets/f7d4ce55-b5b3-4b15-821d-aafe026f670f)

# Fixed Position relative to the debris

The servicer first helds a fixed position relative to the debris body frame, following a non-Keplerian reference trajectory.

![task7](https://github.com/user-attachments/assets/025e738b-9624-4bd7-b694-e3606e85205b)

# Final Approach Trajectory

The services approaches the debris maintaining a constant approach rate along a defined direction in the debris body frame. The servicer follows as weel a non-Keplerian reference trajectory.

![task8](https://github.com/user-attachments/assets/cea7bbb4-4114-4620-b0a0-128da2e1f538)

# Code Sample

A code sample of the propagator is included in the repository. The code sample shows the core logic of the orbital propagator, integration of attitude dynamics using a Runge-Kutta method. This code sample was written in Python language.
