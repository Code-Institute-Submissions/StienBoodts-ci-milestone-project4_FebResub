# Seafoam Winter E-commerce Store

This website offers visitors the chance to browse and buy knitwear.
The seller can showcase her handmade knitwear.

<img src="" width="500"/><br>

## User Experience
---

### _User Stories_

- #### **First Time Visitor Goals:**
1. As a first time user, I want to find out the purpose of the website immediately.
2. As a first time user, I want to find out what products are available.
3. As a first time user, I want to find out how I can buy the products.

- #### **Returning Visitor Goals:**
1. As a returning user, I want to find out how I can buy more products.
2. As a returning user, I want to access my profile and view previous orders.
3. As a returning user, I want to access my profile and edit info kept on file.

- #### **Frequent User Goals:**
1. As a frequent user, I want to find out how I can get in touch with the maker for custom orders.

### _Design_

- #### **Colour Scheme**

    <img src="" width="500"/><br>
   

- #### **Typography**

    <strong>Headings:</strong> Satisfy, [Google Fonts](https://fonts.google.com/). A bit playful and fun to match the fun activities.<br>
    <strong>Main font:</strong> Roboto, [Google Fonts](https://fonts.google.com/). Clear, legible without being too formal looking.

- #### **Wireframes**

    <img src="media/Wireframe Homepage.png" width="500"/><br>

    Wireframes for homepage.
    Made with []()).

    During the developing process a few changes were made to the lay-out.

## Features
---

### _Existing Features_

- __User Accounts__

    Users can log in to view address details and previous orders

- __Bag__

    Users can add products to bag and can view a snippet of the bag whenever new products are added.


### _Features Left To Implement_

- __Shop by colour__

    The original plan was to have a colour picker feature, but due to lack of time this wasn't implemented.

- __Custom order form__

    A specific order form where users can make custom orders.

## Technologies Used
---

### _Languages Used_

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [jQuery](https://en.wikipedia.org/wiki/JQuery)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### _Frameworks, Libraries & Programs Used_

1. [Django](https://www.djangoproject.com/)
    - Django was used for the structure of the backend.
1. [Bootstrap:](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
    - Bootstrap was used on parts of the website to make them responsive.
1. [Adobe Color:](https://color.adobe.com/)
    - Adobe Color was used to select the colour scheme and test its accessibility.
1. [Gitpod:](https://gitpod.io/workspaces)
    - Gitpod workspaces was used to create and edit code and push them onto the Github repo.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from the Gitpod.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts was used to import the 'Montserrat' and 'Nothing You Could Do' (logo) fonts into the style.css file which are used on all pages.
1. [Elephant SQL](https://www.elephantsql.com)
    - Elephant SQL is used to host the database


## Testing 
---

- [HTML](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [CSS](https://jigsaw.w3.org/css-validator/validator)
- [JSLint](https://www.jslint.com/)

### _Validator Testing_

- #### **HTML**

    - Error: 

- #### **CSS**

    - Error: 

- #### **JSLint**



### _Testing User Stories from User Experience (UX) Section_

- #### **First Time Visitor Goals:**


- #### **Returning Visitor Goals:**


- #### **Frequent User Goals:**

## Deployment
---

This project was developed on Gitpod, committed to Git and pushed onto the [Github repository](https://github.com/StienBoodts/horizon-animatie-CI-MP2) using Bash. 


##### Hosting of database on ElephantSQL

1. log into Elephant SQL
2. click 'Create New Instance'
3. Give a name and choose the free 'Tiny Turtle' plan, tags can be left blank
4. Select region closest to you
5. click 'Review'
6. then 'Create Instance'
7. return to Elephant SQL database and click database instance for the project
8. copy the database URL
9. Leave tab open, you'll need this in deployment later.

##### Heroku set up for database

1. log into Heroku
2. Click New to create a new app
3. Give the app a name and select region closest to you
4. Cick 'Create app'
5. Open settings tab
6. Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL
7. Leave tab open, you'll need this in deployment later.

##### Connect the database

1. in the Gitpod terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database: pip3 install dj_database_url==0.5.0 psycopg2
2. Update your requirements.txt file with the newly installed packages: pip freeze > requirements.txt
3. In your settings.py file, import dj_database_url underneath the import for os
4. Scroll to the DATABASES section and update the code so sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL. (DO NOT COMMIT)
5. In the terminal, run the showmigrations command to confirm you are connected to the external database
6. Migrate your database models to your new database
7. Load in the fixtures. Please note the order is very important here. We need to load categories first
8. Then products, as the products require a category to be set
9. create a new superuser for your new database
10. to prevent exposing our database when we push to GitHub, delete the url again from our settings.py - set it up using an environment variable
11. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
12. Click the Table queries button, select auth_user
13. When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database

##### Adjust settings
1. Make sure both databases are connected with an if statement
2. install gunicorn and add it to the requirements
3. Create Procfile
4. log into heroku in the terminal
5. enter heroku config:set DISABLE_COLLECTSTATIC=1 --app with app name added to the end
6. Add host name to Heroku app in allowed host in settings.py (also add local host)
7. 

 


To deploy the website from the repository onto Github Pages the following steps were taken:

1. log into Github
2. from the list of repositories, choose **StienBoodts/horizon-animatie-CI-MP2**.
3. Navigate to **Settings** at the top of the repository.
4. Choose **Pages** from the menu on the left of the page.
5. In the Source Section, select **Branch: main** in the drop down menu.
6. Leave **/(root)** selected in the next drop down menu.
7. Press **Save**
8. The page will refresh and the **link to the deployed website** will appear at the top.

## Credits & Resources
---

### _Content_ 


1. [Code Institute](https://codeinstitute.net/)
    - this project was based on the walkthrough project from Code Institute.
1. [https://stackoverflow.com/](https://stackoverflow.com/)
    - General searches to solve issues

### _Media_


1. Developers own> :)
