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
##Robot Visualization

The following image shows the robot successfully loaded and visualized in RViz.

<img width="721" height="880" alt="Screenshot from 2026-07-13 01-57-16" src="https://github.com/user-attachments/assets/cd1fe8e5-1bdf-4425-b41c-66e987c2fb93" />



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

## Exploring the System

To better understand how the robot communicates within ROS 2, several commands were executed to inspect the active topics, monitor joint states, observe transform broadcasts, and generate the TF tree.

---

### Active Topics

The following command was used to display all active ROS 2 topics:

```bash
ros2 topic list
```

**Terminal Output**

<img width="904" height="161" alt="Screenshot from 2026-07-13 01-00-28" src="https://github.com/user-attachments/assets/bee86edc-02a0-489b-a48c-16ee0cca2f2a" />


---

### Joint States (Before Moving)

Before moving any robot joint, the current joint states were monitored using:

```bash
ros2 topic echo /joint_states
```

The output shows the initial values of all movable joints before any interaction with the Joint State Publisher GUI.

**Output**

<img width="367" height="574" alt="Screenshot from 2026-07-13 01-28-24" src="https://github.com/user-attachments/assets/6e7eaee4-8c7c-40f8-a216-a7f41f993e38" />


---

### Joint States (After Moving)

After adjusting the joints using the **Joint State Publisher GUI**, the same command was used again:

```bash
ros2 topic echo /joint_states
```

The joint values changed after moving the sliders in the Joint State Publisher GUI, confirming that the robot state was updated successfully.

**Output**

<img width="367" height="574" alt="Screenshot from 2026-07-13 01-35-24" src="https://github.com/user-attachments/assets/4bcef4f9-2209-44ce-a5ae-03b73254f19c" />


---

### Live Transform Broadcasts

The transform frames published by the robot were monitored using:

```bash
ros2 topic echo /tf
```

This command displays the real-time transformations between the robot's coordinate frames.

**Output**

<img width="367" height="574" alt="Screenshot from 2026-07-13 01-37-30" src="https://github.com/user-attachments/assets/37e6979a-6f3a-46d1-bbfa-79f9f3d29ad7" />


---

### TF Tree Generation

The complete TF tree was generated using:

```bash
ros2 run tf2_tools view_frames
```

The generated TF tree illustrates the parent-child relationship between all robot frames and shows how the links are connected through their corresponding joints.

**Output**

<img width="1685" height="545" alt="Screenshot from 2026-07-13 00-34-45" src="https://github.com/user-attachments/assets/c25514b5-b80c-40c9-9b20-3cd81e0d63e9" />

---

## ROS 2 Nodes

The following nodes were running during the visualization:

- `robot_state_publisher`: Publishes robot transforms based on the URDF model.
- `joint_state_publisher_gui`: Publishes joint states and allows manual joint movement.
- `rviz2`: Visualizes the robot model and TF frames.

---


## Robot State Publisher

`robot_state_publisher` reads the URDF model and publishes the robot transforms to the `/tf` topic according to the current joint states.

---

## Joint State Publisher

`joint_state_publisher` publishes joint values to the `/joint_states` topic and allows moving movable joints using the GUI.

---
## URDF Modification

A simple modification was made to the URDF file by changing the blue material color to another color. The robot was relaunched to verify the visual change in RViz.

### Before Modification

<img width="1362" height="920" alt="Screenshot from 2026-07-13 00-17-47" src="https://github.com/user-attachments/assets/d3d969c5-ad41-402c-8d22-3485809448eb" />


### After Modification

<img width="1362" height="920" alt="Screenshot from 2026-07-13 00-33-21" src="https://github.com/user-attachments/assets/dc7ae37f-2d66-42e4-b475-1499115d021a" />

---
## Video Demonstration

A short video explaining:
- How the robot was launched.
- How links and joints are structured.
- The TF tree and ROS 2 topics.
- The role of robot_state_publisher and joint_state_publisher.
- The URDF modification and its effect in RViz.

[Video Link](https://drive.google.com/drive/folders/11pDhmsecrjKdpjHLE4G8mS1-299AuPum?usp=sharing)

---

## Conclusion

This task provided practical experience with robot modeling using URDF in ROS 2. The robot was successfully visualized in RViz, its links, joints, and TF tree were explored, and a simple modification to the URDF model was verified through visualization.













