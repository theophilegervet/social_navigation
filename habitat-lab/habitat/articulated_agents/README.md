Robot Design
==============================

Habitat supports different kinds of agents that can interact in the environment, including robots or humanoids. These agents are represented as articulated objects, consisting of multiple rigid parts (links) connected by joints to perform rotational or translational motion. This readme file details the design of these articulated agent modules, which robots inherit from. We provide the implementation of different robots under the `robots` folder.

---

## Articulated Agents's Component Design

1. **Control**
    - `manipulator.py` controls the arm and gripper joint angles.
    - `articulated_agent_base.py` controls the leg joint angles or base position depending on the morphology of the agent.

1. **Articulated Agent Module**
    - `mobile_manipulator.py` is a class that is built upon `manipulator.py` and `articulated_agent_base.py`. We kinematically simulate the robot to control its position.
    - `static_manipulator.py` is a class that is built upon `manipulator.py`. Since it is "static", it does not call `articulated_agent_base.py`.
    - `articulated_agent_interface.py` defines a generic agent interface.