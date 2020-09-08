STEPS FOR DOWNLOADING AND INSTALLING LOCALLY
1. Make sure virtualenv is installed or run `sudo pip install virtualenv`
2. Clone the github repository
3. cd into directory
4. pip3 install -r requirements.txt
5. Make sure you have Postgres installed
5.5 Might need to create the database manually first...? Or might be created automatically when running migrations?
6. Run `manage.py migrate` 
7. See the next section for steps to make sure the code is configured for local
8. Run `python3 manage.py runserver`
9. Go to `http://127.0.0.1:8000/`

STEPS FOR RUNNING LOCALLY, ONCE INSTALLED
1. Comment off AWS storage settings at end of settings.py
2. Uncomment STATIC_ROOT, STATIC_URL, STATICFILES_DIRS near end of settings.py
3. Comment toggle gallery/templates/collections.html to use cover_photo.name instead of cover_photo.url
4. Comment toggle gallery/templates/show_collection.html to use photo.image.name instead of photo.image.url


FILE STORAGE
- settings.py "MEDIA_ROOT" setting defines where files are stored.
- The "collections" model definition can further specify a subfolder, but because it doesn't, uploaded files are stored where "MEDIA_ROOT" specifies.
- A call to collections/{ID} hits urls.py, which loads views.show_collection
- views.show_collection uses Django ORM to load related photos, and passes them into the "show_collection.html" template
- "show_collection.html" template then creates a series of <img> tags, and sets the "src" attribute to...
    - {% static ''} to tap into Django's static file management feature
    - images/ to get into the images folder (which is where files are, per "MEDIA_ROOT")
    - "photo.image.name" to get the file name
    - For prod, will switch to instead use "photo.image.url", which will call the file from Amazon S3. No need to mess with {% static %} etc.


RANDOM NOTES
- "sjspencer" is the "project", and "gallery" is the "app". One project can have many apps.
- Admin:
    - Dad's login:
        - Username --> email
        - Password --> young muscle
    - My login:
        - Username --> LDAP
        - Password --> formula + Dad
- Worried that the requirements.txt file is full of junk? You can delete it and run "pip freeze > requirements.txt" to automatically generate a new one based on what's already installed. Note that this will not work for a fresh download from github... in that scenario, the existing requirements.txt file dictates what gets installed.
- AWS access credentials manually entered into the "settings" section of the Heroku project as "Config Vars"
- https://devcenter.heroku.com/articles/django-app-configuration


COMMANDS
    - DJANGO
        - python3 manage.py runserver
            - You can save edits to files without needing to restart the server, but if you add a new file, that does require a restart.
        - python3 manage.py 
            - Lists available subcommands
        - python3 manage.py makemigrations {app-name}
            - In this case, "sjspencer" is the project name, and the app is "gallery"
            - This creates new migration files based on the definitions in models.py
        - python3 manage.py migrate
            - This actually updates the database based on the new migration file
        - python3 manage.py createsuperuser
    - SASS
        - sass input.scss output.css
        - sass --watch input.scss:output.css 
            - Informs SASS to watch the file and update the CSS whenever SASS file changes.

TODO
- Do I need both static and staticfiles? Added the former to resolve a Heroku deploy error.
- Am I actually using Whitenoise? Remove?



