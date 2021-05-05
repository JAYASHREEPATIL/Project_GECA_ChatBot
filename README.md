# Project_GECA_ChatBot

## How to run rasa/project:
### Step 1: 
$ rasa train
### Step 2: 
$ rasa run -m models --enable-api --cors "*" --debug

## Git Commands:
### for updating your working domain/ Project :
####
$ git pull

### for adding/push data from your system on git repo:
#### 
$ git push

## for push data from your system on git repo:
### follow below process:
#### => see the status of your system so, you know what are the changes you have done: command :->      
$ git status
#### => then add required files one by one : commnad :-> 
$ git add "file name which u want to add"
#### => then commit recently added file : commnad :-> 
$ git commit -m  "here you can add comment on added file(give short info about that file)"
#### => then finally push your file : commnad :->
$ git push

# Steps to create ngrok funnel 
### Download ngrok application
### download WAMP server
1)Open the project in pycharm <br />
2)Run action server by typing the command rasa run actions <br />
3)Run api server by typing the command  rasa run -m models --enable-api --cors "*" --debug same time in another terminal <br />
4)start ngrok prompt and type command ngrok http portno (port no. on which api server is running) <br />
5)One global mapped url will be generated  for local api server <br />
6)In UI/static//js/scripts.js file you will see one localhost address change that to this globally mapped address by ngrok and save the file <br /> 
7)In Wamp folder there is one folder www copy UI folder of our project in this directory (location:C:\wamp64\www) <br />
8)Start apache server and type localhost on browser after server starts<br />
9)Open another ngrok prompt and type command ngrok http 80 (80 is standard port number on which wamp server runs. By running this command we are generating globally mapped url for our local geca.html page)  <br />
10) Once this golbal mapping is generated you can put it in your browser and run the bot globally and can even share it with anyone. 
<br />

