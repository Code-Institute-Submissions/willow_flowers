# Willow Flowers 

![responsive-img](documents/images/responsive-img.png)

[Willow Flowers](https://willow-flowers.herokuapp.com/) is a user-friendly e-commerce website built via main technologies [HTML](https://html.com/), [CSS](https://en.wikipedia.org/wiki/CSS), [JavaScript](https://www.javascript.com/about), [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/). 
The purpose of this website is to enable consumers to purchase items, such as plants and flowers, and create a user profile to store their previous orders and site favourites to access at any time. The website owner can upload, edit and delete products when necessary. 

# Contents
* [UX Design](#UX-Design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](##Skeleton)
    * [Surface](#Surface)
    * [Wireframes](#Wireframes)
* [Project Review](#Project-Review)
* [Databse](#Database)
* [Trello](#Trello)
* [Features](#Features)
    * [Existing Features](#Existing-features)
    * [Features Left to Implement](#Features-Left-to-Implement)
* [Technologies Used](#Technologies-Used)
    * [Other Tools](#Other-Tools)
* [Testing](#Tesing)
    * [Code Validation](#Code-Validation) 
    * [Browser Capability](#Browser-Capability)
    * [Responsive Testing](#Responsive-Testing)
    * [User Stories](#User-Stories)
    * [Feature Testing](#Feature-Testing)
    * [Problems Encountered](#Problems-Encountered)
* [Deployment](#Deployment)
* [Credits](#Credits)
    * [Content](#Content)
    * [Media](#Media)
    * [Acknowledgements](#Acknowledgements)



# UX Design 

## Strategy
Following the five planes of user experience design, the strategy has been separated into *Who*, *What*, *Where*, *When* and *Why* to initially  understand the website users’ requirements and needs. 

**Who** - The customer will be an individual looking to purchase flowers or a plant for an occasion such as a Birthday, New Baby, Congratulations, Wedding, Get Well Soon and Inside or Outside plants. The website will therefore not have a specific target demographic. 

**What** - The idea for this website is to design and build an e-commerce florist site whereby consumers can purchase and have products from the site delivered to recipients depending on the occasion at hand. They are also able to favourite specific items and keep them in their personal account favourites to revisit later. 

**Where** - The site will promote all products available, along with links to social media platforms to showcase to a wider audience. The site will also include a contact page, whereby consumers can contact the owners with any queries they have. 

**When** - The website will be available for users to make a purchase at any point in their journey. 

**Why** - Consumers will want to use this website to purchase florist products due to its easy navigation and information architecture layout, and simple payment process.

Following this, I also conducted some user stories to ensure the website will serve its purpose.

| As a:       | I would like to:                                | So that I can:                                            |
| :---        | :----                                           |  :---                                                     |
| **User A**    | Shop the florist range by occasion              | Purchase some flowers for a particular event              |
| **User B**    | Create a user account                           | Keep track of my previous purchases                       |
| **User C**    | Search for a particular flower                  | Order them for a specific occasion                        |
| **User D**    | Add multiple products to my basket              | Order more than one item at once                          |
| **User E**    | Add and delete items from my basket             | Decide on my final purchase at the end of my experience   |
| **User F**    | Receive an email confirmation of my order       | Have a copy of my order number                            |
| **User G**    | Favourite an item advertised on the site        | Come back to it and purchase later                        |
| **User H**    | Contact the owners of the business              | To thank them for my purchase                             |

<br>


| As a:       | I would like to:                                | So that I can:                                |
| :---        | :----                                           |  :---         
| **Admin A**   | Add, Update, and delete products                | Update the website when necessary             |
| **Admin B**   | Receive a copy of any contact forms submitted   | So, I can respond accordingly to the customer |


[Contents](#Contents)

## Scope
The features included in this website will consist of:
* The option to narrow down a product search through filtering the occasion. 
* A search page to pull up results based on name and description (through a term such as a colour).
* Personal login to view previous orders.
* An option to create a personal account- to complete a purchase or save items to your favourites.
* Shopping basket to display reserved items and a subtotal amount (£).
* Testimonials from previous customers.
* Online payments and order confirmation.

[Contents](#Contents)

## Structure 
Information architecture will be organised via product information. [Bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/) will be used to organise the product preview images on pages such as the search, the product pages and the basket to keep the layout clean and simple. Buttons will guide the user to complete their purchase, sign up, login or navigate to another page on the site. 

[Contents](#Contents)

## Skeleton
The navigation menu will be divided like so:

![nav-link](documents/images/nav-link.png)

[Contents](#Contents)

## Surface
Due to the fact there will be a lot of bursts of colour through the imagery of the products, I thought it would be best to keep surrounding colours minimal as to not over-crowd the page and avoid distraction for users. I will use an accent colour of Bubble-gum Pink (#ffc1cc) for the navigation menu, footer and buttons to keep the theme consitent. The font used will be [Playfair Display](https://fonts.google.com/specimen/Playfair+Display?query=playfair), taken from [Google Fonts](https://fonts.google.com/).

[Contents](#Contents)

## Wireframes 
Below is a preview of the Home Page wireframes for desktop, tablet and mobile created on [Balsamiq](https://balsamiq.com/). The individual desktop, tablet and mobile wireframes with all pages can be found [here](documents/wireframes).

![wireframes-preview](documents/images/wireframes-preview.png)


[Contents](#Contents)

# Project Review 

I constantly reflected through my wireframes during the development process for this project. Upon project completion, there are a few features which I refrained from implementing or changed during the development. 

**Toast Notifications**  – After much consideration, I had decided to not include toast messages into the final project. This was because I felt they weren’t completely necessary for the project at this stage. This is potentially something I will look to include further along the line of developing this project. 

![toast-messages.pgn](documents/images/toast-messages.png)

**The Basket Icon** – When it came to adding items to a user’s basket, initially I had designed for this to be done via clicking on a basket icon displayed in the product’s full description. I found out through my development that this was not actually the most feasible way to add an item to a user’s basket due to the quantity factor.

![basket-icon-2.pgn](documents/images/basket-icon.png)

**Testimonial Carousel** - Initially I had designed this to show two rotating customer testimonials at a time on the Home page. This initially caused issues as the testimonials would only show inside the left column, leaving the right blank. Due to this, after careful consideration, I had decided to only preview one testimonial at a time on the home page, spanning the full width of the page.

![testimonial-2.pgn](documents/images/testimonial-2.png)

[Contents](#Contents)

# Database
The database used for the development of the project was [SQLite](https://sqlite.org/index.html) which was later moved to [Heroku](https://dashboard.heroku.com/) using the [Postgres](https://www.postgresql.org/docs/) add-on. 

[Contents](#Contents)

# Trello 
To ensure I was staying organised and keeping in time with the deadline for this project, I created a [Trello](https://trello.com/en) board to list things I needed to do, were a working progress and what was completed. This helped me to ensure I was covering all aspects of the requirements for this project. 

![trello.pgn](documents/images/trello.png)

[Contents](#Contents)

# Features

## Existing Features 
*	Logo – The logo appears consistently on every page in the top left corner. Once clicked, this will also direct the user back to the Home page of the website. 

![logo.pgn](documents/images/logo.png)

*	Favicon -  The Favicon displays in the user’s browser. Should the user move to another tab, they can recognise from the favicon the Willow Flowers branding and direct back to the browser. 

![favicon.pgn](documents/images/favicon.png)

*	Icon Navigation – The top right corner of the website provides icon navigation links to Favourites, User Login, Basket and Search. These are visually accessible on every page allowing the user to quickly navigate to the required page.  

![icon-navigation.pgn](documents/images/icon-navigation.png)

*	Navigation Menu – The main navigation menu provides links to the Home page, a dropdown to the Flower products and Plant products, and a link to the Contact form. On a mobile view, these can be accessed via the responsive navigation bar. 

![navigation-flowers.pgn](documents/images/navigation-flowers.png)

*	Contact Form – Allows users to contact Willow Flowers directly by having them fill out a contact form which requires their name, email address and a message to submit.  

![contact.pgn](documents/images/contact.png)

*	Customer Testimonials  - These can be found at the bottom of the home page and are used encourage new consumers to purchase products from the site based on previous customer experiences. 

![testimonials.pgn](documents/images/testimonials.png)

*	X3 Image links – On the Home page is three circle images which provide links to the categories Birthday, Inside Plants and Wedding. When an image is clicked the user will be taken to that products category of items displayed as product cards. 

![x3-images.pgn](documents/images/x3-images.png)

*	Product Cards – While browsing product categories, users will be presented with product cards. These will provide brief information on an items name, image, and price with a button to “view more” which will take the user to that product’s full description. 

![product-cards.pgn](documents/images/product-cards.png)

*	Search Functionality – This will be found in the navigation menu and will take a user to a page whereby they are able to enter a word based on a product they would like to find. From here a list of products resulting to that search term will be displayed.

![search.pgn](documents/images/search.png)

*	Links to Social Media – Links to [Pinterest](https://www.pinterest.co.uk/), [Instagram](https://www.instagram.com/) and [Twitter](https://www.instagram.com/) are accessible in the bottom right of the page footer. These links will take a user directly to the social platforms in a new browser, to ensure they don’t venture off from Willow Flowers. 

![sm-links.pgn](documents/images/sm-links.png)

*	User Profile– Users have the option to create a personal profile whereby they can login and have access to their previous orders. The user will have to click on the user icon at the top of the page and then either login or sign up to create an account. 

![user-icon.pgn](documents/images/user-icon.png)

* User Profile - Login.

![login.pgn](documents/images/login.png)

* User Profile - Sign Up. 

![sign-up.pgn](documents/images/sign-up.png)

* User Profile - Email Verification.

![verify-email-address.pgn](documents/images/verify-email-address.png)

* User Profile - Password Reset.

![password-reset.pgn](documents/images/password-reset.png)

* User Profile - Account. 

![user-profile.pgn](documents/images/user-profile.png)

* User Profile - Sign out.

![sign-out.pgn](documents/images/sign-out.png)

*	Add Favourite Items – The favourites features allow users to essentially save an item for later. To add a product to their favourites, a user would have to click on a products full description and select the button "Add to favourites". 

![add-to-favourites.pgn](documents/images/add-to-favourites.png)

*   View Favourites - A user can access this list at anytime by clicking on the heart in the top right icon navigation which will direct them to their listed favourites.

![saved-favourites.pgn](documents/images/saved-favourites.png)

* No Favourite Items - If there are no items to display in the Favourites, the user will be presented with a message “No items in your favourites” and a button leading them back to the Home page. 


![no-favourites.pgn](documents/images/no-favourites.png)

*	Add Items to Basket – For a user to complete a purchase on a product, they would be required to add that item to their basket. This can be completed by selecting the quantity required on the items full description and selecting “Add to basket”. 

![add-to-basket.pgn](documents/images/add-to-basket.png)

*	Update Basket - The basket icon displayed in the top right corner updates when items are added to the basket and upon click, will take the user to a list of items currently in their basket.

![basket-total-nav.pgn](documents/images/basket-total-nav.png)

* Update Basket - To add or remove quantities from their basket, the user would manipulate the quantity arrows next to each product and select “Update Basket”. 

![update-basket.pgn](documents/images/update-basket.png)

* Backet Total - At the bottom of the basket page will display the basket total.

![basket-total.pgn](documents/images/basket-total.png)

* Empty Basket - If a user clicks on the basket icon but they have no items saved into their basket, they will reach a page informing them of "Your basket is empty" and a button redirecting them back to the home page.

![empty-basket.pgn](documents/images/empty-basket.png)

*	Checkout – To complete a purchase the user would be required to browse to their basket and click “Checkout”. They will be taken to a page whereby if they are a logged-in user, their personal information will be auto filled out. If not, the user will be required to fill in the necessary personal fields, along with their payment information. The payments were built using [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450319&utm_term=stripe%20payments&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQiAyJOBBhDCARIsAJG2h5fdOn7FyoK16NSYU2pwY4gixT-rSAGqwtX9Xm6m-7FI5Cl8J3Lf_90aAod7EALw_wcB) payments. 

![checkout.pgn](documents/images/checkout.png)

*	Checkout Confirmation – Upon completion of purchase, the user will be directed to a checkout confirmation page, informing them of the email address their confirmation has been sent to along with their order confirmation number. 

![order-confirmation.pgn](documents/images/order-confirmation.png)

*	Admin Profile – The Amin profile is created for the site superusers. The Admin view provides different access links and visuals to a standard user. 

![admin-user-icon.png](documents/images/admin-user-icon.png)

* Admin Update or Delete a product - By clicking on a product, they can update product information or delete the product from the website. 

![admin-update-delete.png](documents/images/admin-update-delete.png)

* Admin - Update A Products Information.

![admin-update-product.png](documents/images/admin-update-product.png)

* Admin Add A New Product - In the Admin profile, the Admin can upload new products to the website by filling out the required information. 

![admin-add-products.png](documents/images/admin-add-products.png)

[Contents](#Contents)

## Features Left to Implement

*	Live chat – Allow users to chat online with Willow Flowers to get a direct and fast response on their query.
*	About Us – Provide some information about how Willow Flowers was initially created and who are the employees involved, to give the website a more personal touch. 
*	Subscription Offer – Whereby a user can pay a monthly fee and receive a random product from Willow Flowers every month.
*	Contact Information - Provide information such as phone number, address and business hours in the far left of the footer to display on every page. 
*	GDPR Feature- Allowing the user to opt-in to receiving promotion email offers from Willow Flowers. 
*	Review System – Give users the option to review products on a star rated system based off their personal experience with the product. These would be visible on the product cards. 
*	Toast Notifications – Previewing a brief message to users when they have complete certain actions on the website.

[Contents](#Contents)

# Technologies Used
*	[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) – Used as the main language for the templates.
*	[CSS3](https://www.w3.org/Style/CSS/current-work.en.html) – Used to style the website.
*	[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) – Used for some frontend functionality.
*	[Python](https://www.python.org/) – Used for backend data manipulation.
*	[Django](https://www.djangoproject.com/) – Used to enable rapid development to create a secure and maintainable website. 
*	[Bootstrap](https://getbootstrap.com/)- Used HTML	 and CSS templates to feature on the website, along with some JavaScript plugins.
*	[Pillow](https://python-pillow.org/) – Used to add images to the database.
*	[Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) – Used to create user authentication, registration, and account.
*	[Gunicon](https://docs.gunicorn.org/en/stable/configure.html) – Used to server Django Python applications through WSGI interface on production.
*	[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) – Used to create forms for the website.
*	[db.sqlite3](https://sqlite.org/docs.html) – Used to hold the database while in development. 
*	[PostgreSQL](https://www.postgresql.org/docs/) – Used to store the primary data after deployment. 
*	[Git](https://git-scm.com/) – Used for version control.
*	[GitHub](https://github.com/) – Used to store my project repository.
*	[Gitpod](https://www.gitpod.io/) - Used to build the development of the website.
*	[Heroku](https://dashboard.heroku.com/) – Used to host the website.
*	[Stripe](https://stripe.com/docs) – Used to process payments on the website. 
*	[AWS](https://aws.amazon.com/) - Used for servers and storage.
    *	[S3](https://docs.aws.amazon.com/s3/index.html) – Used to store and retrieve data.
    *   [IAM](https://docs.aws.amazon.com/iam/) – Used for security.
*	[Webhooks](https://stripe.com/docs/webhooks) - Used to allow the web applications to communicate.
*	[Google Fonts](https://fonts.google.com/) – Used for website typography.
*	[Font Awesome](https://fontawesome.com/) - Used for icons.

## Other Tools 

*	[Adobe illustrator](https://helpx.adobe.com/uk/globalsearch.html?q=illustrator&start_index=0&country=GB&activeScopes=%5B%22helpx%3Alearn%22%2C%22helpx%3Ahelp%22%2C%22helpx%3Acommunities%22%2C%22adobe_com%3Aproduct%22%2C%22adobe_com%3Ablog%22%2C%22adobe_com%3Athought-leadership%22%2C%22adobe_com%3Apartner_extensions%22%2C%22adobe_com%3Aevents%22%2C%22adobe_com%3Acorporate%22%5D&scopeConfigs=%5B%7B%22value%22%3A%22helpx%3Alearn%22%2C%22renderStyle%22%3A%22horiz%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Atrue%7D%2C%7B%22value%22%3A%22helpx%3Ahelp%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Atrue%7D%2C%7B%22value%22%3A%22helpx%3Acommunities%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Atrue%7D%2C%7B%22value%22%3A%22adobe_com%3Aproduct%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Atrue%7D%2C%7B%22value%22%3A%22adobe_com%3Ablog%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Afalse%7D%2C%7B%22value%22%3A%22adobe_com%3Athought-leadership%22%2C%22renderStyle%22%3A%22horiz%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Afalse%7D%2C%7B%22value%22%3A%22adobe_com%3Apartner_extensions%22%2C%22renderStyle%22%3A%22horiz%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Afalse%7D%2C%7B%22value%22%3A%22adobe_com%3Aevents%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Afalse%7D%2C%7B%22value%22%3A%22adobe_com%3Acorporate%22%2C%22renderStyle%22%3A%22vert%22%2C%22seeMoreLink%22%3Anull%2C%22isSelectable%22%3Afalse%7D%5D&filters=%7B%22products%22%3A%5B%5D%7D&banners=%7B%22aboveResults%22%3A%7B%22count%22%3A3%2C%22ids%22%3A%5B%22auto%22%5D%7D%2C%22sidebar%22%3A%7B%22count%22%3A0%2C%22ids%22%3A%5B%5D%7D%7D&ctrls=%7B%22prodFilts%22%3Atrue%7D) - Used to create the logo and favicon.
*	[Balsamiq](https://balsamiq.com/) – Used to create the wireframes.
*	[Grammarly](https://www.grammarly.com/p?q=brand&utm_source=google&utm_medium=cpc&utm_campaign=brand_f1&utm_content=486649398671&utm_term=grammarly&matchtype=e&placement=&network=g&gclid=Cj0KCQiAyJOBBhDCARIsAJG2h5eR5CsKtHNwTNXGyR6v2KuJYOb0_ZWW2P49aqLL15s30lS7dI7peFwaAoGyEALw_wcB&gclsrc=aw.ds) - Used to check spelling and grammar.
*	[W3C Markup](https://validator.w3.org/) - Used this to check my HTML for errors and typos.
*	[W3C CSS](https://jigsaw.w3.org/css-validator/) - Used this to check the validity of my CSS.
*	[Jshint](https://jshint.com/) – Used to check my JavaScript code.
*	[pep8online](http://pep8online.com/) – Used to validate my Python code.
*	[dbdiagram](https://dbdiagram.io/home) – Used to initially format my database schema.
*   [Slack](https://slack.com/intl/en-gb/) - Used to query code challenges.
*   [Stack overflow](https://stackoverflow.com/) - Used to query code challenges.


[Contents](#Contents)

# Testing 

## Code Validation 

| Code:         | Validated on: | Results:      |
| -----------   | -----------   |---------------|
| HTML          |  [https://validator.w3.org/](https://validator.w3.org/)             |  Verified (Expected errors from python code)             | 
| CSS           |  [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)             |Verified - No Errors           
| JavaScript    | [https://jshint.com/](https://jshint.com/)  | Verified          |               
| Python        | [http://pep8online.com/](http://pep8online.com/)              | Verified              |

[Contents](#Contents)

## Browser Capability 

| Browser:         | Device Type:   | Compatibility:| Notes:         |   
| -----------      | -----------    |---------------|----------------|
| Google Chrome    | PC             | ★★★★★       | Every page works as expects.
| Mozilla Firefox  | PC             | ★★★★★       | Every page works as expects.
| Apple Safari     | PC             | ★★★★★       | Every page works as expects.
| Internet Explorer| PC             | ★★★          | Images appear slightly distaughted and the basket nav icon falls off the edge of the page.
| Opera            | PC             | ★★★★★       | Every page works as expects.

[Contents](#Contents)

## Responsive Testing 

| Device Size:     | Browser:        | Compatibility:| Notes:
| -----------      | -----------     |---------------|----------
| > 1200 px         | Google Chrome  | ★★★★★      |  
| > 992 px          | Google Chrome  | ★★★★★      |
| > 768 px          | Google Chrome  | ★★★★        | x3 images on the Home page appear down the left.
| > 576 px          | Google Chrome  | ★★★★        | Moved min-width to 1500vh - Footer can some times be too far down.
| > 768 px          | Google Chrome  | ★★★★        | x3 images on the Home page appear down the left.

[Contents](#Contents)

## User Stories 

Below are the solution to the user stories previously mentioned. 

| User Story:       | Solution:                                
| :---        | :----                                        
| **User A**    | -	Click on either ‘Flowers’ or ‘Plants’ on the main navigation menu and select the occasion required.             | 
| **User B**    | -	Select the user icon in the far-right corner. Select Sign up and complete the required fields to create your account.                         | 
| **User C**    | -	Select the search icon in the far-right corner, type in your search term in the search bar and select ‘Search’ to receive all products relating to your search.                 | 
| **User D**    | -	To add items to your basket, click on the product cards ‘View more’ button to view its full description. Using the quantity feature, select the amount required and click ‘Add to basket’. Repeat this with every product you would like to add to your basket.            
| **User E**    | -	Select the basket icon from the far- right corner, this will pull up all items in your basket. To remove an item, move the quantity feature to 0 (or the new amount required) and select ‘Update basket’.            | 
| **User F**    | -	Once a checkout is complete, the user will be presented with a checkout confirmation, informing them of their order confirmation number and the email address a copy of this has been sent to.      | 
| **User G**    | -	To add an item to your favourites, view the items full description and select the ‘Add to favourites’ button. If you are a registered user, the website will then ask you to log in to your account. If not, you will be asked to sign up to create a favourites list on your account. You can view your favourites at any time by clicking on the heart icon in the far-right corner.        | 
| **User H**    | -	Select ‘Contact’ via the main navigation, this will take you to a form requiring your name, email address and the message you would like to submit. Once complete, click ‘Submit’ and your query has been sent to the business owners.             | 

<br>


| Admin Story:       | Solution:                                |
| :---        | :----                                           |          
| **Admin A**   | -	Add a product: Login to your admin account, select Admin    from the user icon. This will take you to a from where you can add a new product. - Update a product: Login to your admin account, click on a products full description you would like to update, select the ‘update’ button. This will take you to a form with the product details pre-filled allowing you to update details where necessary. - Delete a product: Login to your admin account, find the product you would like to delete and view its full description. Select the ‘Delete’ button to remove the item from the site.
| **Admin B**   | -	Once a customer has completed the contact form, a copy of the information and message will be sent to the website owners email inbox. 

[Contents](#Contents)

## Feature Testing 

Below is a list of all features tested to ensure they are working properly:

- [x]	Navigation links work – Desktop/ Tablet/ Mobile
- [x]	Home page hero carousel slides 
- [x]	X3 Home page image links work to correct landing pages
- [x]	Testimonial carousel slides
- [x]	Social media icons link correctly 
- [x]	Navigation ‘Flowers’ and ‘Plants’ menu pulls up correct categories 
- [x]	‘View More’ button on Bootstrap product cards takes user to full description of the item
- [x]	Add/ remove items in favourites
- [x]	Add/ remove items in basket
- [x]	Favourites asks user to login/ sign up before adding items 
- [x]	Favourites pulls up favourite items OR informs user of no items in their favourites 
- [x]	Basket displays all items added to basket OR informs user of no items in their basket
- [x]	Update quantity on basket items 
- [x]	Basket (£) icon updates once a user has added to their basket
- [x]	Contact form- required fields work and submit sends form to hosted email address 
- [x]	Login / Sign up/ Forgot password/ Verify Email links work
- [x]	User profile- View personal information and any previous orders 
- [x]	Admin- Add product to the website
- [x]	Admin- Update product information
- [x]	Admin- Delete product from the website
- [x]	Checkout link works from user’s basket 
- [x]	Checkout form required fields and card information is correct
- [x]	Checkout confirmation page displays users email and confirmation number
- [x]	Search pulls up all products relating to that search term
- [x]	All buttons direct users to the correct landing pages

[Contents](#Contents)

## Problems Encountered 
* Gitpod showing degraded performance on dashboard, workspace and automatic docker image builds 06/02/2021 – 08/02/2021.

* Media and Static files won’t load after adding AWS to website– After thoroughly checking the AWS Management Console and S3 Management Console, I had discovered that the code linking to the Media and Static files needed to be updated in order to link the correct URL to the images and static files.

* Favicon- Initially kept in the MEDIA folder, it would never link properly- After conducting some research I moved it to the static folder and re-coded the link I the base.html template and it then worked on every page.

* New CSS failing in development - New CSS written in mid-way through the project was failing to work in the browser- to solve the issues I had to recreate the work space by downloading my db.sqlite3 file to my PC, closing the current Gitpod workspace, clicking Gitpod on the repository in my GitHub respository, opening the new workspace, uploading the db.SQlite3 file from my PC and then reinstall the requirements.txt file to allow for Django to work. Once I had done this and ran the project all new CSS was working.


[Contents](#Contents)

# Deployment 

The repository for this project is hosted through [GitHub Pages](https://github.com/) and is deployed live through [Heroku](https://dashboard.heroku.com/).

To deply my project I followed the below steps:

1.	Login to Heroku
2.	Create a new app and give it a name
4.	Choose location closest to me (EU)
5.	Go to resources and select new Postgres database
6.  In Gitpod- `install pip3 install dj_database_url`
7.	In Gitpod - `install pip3 install psycopg2-binary`
8.	In the terminal type `pip3 freeze requirements.txt`
9.	In `settings.py`  - `import dj_database_url`
10.	Scroll to database settings and comment out default configuration variable 
11.	Replace default database with `dj_database_url.parse()`
12.	Go to Heroku configuration variables and get the Postgres database_url and paste it into the parse() and save
14.	Type `python3 manage.py migrate` into the terminal 
15.	Import category data- load categories `python3 manage.py loaddata categories`
16.	Import product data- load categories `python3 manage.py loaddata products`
17.	Create a superuser in the terminal - `python3 manage.py createsuperuser`
18.	Enter: Username, Email, Password 
19.	Remove Heroku database configiuration variable and uncomment the original so database URL doesn't end up in version control
20.	Commit changes
21.	Use if statement in `settings.py`- when app is running via Heroku the data base URL Environment variable will be defined, connect to Postgres and otherwise use SQLite
22.	In the terminal type - `pip3 install gunicorn`- web server - freeze in `requirements.txt` file 
23.	Creat a  `Procfile` 
24.	Run gunicorn to serve the Heroku app
25.	Login to Heroku from the terminal 
26.	Temporarily disable `collect static = 1`
27.	Add allowed hosts name to Herkou app in `settings.py` (and local hosts so Gitpod still works)
28.	Add and commit changes and push to Github
29.	Gitpush Herkou master to deploy to Heroku
30.	Set up automatic deployment in Heroko- go to the deploy tab and connect to the Github repository and enable automatic deployment
31.	Add secret key to Heroku configuration variables
32.	In `settings.py`, replace the secret key with a call to get it from the Environment Varaibles
33.	Set `debug = true` if development is in environment variables
34.	Commit changes and push to Github
35.	Go to Herkou and check the building progress
36.	Store static files and images in AWS S3 
37.	Create a AWS account 
38.	Sign in to AWS Management 
39.	Search for S3 and open it 
40.	Create a new bucket to store files
41.	Go to properties and turn on static website hosting and save
42.	Permissions- pass in CORS configuration, bucket policy- policy generator S3 bucket policy, allow all principles, action is get object
43.	Copy ARN and paste into the ARN box
44.	Click add statement 
45.	Generate policy- copy policy into bucket policy editor 
46.	Add `/*` to end of resource key
47.	Click save
48.	Access control list tab set the list objects permission to everyone
49.	Create a user to access S3 bucket
50.	Open IAM and create a group, then access policy, assign the user to the group
51.	Download and save .CSV file
52.	Install `boto3` and Django storage 
53.	Freeze into `requirements.txt` file
54.	Add storages to installed apps
55.	In `settings.py` add an if statement for Heroku by using `USE_AWS` 
56.	Add the storage bucket name, AWS region name, AWS secret access key
57.	Add AWS keys to Herkou configuration variables 
58.	Add `USE_AWS = True` to Herkou configuration variables 
59.	Remove disable collect static variable from Herkou configuration
60.	In `settings.py` inform Django of where static files are coming form in production 
61.	Create custom storages file
62.	Import both settings from `Django.conf` and `S3boto3` storage 
63.	Create custom class and store static and media files from location in settings 
64.	In `settings.py` - static files use the storage class just created 
65.	Repeat with media files 
66.	Override and set static & media files custom domains media location 
67.	Add and commit changes and push
68.	Check the build log in Heroku to see if the files were collected
69.	Go to S3 and check for the static folder in the bucket 
71. Go to S3 create a new folder called media 
72.	Upload - add files- select all product images and click next
73.	Manage public permissions grant public read access 
74.	Click next and then upload 
75.	Go to Django admin and confirm superuser's email 
76.	Add stripe keys to Heroku configuration variables
77.	Go to Webhooks, add end point, add URL for Heroku app followed by `/checkout/wh/` and select receive all events and add end point 
78.	Add Webhooks signing secret to Herkou configuration variables 

[Contents](#Contents)

## Deploy code locally using the CL

If a developer was interested in running my code locally, then they would need to follow the below steps:

1.	Login to GitHub and navigate to the main page of the repository you are wanting to clone.
2.	Above the list of files, click the green button with a downwards arrow “Code”.

![clone-1.pgn](documents/images/clone-1.png)

3.	To clone the repository using HTTPS, under “Clone with HTTPS”, click the clipboard icon. To clone the repository using a SHH key, including a certificate issued by your organisation’s SSH certificate authority, click “Use SSH” and then click on the clipboard icon. To clone the repository using GitHub CLI, use click “Use GitHub SLI” and then click on the clipboard to copy the URL.

![clone-2.pgn](documents/images/clone-2.png)

4.	Open Git Bash.
5.	Change the current working directory to the location where you want to clone the directory.
6.	Type “git clone”, and then paste the URL you copied above.
7.	Press Enter to create your local clone

### Environment Variables

You will need to set up the following environment variables on your system:

| Variable Name:        | Used For:                                                         | 
| :---                  | :----                                                             |  
| DATABASE_URL          | Deployment Only – Sets hosted Postgres database                   | 
| SECRET_KEY            | Used by Django                                                    | 
| STRIPE_PUBLIC_KEY     | Need for Stripe payments                                          | 
| STRIPE_SECRET_KEY     | Need for Stripe payments                                          | 
| STRIPE_WH_SECRET      | Need for Stripe payments                                          | 
| USE_AWS               | Deployment only – to tell Django to use S3 instead of local files | 
| AWS_ACCESS_KEY_ID     |  Need for S3 Bucket static files                                  | 
| AWS_SECRET_ACCESS_KEY | Need for S3 Bucket Static files            | 
| EMAIL_HOST_USER       | Need for email verifications and contact      |
| EMAIL_HOST_PASSWORD   | Need for email verifications and contact  |


Should you wish to access the URL to the website, that can be found via: [https://willow-flowers.herokuapp.com/](https://willow-flowers.herokuapp.com/)

[Contents](#Contents)

# Credits 

## Content
Customer Testimonials were written by friends Maddy Darvell, Bill Mold and Daisy Lewis.

All product descriptions were written by me. 

[Contents](#Contents)

## Media
The flower and plant images used for this website were taken from:
*	[Pexels](https://www.pexels.com/)
*	[Pixabay](https://pixabay.com/)

[Contents](#Contents)

## Acknowledgements
I received inspiration from this project due to the fact I have placed more orders for floral gifts in this past year then I believe ever before. 
I would like to thank Tutor support, especially Igor Basuga, for his continued help and patience during challenging times on this project. My Mentor, Aaron Sinnott for providing helpful guidance throughout and making the process as logical as he could. 

[Contents](#Contents)

