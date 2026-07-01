<img width="1920" height="1080" alt="Screenshot from 2026-07-01 18-47-31" src="https://github.com/user-attachments/assets/b5c54cb6-e803-462f-823a-92a74de40b22" />
<img width="1920" height="1080" alt="Screenshot from 2026-07-01 19-07-50" src="https://github.com/user-attachments/assets/10b3cfcf-620d-4a12-be2b-5d403658b037" />
<img width="1368" height="850" alt="Screenshot from 2026-07-01 19-24-35" src="https://github.com/user-attachments/assets/f43d06ed-eba4-4edc-9b15-67b17a334a95" />

_________________________________________________________________________________________________________________________


NOTS:

Each robot publishes its position and priority using two separate topics. Since these messages do not arrive at exactly the same time, I store the latest position and priority of each robot.

The traffic manager uses two dictionaries to save the latest data received from all robots.

A timer runs periodically to compare the robots' positions, calculate the distance between them, and check if they are inside the safety zone.

If the distance is less than the safety distance and another robot has a higher priority, the system prints a Danger message indicating which robot should yield. Otherwise, it prints Clear.
____________________________________________________________________________________________________________________________


VIDEO:

https://drive.google.com/drive/folders/1UAc5_Z_5fxiQHgYMIdTc80VqqF41QJXN?usp=drive_link
