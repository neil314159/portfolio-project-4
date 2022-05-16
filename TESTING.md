# Testing Report

## Manual Testing

## HTML/CSS Validation
![html & css](./media/testing/spreadsheet/html_css.png)

CSS validation was carried out with the Jigsaw CSS Validator service. There was only a small amount of custom CSS included in this project, with most of then styling being done through bootstrap classes. There were no errors returned, with one warning which is die to a limitation of how Jigsaw operates.

#### CSS Validation on Jigsaw
<img src="./media/testing/validation/css.png" width="300">

HTML Validation was carried out with the W3C validator. An early version of the site flagged an error where I the links in the drop-down menu were incorrectly wrapped in just 'a' tags rather than 'li' tags as well, this error was fixed and no further problems occured.

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

The Autopep8 package which comes with the Code Institute tenplate was used to fix Python formatting errors in all files. This removed whitespace, fixed line spacing etc. There are a small number of errors remaining on setting.py and models.py . These are errors for lines being too long, and are due to a Cloudinary URL string and 4 Django authorization method names. All files were checked agains the [PEP8 validator](http://pep8online.com).

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
![homepage](./media/testing/wave/wave_homepage.png)

#### Reviews Page WAVE Test
![reviews](./media/testing/wave/wave_reviews.png)

#### Login Page WAVE Test
![login](./media/testing/wave/wave_login.png)

#### Signup Page WAVE Test
![signup](./media/testing/wave/wave_signup.png)

#### New Review Page WAVE Test
![newreview](./media/testing/wave/wave_new_review.png)

#### Profile Page WAVE Test
![profile](./media/testing/wave/wave_profile.png)

#### Wishlist Page WAVE Test
![wishlist](./media/testing/wave/wave_wishlist.png)

#### Category Page WAVE Test
![cat](./media/testing/wave/wave_category.png)



## Navigation
![nav](./media/testing/spreadsheet/navigation.png)

## Browse Reviews
![browse reviews](./media/testing/spreadsheet/browse_reviews.png)

## Reviews CRUD Functionality
![reviews crud](./media/testing/spreadsheet/reviews_crud.png)

## Comments CRUD Functionality
![comments cruds](./media/testing/spreadsheet/comments_crud.png)

## Wishlist CRUD Functionality
![wishlist crud](./media/testing/spreadsheet/wishlist_crud.png)

## User Account
![account](./media/testing/spreadsheet/user_account.png)

## Search
![search](./media/testing/spreadsheet/search.png)

## Mobile
![mobile](./media/testing/spreadsheet/mobile_testing.png)

## User Stories

## Third Party Testing

## Unit Testing

