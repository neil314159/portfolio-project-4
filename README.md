# Book Barn Reviews

## Introduction



Book Barn Reviews is a site designed for book lovers around the world. When you read a great book, the first thing you want to do is tell someone else about it! This site lets you publish your own reviews and also look at reviews from other users to get new ideas. Users can interact with each other via a commenting system, and can also create a wishlist of books they have not yet got around to. The site is built with the Django framework in Python, and also uses HTML and CSS.

This is my fourth Portfolio Project for the Diploma in Software Development with the Code Institute.

The project demonstrates working CRUD implementations for a number of data models including Reviews, Comments, and Wishlist Items. 

<br>
![Screenshot of homepage](./media/readme/screenshotfrontpage.png)

<br>
[Visit the live website on Heroku here](https://book-barn-reviews.herokuapp.com/)

<br>




<br>
![intro](/docs/new.gif)
<br>
## Table of Contents

* [Planning](#planning)
* [Features](#Features)
* [User Input and Validation](#user-input-and-validation)
* [OOP and Data Model](#oop-and-data-model)
* [Future Features](#possible-future-features)
* [Third Party Libraries](#third-party-libraries)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Validation Testing](#validation-testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Planning

### Goals
* To present a simple, easy-to-grasp text interface with a clear logical flow
* Make the purpose and operation of the software clear 
* Provide feedback and guidance on user actions
* Gracefully handle user input and ensure data is recorded correctly
* Operate continuously in a loop without crashing

### Logical Flow

I created this chart to map out the flow of control through the program and help me understand where to direct the various functions.
<br>
![dashboardtitle](/docs/Flowchart.png)

# Features

## Main Menu
This is the home screen and main menu
* Simple, numbered menu options.
* Colourful ASCII art title.
* Only 1-5 accepted from keyboard, all other input is rejected.  
  
![main menu screenshot](docs/mainmenu.png)

## User Guide 
* Gives the user an overview of the function of the software
* Explains menu options
* Coloured text to highlight information
* User can easily return to main menu.

![user guide screenshot](docs/userguide.png)

## View At Risk Patients  
* Shows a table view of patient records
* Sorted by vaccine status and then by age to determine risk
* Contrast colours highlight actionable cases
* Menu options to go forward and back through pages of records
  
![at risk patients screenshot](docs/riskpatients.png)

## View All Patients  
* Alphabetically sorted list of all patients
* Offers user option to edit or delete a record
* User types in number of record from left-hand column and can then make and edit or deletion
* Software confirms whether or not you want to make these changes, if not you return to the main menu
  
![all patients screenshot](docs/allpatients.png)

## Add New Patient  
* List of guided questions to input new patient
* Answers validated to prevent incorrect data
* Some questions are sequential, so if you missed first vaccine you won't be asked about follow-up shots, as they are dependent on receiving the first one.
* Message displayed on successful addition of patient. In case of a problem with the API, an error message will be displayed.
  
![add new patient](docs/addnew.png)

## Progress Dashboard  
* Bar chart showing how many of the current patients have been vaccinated to each level.
* Will update as patient records change over time.
* Created using external library.
  
![Welcome screen screenshot](docs/dashboard.png)

## Update Patient 
* Select a current patient and update their vaccine history through series of prompts.
* Similar to when creating new user, questions are nested.
  
![Welcome screen screenshot](docs/update.png)

## Delete Patient 
* User selects patient via number on left-hand column
* The system confirms that a deletion is requested, otherwise returns to the main  menu
* A confirmation is displayed if the deletion was effective.
  
![Welcome screen screenshot](docs/delete.png)



## OOP and CRUD Functionality

This project was designed using Object Oriented Principles in mind. Here is an overview of the classes used to create the site:
### Clinic class
* This is the overall management class for the app, it takes in the data on loading, and also presents menu options to the user. It has helper functions to display data, clear the screen, create and edit patient records. It also sorts and filters the data in order to present it to the user.
### Patient class
* This represents the individual patient kept track of by the clinic. This class has a unique 6 digit ID, and attributes showing personal details and vaccination records. It has a method which calculates their age based on today's date and returns it to the Clinic class for sorting.
### Table View class
* The main functionality of this program is in presenting pages of patient records to the user. Rather than printing long lists which require scrolling, I wanted to allow the user to page forward and back through a table. This class takes in data and prints out a slice of it in table form based on which page number is currently selected. This allows the program menu to show data and options that properly persist over time rather than being reset.


## Future Features

### XXX
* ccc



#### Technologies Used

* Python
    * These Python modules were used for the project:
        * asgiref==3.5.1
        * cloudinary==1.29.0
        * coverage==6.3.2
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2.13
        * django-active-link==0.1.8
        * django-allauth==0.50.0
        * django-crispy-forms==1.14.0
        * django-extensions==3.1.5
        * gunicorn==20.1.0
        * oauthlib==3.2.0
        * psycopg2==2.9.3
        * pydot==1.4.2
        * PyJWT==2.3.0
        * python3-openid==3.2.0
        * pytz==2022.1
        * requests-oauthlib==1.3.1
        * sqlparse==0.4.2

* Of the above packages, the most important ones were:
    * Cloudinary, for storing both site and user images and providing static storage
    * AllAuth, for providing user authorization management. This package takes care of allowing users to register, log in and out, reste their passwords, and use email addresses for account  confirmation and password reset
    * Crispy Forms, which was used to provide easy Bootsrap styling to the forms generated by Django
* Django
    * Django is a mature, high-level Python framework used to develop and deploy websites
* HTML
    * HTML was used mainly to style the templates used by Django for displaying the front end of the site.
* CSS
    * A small amount of CSS was written to style the background and fonts for the project.
* Bootstrap
    * A comprehensive CSS framework used to quickly provide layout and styling for web pages
* Font Awesome
    * The Font-Awesome icon library was used for the social media links in the footer of the site.
* Heroku
    * The project was deployed on Heroku's cloud-based platform
* Heroku PostgreSQL
    * The database functionality was provided by the Heroku Postgres Add-on

#### Other Resources Used
* [Github](https://github.com) 
    * GitHub is used for version control and as a repository for the code of the project.
* [Gitpod](https://gitpod.io) 
    * Gitpod was the development environment for this site and linked to Github for storage and deployment.
* [MacOS Preview](https://support.apple.com/guide/preview/welcome/mac)
    * All screenshots were captured and edited with this program.
* Balsamiq
    * Used to develop and refine wireframe images in the planning stage of the project.
* Cloudinary API Refernce
    * This was used to understand how to apply image transformations when uplaoding and storing images on their service.


## Testing

## Testing Strategy

A comprehensive manual testing plan was used for this project. A full description of all of the procedures and methods used can be found in the [testing.md file here](TESTING.md). All functionality relating to user actions and CRUD operations was carefully examined. Wherever possible, testing was also related back to the acceptance criteria in the orginal Epics defined before development began.


## Notable Bugs

1. Slug Creation
    * Problem: The use of a Django slug is often desirable for publishing articles on a website as it helps to provide a more user-readable URL. In this project, I encountered problems in trying to ensure that no two articles with the same title could ever prodiuce an identical slug. Initially I used a third party component from the Django Extensions package, which was able to create a unique slug but failed when the title had more than one world. I then reverted to generating the slug manually but could not relaibaly ensure that the same slug would not exist for two reviews of the same book.
    * Solution: removed the slug from the Model used to represent the book reviews in the databse and swicthed to using an Int-based ID identifier isntead. This is slightly less readable but is very effective at guaranteeing uniqueness. In the future it would be possible to switch to a UUID-based identifier instead.

2. Success URLs
    * Problem: For most of the project I encountered issues when supplying a Success URL for the Comment Model. This is the address used to redirect to after the comment is created, and I had difficulty in properly capturing the ID of the review connected with the comment.
    * Solution: After reading and watching some tutorials on how to properly reference attached objects, I was able to fix the get_success_url function and properly redirect the user once they had written or edited a comment.







# Deployment

## Creating the Project
1. A new repository was created for the project on GitHub by clicking 'New Repository' on the GitHub user page, giving a name to the project.
1. The GitPod link created by the Chrome extension was clicked on the Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template).
1. This created a virtual workspace which was then linked to my GitHub account.
1. After writing code for the project, I used git commands add, commit and push which sent all the project files from GitPod to my GitHub repository.

## Deploying to Heroku
The project was deployed on the Heroku site by using these steps:
1. Log into Heroku after creating a user account if necessary.
1. Select the 'New' button and click 'Create New App'.
1. Choose a unique name for your app.
1. Add the buildpacks for Python and NodeJS from the settings page for your project. They must be added in this order.
1. Add the configuration variables for your app on the settings page. These include PORT=8000 and the credentials used for your API access.
1. On the settings page, click the 'Deploy' tab.
1. Select GitHub as the method for deployments.
1. Sign in when prompted with your GitHub login and search for the repository for your project.
1. Click the correct repository and click 'Connect'.
1. Under the deployment type section, you can choose between automatic deployment whenever you push updated code to GitHub, or manual deployment where you must confirm that you want the site updated.

## Local Deployment

#### Forking the repo on GitHub
1. Log into your GitHub account.
1. Navigate to the project page found [here](https://github.com/neil314159/portfolio-project-4).
1. Click the 'Fork' icon on the upper right hand side of the screen.
1. This action copies the code into your own repo so you can examine and edit it in the development environment of your choice.

#### Cloning to Gitpod
1. Install the Google Chrome Gitpod plugin found [here](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki).
1. Navigate to the project repository page [here](https://github.com/neil314159/portfolio-project-3).
1. Click the green GitPod button on the top right of the screen.
1. This will open the project in a virtual GitPod workspace.
1. Install the required libraries by executing the command 'pip3 install -r requirements.txt' in your GitPod terminal.


#### Download a zip file of the source code
1. Click this [link](https://github.com/neil314159/portfolio-project-4) to the project home page.
1. Click the 'Code' button on the right hand side.
1. Select "Download Zip'
1. Decompress the files on your own machine.
1. Open them in your local IDE such as VSCode.

# Credits

## Pictures

* All pictures used in designing the site came from [Unsplash](https://www.unsplash.com)
* Book covers came from [Amazon](http://www.amazon.co.uk)

## Coding Inspiration

[Very Academy on Youtube](https://www.youtube.com/channel/UC1mxuk7tuQT2D0qTMgKji3w) - Their series on Learning Django was useful for concepts around Class-Based Views <br>
[William Vincent books](https://wsvincent.com/) - His series on devleoping Django applications gave a good overview of the subject <br>
[Bootstrap Examples](https://getbootstrap.com/docs/5.2/examples/) - The example code provided here gave ideas on how to lay out and refine the presentation of the site. <br>

# Acknowledgements

* Thanks to CI Mentor Daisy McGirr for her advice and guidance.