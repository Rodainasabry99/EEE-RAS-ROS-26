Screenshots of the successful installation
<img width="1050" height="819" alt="Screenshot from 2026-05-10 16-55-56" src="https://github.com/user-attachments/assets/262d950b-b945-44f4-a1e5-648fd384c165" />

terminal outputs
<img width="1855" height="987" alt="Screenshot from 2026-05-10 15-22-23" src="https://github.com/user-attachments/assets/3ab5ab3c-9dde-42fb-8bb2-918fe07ebf87" />

The exact command you used to draw your "Manual Star"

ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 2.5}}"
<img width="1855" height="987" alt="Screenshot from 2026-05-10 16-31-02" src="https://github.com/user-attachments/assets/d046d8ab-4c30-4b4d-81f8-e0a115a7d5cd" />
<img width="499" height="539" alt="Screenshot from 2026-05-10 16-42-43" src="https://github.com/user-attachments/assets/571a722d-e32f-4dad-8e35-4f7e450db5e2" />

A notes briefly explaining Nodes, Topics, and Services in your own words.
Nodes: are small parts of a ROS 2 system,Each node performs a specific task in the program
Topics: are communication channels used by nodes to exchange information
Services:are a communication method where a node sends a request and receives a response.
