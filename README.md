# WarMaster Battle Log

[View the live project here.](https://warmaster-battle-log.herokuapp.com/)

![](/images/amiresponsive.jpg)

I love Warmaster (https://www.wm-revolution.com/), best wargame ever created!

For this reason I choose to create a script to keep track of the matches done with my group of friends.

WarMaster Battle Log is a terminal based designed for my WarMaster group of players, to generate log of every battle, in this way it will be easy to keep track and record progression through the campaign.

WarMaster Battle Log keeps track of the tournament battle scenario played, reporting all relevant game information.


## **UX**

I wanted to create a battle log generator for fun and to remember the epic moment for every campaign played with my friends.


#### **The ideal user:**

* WarMaster player


### **The log generator will help user to:**

* Provide some entertainment.
* Keep track of the played battles.
* Remember the topic moments for every battle.
* Help the Campaign referee to write a story at the end of the campaign.


## **Tournament Scenarios**

* Four different tournament scenarios are the final logs.
* As WarMaster player I want to have all the tournament scenario first, later on more scenarios will be added.


## **The Structure**

The script consists of only 1 page which is the terminal page. I am using Python to generate the data and create battle logs.

![](/images/flowchart.jpg)


## **The Scope**

To achieve my goal, I included the following features in my game:


### **Features**

* An epic opening banner.
* A list of four scenarios.
* A list of game elements to select in order to provide more scenario details.
* The user can leave the script pressing 5 and another epic banner will be shown.


### **Future Features**

* Add the complete Army List (23 Armies)
* Add the complete scenario list (more than 16 scenarios).
* Create a script to generate the Winner and Loser result and add it automatically at the end of every log.
* Create a function to export every battle log in a txt file to be saved for future reference.


## **The Design**

The design is very easy and because it is intended to be used for a very specific type of users (WarMaster players), some effort has been spent to create nice banners.
No graphics other graphics is intended to be used for this project.


## **Technologies Used**

* [Gitpod](https://gitpod.io/workspaces) I used this developer to write the code for this game.
* [Github](https://github.com/) Was used to host my repository and readme.
* [Heroku](https://id.heroku.com/login) To host my app and deploy here.


## **Testing**

### 1 As a new user, I want the navigation to be easy and fast
* After the banner loading, the scenario list is shown to be ready for selection.

![](/images/test_1.jpg)
![](/images/test_0.jpg)

### 2 As a user, you want to exit the script when no battle logs are reported
2 Pressing 5 you will get the exit message.

![](/images/test_2.jpg)

### 3 As a user, I want to be create and read battle log report.
* After adding game information the related scxenaio log is created.

![](/images/test_3.jpg)


## **Validation**

Becasue PEP8 (http://pep8online.com) was down at the time of my validation, I followed this procedure to validate my code and be sure was error-free:

### 1 Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results

![](/images/image_1.png)

### 2 Select pycodestyle from the list

![](/images/image_2.png)

### 3 PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

**No errors found during the validation**


## **Compatibility**

I tested the script across all major browsers on both desktop and mobile.
* Chrome
* Mozila Firefox
* Edge
* Safari
Although this is a web app it is visible on a mobile and tablets, even though it is not responsive.


## **Deployment**

This project was developed using Heroku, committed to git and pushed to GitHub using git commands.
You can clone this repository [Here](https://github.com/etherealsheep/Warmaster-Battle-Log)

To deploy this page to Heroku from GitHub repository, the following steps were taken:

1. In the Heroku dashboard I selected 'New' in the top right hand corner and clicked on 'Create new app'.
2. Then I Created the App name and Choose my region as Europe. Then selected 'Create app'
4. Then I selected Settings tab, and scrolled down to 'Buildpacks'. Here I added 'Python' clicked saved changes and then selected 'Node.js' and saved my changes again.
5. On top of the page I clicked on the 'Deploy' section, and I selected Github as my deployment method.
6. Then I selected 'Connect to Github, and searched for my repository name and clicked on 'Connect' to link my Heroku app to my Github repository code.
7. Scrolling down I have selected 'Enable Automatic Deploys' and after this I selected 'Deploy Branch' to deploy my project. I had to wait for it to build.
8. After it has successfully deployed a 'view' button appeared which took me to my deployed app.


## Credits

* Working on this project everything went well and straightforward.
* Warmaster is a game release in 2000 by Games Workshop (https://en.wikipedia.org/wiki/Warmaster).
* Warmaster stopped being officially supported by Games Workshop (GW) in 2013 and since then, a huge community of player keeps the game alive.
* Nowadays, WarMaster is seeing the biggest numbers of players ever seen before and the community is still increasing.