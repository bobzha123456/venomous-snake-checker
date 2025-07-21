# venomous-snake-checker
The main porpuse of the project is using ai to identify the name, kind of the snake and how dangerous it is.
 

## The Algorithm

 
<img width="661" height="493" alt="code" src="https://github.com/user-attachments/assets/28d8e8bf-bb58-4604-b58e-22dde87458dc" />
This project depends on ai image recongation in the getson orin. In this case, I used google net to identify the imgae.

First, you will need to import the necessary functions for this.

Next, you need to parse the file name and retrieve the Google Net model for the AI. You can use a different model, change the name on lines 11 and 16

The next step is to get the image. 

Next, we will need to let Ai classify the image and provide us with the index number. With this index number, we can get the name of this animal. 

Now we want to know whether this snake is venomous or not.

If the user didn't give us a picture of a snake, print this animal is so cute.

## Running this project

Make sure you already have the Jetson-inferson project ready, if not go to https://github.com/dusty-nv/jetson-inference
You also want to make sure you have python downloaded, so you can run it.
Next download everything, put it into a folder .
Now run the code in the terminal, here is the example 
python3 my-recognition.py snake_testing.png
Paste this code into terminal, and you should be good 
if you want to download anouther snake pictue, make sure put it into the same folder, not download folder. Also change the snake_testing.png to your file name, make sure add png or jpg. 
[View a video explanation here](video link)
