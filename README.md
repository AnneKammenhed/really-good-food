<h1>Remember</h1>

python3 manage.py makemigrations --dry-run

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

<h1>Welcome to Good Food!</h1>

<h2>Background</h2>
This project is the fourth in my full stack developer course at Code Institute that I will be completing in october 2022. 

It is a restaurant booking app with a website to promote Good Food. I wanted to build the site without having to log in, but the User ID for booking is the only way to securely delete bookings.  


<h2>Development</h2>
I installed Django and the supporting libraries. Since I will deploy the project to Heroku I also installed gunicorn as the server that I will use to run Django on Heroku. 

The supporting libraries are postreql and psycopg2. 

The images will be on Cloudinary. 

I called the project "goodfood" in Django and the app is called "booktable". 

I went back and fourt during development between one or several models. There has been models for guest and TimeDateFields too but in this one there is one model called Booking. 

The guest-model has also been based on either ForeignKey User or a CharField. Since the requirement is to be able to erase bookings, I went with the User solution. It is a one to many relationship since Good Food likes its guests to come back but it is not possible for the same guest to book twice on the same time.

This app was created using three different repositories. In troubleshooting the first repository, I found that many changes to the models can make the latest changes clash with the first migrations. After removing the migrations files and migrating again there is still an issue of unapplied migrations and programming error in the admin panel where the admin form is visible for the models, but its not possible to see the list of bookings or menu items or to add anything to the database. Lots of thanks to both my mentor and the crew at tutor assistance for trying to help me out with this problem. The original kanban-board is in a project in this repository. 

The second repository was not connected to Heroku and there I succeeded in getting a model working to book times. 

To be sure not to run in to the same problem as in the first repository, I also created a third repository (not connected to Heroku) where I tried to develop the functioning model with different tests to connect the model to djangos TimeDateField. I also connected the User function since this is the solution that I found for the guest to be able to erase their bookings (requirement for the project).  


<h2>Deployment</h2>
Cloudinary
Heroku

<h2>Tests</h2>


------

<h2>Credits</h2>

This site is built on the Code Institute student template for Gitpod with preinstalled tools to get started. I reused the templates from the Django Blog walkthrough project for the html in this project.  

Django


---

Enjoy!

