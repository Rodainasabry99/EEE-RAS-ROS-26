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

A simple modification was made to the URDF file by changing the robot's blue material color. The robot was relaunched to verify the change in RViz.

### Before Modification

<img width="1362" height="920" alt="Screenshot from 2026-07-13 00-17-47" src="https://github.com/user-attachments/assets/d3d969c5-ad41-402c-8d22-3485809448eb" />


### After Modification

<img width="1362" height="920" alt="Screenshot from 2026-07-13 00-33-21" src="https://github.com/user-attachments/assets/dc7ae37f-2d66-42e4-b475-1499115d021a" />

---


### ros topic list

<img width="904" height="161" alt="Screenshot from 2026-07-13 01-00-28" src="https://github.com/user-attachments/assets/3acfc6a6-6b0d-46f7-bf89-2de3912fd76a" />




### TF Tree

<img width="1685" height="545" alt="Screenshot from 2026-07-13 00-34-45" src="https://github.com/user-attachments/assets/17050977-c5ea-4b3c-af30-284b22de233b" />


### Joint States

