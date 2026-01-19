# Proximity-Operations-Tumbling-Debris

Capstone project for the Spacecraft Formation Relative Orbits Specialization offered by the University of Boulder, Colorado via Coursera.

This project simulates a proximity operations mission in which a servicer spacecraft approaches and inspects a tumbling debris object in low Earth orbit. The mission profile consists of a sequence of controlled proximity maneuvers executed using continuous feedback control.

## Drifting Spiral Trajectory

A drifting elliptical relative orbit is used to enable full-angle inspection of the debris. Reference trajectories are defined using Relative Orbital Elements (ROEs), with the dynamics modeled in the LVLH frame.

![task5](https://github.com/user-attachments/assets/1d61b8b3-297c-462d-ac04-081bfe50ddba)

## Fixed Position Relative to the Debris

The servicer maintains a fixed position with respect to the debris body frame by following a non-Keplerian reference trajectory.

![task7](https://github.com/user-attachments/assets/0fc6cd5d-f0e3-4ca0-82b4-f3d71fda3f41)

## Final Approach Trajectory

The servicer approaches the debris while maintaining a constant approach rate along a predefined direction in the debris body frame. This phase also follows a non-Keplerian reference trajectory.

![task8](https://github.com/user-attachments/assets/e18e56a4-9515-42eb-b09a-5df5d83e2ed9)

## Code Sample
A code sample of the orbital propagator is included in this repository. The sample illustrates the core logic of relative motion propagation, reference trajectory generation and tracking, and feedback control implementation. Numerical integration of the relative dynamics is performed using a first-order (forward) Euler method implemented in Python. The sample corresponds to the most representative maneuver among those described above, namely the servicer maintaining a fixed position with respect to the debris body frame during proximity operations.
