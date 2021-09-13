DISCLAIMER: This is not my mode. Code sourced from a website which I forgot :).

This is a simple project of automating chrome interent failure dinosaur. To perform this, PIL and pyautogui libraries are used. 
Before starting, make sure to get the screen pixel coordinates of your dino,an area few pixels away from your dino where obstacles are present, and the restart button. This requires trial and error.
This program is not optimised for a higher score.
On pressing X key the game will start. Dino will start running. The maximum score which I could achieve with limited optimisation is 308. Feel free o achieve a higher score.

SIMPLE EXPLANATION:
X key will start the program. Based on the grey scale value of the obstacles, a mean threshold value is calculated. Based on this value, the dino decides either to jump or keep running. PIL library is used for finding the mean grey scale value of obstacles. PyAutoGUI is used for auto clicking space button and restart button.

Medium article for an elaborate explanation
https://medium.com/analytics-vidhya/automate-chrome-dino-game-using-python-pyautogui-and-pil-eeb839005ccf
