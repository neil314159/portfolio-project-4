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

View information about testing in the [testing.md file here](TESTING.md)

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

## UX

### Strategy

### Scope

### Structure

### Skeleton

### Surface



## Features

#### Static Homepage
The homepage explains the purpose of the site to new users, and explains that they can register for an account for extra advantages, or else start browsing the site directly.

![homepage](/media/readme/features/screenshotfrontpage.png)

#### Navbar
The navbar appears at the top of every page on the site, giving users access to every section of the site. Only logged in users will see the links for adding a review, the profile page and the wishlist page. Logged out users will see links to register and login instead of the logout link here.

![navbar](/media/readme/features/navbar2.png)

#### Dropdown and Search Menu
On the right hand side of the navbar are the drop-down category list and the search box. The category list is populated from the database and directs users to a page showing books from each genre. The search box takes the user's search term when they hit enter and provides a page of matching results.

![navbar](/media/readme/features/dropdown_search.png)

#### Reviews Index
This page provides the main functionality of the site, it shows a paginated list of all the reviews published on the site in reverse chronological order. The user can see all the reviews available here at a glance. The use of the cover images from the books makes the page more engaging and attractive.

![index](/media/readme/features/indexpage.png)

#### Create Review
This form allows the user to create their own review for publication on the site. The instructions at the top let them know which fields are mandatory. They enter the book details, upload a photo of the cover if they wish and click submit.

![index](/media/readme/features/create_review.png)

#### Book Review Card
This UI element gathers all the data about a book and presents it to the user in a variety of contexts, for exmaple in the reviews index, in the search page, in the category listing. It shows the book cover, the author and title of the book, the reviewer and the number of stars the reviewer gave the book. Both the cover image and the Read Reiew button provide a link to a detailed view of the book review.

![index](/media/readme/features/book_card.png)

#### Detailed Review
When the user clicks on an individual review, this page shows them the full details including the text of the review. The user is laso given the option to add the book to their wishlist or purchase it if the reviwer included a link. If the user is logged in and looking at one of their own revierws, they will laso be presented with buttons to edit or delete the review.

![index](/media/readme/features/review_detail.png)

#### Login/Signup
These two forms let unregistered users sign up for a new account, or registered users log back in. If the user forgets their password, there is a link for them to reset it if they have supplied an email account.

![index](/media/readme/features/signup.png)

![index](/media/readme/features/login.png)

#### Search and Category Views
These pages have a similar layout and function. They display the results of the user clicking on a category view from the drop down menu in the navbar, or from searching for a term in the search box in the navbar.

![index](/media/readme/features/search_results.png)
![index](/media/readme/features/category.png)

#### Profile Page
This page has two main functions. First, it allows the user to manage their email and password preferences. They can change their email address and their password. The user can also choose to delete their own account.

Below this section the user can also see a table listing all of the articles they have written, which can be clicked on to bring them to the article.

![index](/media/readme/features/profile.png)

#### Wishlist Page
Here the user can see a listing of all the books they have added to their wishlist. They can remove the book if they choose. If the original reviewer included a purchase link in their form, then the link will appear here and will be opened in a new window. 

Books in this list can also be marked as read or unread. Toggling this state with the Mark as Read button will add a strikethrough to the title to signal that the book has been read.

![index](/media/readme/features/wishlist.png)

#### Comments
The commenting system appears on individual review pages. Any logged in user can leave a comment on any review. They can also later edit or delete this comment. Additionally, the original author of any review page has the ability to remove comments on their pages if they wish, in order to provide a level of user moderation.

![index](/media/readme/features/comments.png)
![index](/media/readme/features/add_comment.png)

#### Footer
This footer appears at the bottom of every page on the site and provides easy access to the social media links for the project.

![index](/media/readme/features/footer.png)



## OOP Principles

This project made use of Object Oriented Programming principles in two main ways:
### Class-Based Views
* Django provides an implementation of generic class Views for Creating, Viewing, Updating and Deleting objects. If your model inherits from these classes, then the forms required for these user interactions are automatically generated and implemented, and the developer just has to provide a template to style the output and user interaction of these forms.




## Future Features

There a number of potentially beneficial user features which were not implemented in this sprint. You can view the Kanban board for this project [here](https://github.com/neil314159/portfolio-project-4/projects/1) to see which items were left to be devleoped at a future date.
* Book Cover API - rather than having to manually search for a book cover image, this could search and retrive the image for the user using the Google Books or Goodreads API.
* AJAX editing -  In order to have instant, on-page editing for categories, reviews and comments, it is necessary to implement AJAX using Javascript so that the user no longer has to refresh the page to see the results of their actions. It is also possible to use the HTMX library with Django to achieve similar functionality.
* Night mode - Some users prefer to able to chnage the colour scheme on a site themselves, and this feature would allow them a certain level of control.
* Social login - it is possible to use the AllAuth package to implement logins using social account credentials such as a Facebook or Google account. Technically this is not very difficult using third-party libraries, but your site must often be verified and approved by the API providers before you can use their credentials to log in users.
* Book of the week - a nice feature for the site administrator would be the ability to select and highlight a certain book review on the static home page for greater visibility.
* User messages - commenting has been implemented already but the ability for users to message eac other directy would be beneficial and engaging.
* Shared wishlists - since wishlists already exist for users, they could potentially share them with other users on the site for reading recommendations.





## Technologies Used

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
* Sendgrid
    * The SendGrid API allows Django to send out emails for user account operations without havng to use a personal email account to send from. This should lead to better deliverability and less chance of emaisl being marked as spam. I could only use SendGrid with my personal domain as they disallow Gmail addresses.
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


A comprehensive manual testing plan was used for this project. A full description of all of the procedures and methods used can be found in the [testing.md file here](TESTING.md). All functionality relating to user actions and CRUD operations was carefully examined. Wherever possible, testing was also related back to the acceptance criteria in the orginal Epics defined before development began.


## Notable Bugs

1. Slug Creation
    * Problem: The use of a Django slug is often desirable for publishing articles on a website as it helps to provide a more user-readable URL. In this project, I encountered problems in trying to ensure that no two articles with the same title could ever prodiuce an identical slug. Initially I used a third party component from the Django Extensions package, which was able to create a unique slug but failed when the title had more than one world. I then reverted to generating the slug manually but could not reliably ensure that the same slug would not exist for two reviews of the same book.
    * Solution: I removed the slug from the Model used to represent the book reviews in the database and switched to using an Int-based ID identifier instead. This is slightly less readable but is very effective at guaranteeing uniqueness. In the future it would be possible to switch to a UUID-based identifier instead.

2. Success URLs
    * Problem: For most of the project I encountered issues when supplying a Success URL for the Comment Model. This is the address used to redirect to after the comment is created, and I had difficulty in properly capturing the ID of the review connected with the comment.
    * Solution: After reading and watching some tutorials on how to properly reference attached objects, I was able to fix the get_success_url function and properly redirect the user once they had written or edited a comment.

3. Delayed Emails
    * Problem: Many of the emails necessary for users to register an account, confirm their email address and reset their passwords were taking a long time to arrive, up to 10 or 15 minutes.
    * Solution: After contacting SendGrid, they informed me that using this API to send emails on a free tier of service would often entail delays.


## Security

When this project was initally created, the secret key included with the Django installation was commited to Github accidentally. This key was quickly changed and hidden through the environment variables in env.py before deployment to Heroku.




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