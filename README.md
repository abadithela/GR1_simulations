# GR1_simulations

## visualization/graph_builder.py
This module contains the functions to create graphs given a GR1 product automaton. 
The orange arrows represent transitions taken by the environment, and the blue arrows represent transitions taken by the system.

## Runner Blocker
The file `runner_blocker.py` synthesizes a controller for the runner blocker example illustrated below.
![rb](self_loop_runner_blocker/StatesExplained.jpeg?raw=true)

The system, known as the runner, tries to eventually reach state 4 while always staying away from the state that the environment, or blocker, is in.

This synthesized controller is stored in `rb.py`.
