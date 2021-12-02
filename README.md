# Virtual-AI-Mouse
Modules used:
mediapipe, pyautogui and opencv

Process
1. Initializing camera, setup, plotting using opencv.<br>
2. Obtaining hand landmarks using mediapipe.<br>
3. Focussing only on 2 landmarks: 8->Index Finger Tip, 12->Middle Finger Tip.<br>
4. Hovering mouse using index finger.<br>
5. Register a click by bringing two fingers (middle and index) closer.<br>

To run:<br>
1. Simply Run main.py.<br>
2. Fps display functionality can be achieved by uncommenting the triple Quote comments.<br>

Optimizations:
1. Shifting the purple rectangle up, since bottom access becomes difficult. - Done<br>
2. Removing numpy and math imports by adding onlt required self made functions. to reduce code complexity and for better optimization.<br>
3. Further smoothening of movement and clicks.<br>
4. Optimizations for specific softwares for pointer to work with.eg: Paint, On-Screen Keyboard etc.
