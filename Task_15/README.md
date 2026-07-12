# Task 15 – URDF Robot Description and Visualization

## Overview

This project demonstrates the fundamentals of robot modeling in ROS 2 using URDF. The robot model was visualized in RViz, its links and joints were explored, the TF tree was inspected, and a simple modification was applied to the URDF model to observe the changes in visualization.

---

## Objectives

- Understand the structure of a URDF robot model.
- Visualize the robot using RViz.
- Explore Links and Joints.
- Inspect the TF Tree.
- Understand the role of `robot_state_publisher`.
- Understand the role of `joint_state_publisher`.
- Modify the URDF model and verify the result in RViz.

---

## Software and Tools

- Ubuntu 24.04
- ROS 2 Jazzy
- RViz2
- URDF Tutorial Package
- TF2 Tools

---

## Launch Command

```bash
ros2 launch urdf_tutorial display.launch.py model:=/home/$USER/Task_15/06-flexible.urdf
```

---

## Robot Structure

```
base_link
├── left_leg
│   ├── left_base
│   ├── left_front_wheel
│   └── left_back_wheel
├── right_leg
│   ├── right_base
│   ├── right_front_wheel
│   └── right_back_wheel
├── head
│   └── box
└── gripper_pole
    ├── left_gripper
    │   └── left_tip
    └── right_gripper
        └── right_tip
```

---

## Explanation of Links

### base_link
The main body of the robot. All other links are connected directly or indirectly to it.

### head
Represents the robot's head and is connected to the base through a continuous joint.

### box
A small box attached to the robot's head using a fixed joint.

---

## Explanation of Joints

### head_swivel
A continuous joint that allows the head to rotate.

### left_gripper_joint
A revolute joint that controls the left gripper.

### right_gripper_joint
A revolute joint that controls the right gripper.

---

## TF Tree

The TF Tree represents the relationship between all coordinate frames of the robot. It defines how every link is positioned relative to its parent and allows ROS 2 to compute transformations between frames.

---

## ROS 2 Topics

### `/joint_states`

Publishes the current position of the robot joints.

### `/tf`

Publishes the transformations between all robot frames.

---

## Robot State Publisher

`robot_state_publisher` reads the URDF model and publishes the robot transforms to the `/tf` topic according to the current joint states.

---

## Joint State Publisher

`joint_state_publisher` publishes joint values to the `/joint_states` topic and allows moving movable joints using the GUI.

---

## URDF Modification

The original URDF model was modified by changing the robot's blue material color. After relaunching the robot, the new color was successfully displayed in RViz.

---

## Results

### Robot Visualization

(الصورة)

### TF Tree

(الصورة)

### Joint States

(الصورة)
