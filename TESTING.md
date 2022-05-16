# Testing Report

## Manual Testing

## HTML/CSS Validation
![html & css](./media/testing/spreadsheet/html_css.png)

CSS validation was carried out with the Jigsaw CSS Validator service. There was only a small amount of custom CSS included in this project, with most of the styling being done through bootstrap classes. There were no errors returned, with one warning which is due to a limitation of how Jigsaw operates.

#### CSS Validation on Jigsaw
<img src="./media/testing/validation/css.png" width="300">

HTML Validation was carried out with the W3C validator. An early version of the site flagged an error where I the links in the drop-down menu were incorrectly wrapped in just 'a' tags rather than 'li' tags as well, this error was fixed and no further problems occurred.

#### Home Page W3C HTML Validation
<img src="./media/testing/validation/html/homepage.png" width="300">

#### Reviews Page W3C HTML Validation
<img src="./media/testing/validation/html/reviews.png" width="300">

#### Add Review Page W3C HTML Validation
<img src="./media/testing/validation/html/add_review.png" width="300">

#### Search Page W3C HTML Validation
<img src="./media/testing/validation/html/searchpage.png" width="300">

#### Category Page W3C HTML Validation
<img src="./media/testing/validation/html/category.png" width="300">

#### Profile Page W3C HTML Validation
<img src="./media/testing/validation/html/profile_page.png" width="300">

#### Wishlist Page W3C HTML Validation
<img src="./media/testing/validation/html/wishlist.png" width="300">

#### Logout Page W3C HTML Validation
<img src="./media/testing/validation/html/logout.png" width="300">


## Python Validation
![python](./media/testing/spreadsheet/python.png)

The Autopep8 package which comes with the Code Institute template was used to fix Python formatting errors in all files. This removed whitespace, fixed line spacing etc. There are a small number of errors remaining on setting.py and models.py . These are errors for lines being too long, and are due to a Cloudinary URL string and 4 Django authorization method names. All files were checked agains the [PEP8 validator](http://pep8online.com).

#### asgi.py Pep8 Validation
<img src="./media/testing/validation/python/bookbarn/asgi.png" width="300">

#### settings.py Pep8 Validation
<img src="./media/testing/validation/python/bookbarn/settings.png" width="300">

#### Project urls.py Pep8 Validation
<img src="./media/testing/validation/python/bookbarn/urls.png" width="300">

#### wsgi.py Pep8 Validation
<img src="./media/testing/validation/python/bookbarn/wsgi.png" width="300">

#### admin.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/admin.png" width="300">

#### apps.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/apps.png" width="300">

#### models.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/models.png" width="300">

#### templatehelpers.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/templatehelpers.png" width="300">

#### test_models.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/test_models.png" width="300">

#### test_views.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/test_views.png" width="300">

#### urls.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/urls.png" width="300">

#### views.py Pep8 Validation
<img src="./media/testing/validation/python/reviews/views.png" width="300">


## Accessibility
![access](./media/testing/spreadsheet/accessibility.png)
Accessibility testing was carried out with the [WAVE tool](https://wave.webaim.org/), all pages returned no errors found. All tags were properly filled in and there were no low-contrast areas of the side which would be difficult for users with poor vision. It should be noted that the online WAVE tool was only able to check pages where the user was not logged in. To check those pages I installed the Wave Chrome Extension which lets you check any page.

#### Home Page WAVE Test
<img src="./media/testing/wave/wave_homepage.png" width="300">

#### Reviews Page WAVE Test
<img src="./media/testing/wave/wave_reviews.png" width="300">

#### Login Page WAVE Test
<img src="./media/testing/wave/wave_login.png" width="300">

#### Signup Page WAVE Test
<img src="./media/testing/wave/wave_signup.png" width="300">

#### New Review Page WAVE Test
<img src="./media/testing/wave/wave_new_review.png" width="300">

#### Profile Page WAVE Test
<img src="./media/testing/wave/wave_profile.png" width="300">

#### Wishlist Page WAVE Test
<img src="./media/testing/wave/wave_wishlist.png" width="300">

#### Category Page WAVE Test
<img src="./media/testing/wave/wave_category.png" width="300">


## Navigation
![nav](./media/testing/spreadsheet/navigation.png)
This test case is to verify that all the main links in the navbar take the user to the correct page. These links were tested by multiple people on different devices over a number of days. All tests were passed with no problems.

## Browse Reviews
![browse reviews](./media/testing/spreadsheet/browse_reviews.png)
This functionality is available to both registered and unregistered users. This test case confirms that a user can browse through the selection of book reviews on the site, use pagination, select a review and see the details of that review.

## Reviews CRUD Functionality
![reviews crud](./media/testing/spreadsheet/reviews_crud.png)
The Review model is the main component of this project, and it is important to verify that all Create, Read, Update and Delete functionality works flawlessly. Users can log into the site and create a new review. They can then look at the details of the review, edit or delete the review. This process was tested many times over the course of development and works perfectly.

## Comments CRUD Functionality
![comments cruds](./media/testing/spreadsheet/comments_crud.png)
The Create, Read, Update and Delete operations all work function as expected for user comments. There were some initial problems early in development with attaching the comments to a review, but once I removed the slug field and used integer based ID fields to identify comments and reviews, this worked perfectly.

## Wishlist CRUD Functionality
![wishlist crud](./media/testing/spreadsheet/wishlist_crud.png)
The user wishlist is the third model that also utilises CRUD operations. Each user can add and remove books from their list, as well as toggling their status between read and unread. The site behaved as expected and no problems occurred.

## User Account
![account](./media/testing/spreadsheet/user_account.png)
There is a large amount of important functionality connected with the user profile. This area has been tested exhaustively to ensure everything works correctly. Django's built-in user management is very good, and using the AllAuth package has made handling user registration, login and logout, and password resets much easier to handle. I used the Sendgrid API for email delivery as it works better than a personal Gmail account. The site can email a new user to verify their account, and use the same email to reset their password if needed. The user can also delete their account if they wish.

## Search
![search](./media/testing/spreadsheet/search.png)
This test case tests if a user can enter a search term in the navbar search box, hit the enter key and be presented with a correct set of results. This functionality is available to all users registered and unregistered.

## Mobile
![mobile](./media/testing/spreadsheet/mobile_testing.png)
It is important to properly verify that the site works at multiple resolutions on different devices such as phones and tablets. The Bootstrap framework used in this project is well-suited to managing responsive designs and it was confirmed that the site works on small devices. The navbar and menu collapse down to a smaller menu which works well on small screens.


## User Stories

## Third Party Testing

## Unit Testing

