<img width="1091" height="579" alt="Screenshot from 2026-05-15 21-59-02" src="https://github.com/user-attachments/assets/5a322b99-c956-4147-ab87-b41dbb14967b" />

<img width="1852" height="958" alt="Screenshot from 2026-05-15 20-27-20" src="https://github.com/user-attachments/assets/e32dfbf2-0d33-442d-aad2-def165aa8386" />

<img width="1025" height="701" alt="Screenshot from 2026-05-15 19-46-05" src="https://github.com/user-attachments/assets/8ed0a1b1-46d9-438b-a106-ee9a3df0dbcf" />

<img width="1025" height="701" alt="Screenshot from 2026-05-15 19-36-58" src="https://github.com/user-attachments/assets/6bb127ff-350c-44b6-ba04-8247deb5fc58" />

__________________________________________________________________________________________________________________________________________________
NOTES:

Each robot publishes its position and priority on two separate topics. Since these two streams are not synchronized, I handled it by always storing the latest received values for each robot.

In the traffic manager, I keep two dictionaries to store the latest position and priority for all robots.

A timer function is used to continuously check the updated data, calculate the distance between robots in real time, and decide the status.

If two robots are too close and one has higher priority, a DANGER message is printed. Otherwise, the system shows CLEAR.

___________________________________________________________________________________________________________________________________________________
VIDEO:

https://drive.google.com/drive/folders/1jZQfNC-qgmDz24Blifk8Y1gbTMyZvZQY?usp=drive_link
