
RANDOM NOTES
"sjspencer" is the "project", and "gallery" is the "app". One project can have many apps.
Admin...
  Username --> email
  Password --> young muscle

  Username --> LDAP
  Password --> formula + Dad
- Worried that the requirements.txt file is full of junk? You can delete it and run "pip freeze > requirements.txt" to automatically generate a new one based on what's already installed. Note that this will not work for a fresh download from github... in that scenario, the existing requirements.txt file dictates what gets installed.

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

AWS ACCESS CREDENTIALS
- For devel, these are stored in ".env".
- For Prod, these were manually entered into the "settings" section of the project as "Config Vars"

DJANGO
- https://devcenter.heroku.com/articles/django-app-configuration


COMMANDS
python3 manage.py runserver
 - You can save edits to files without needing to restart the server, but if you add a new file, that does require a restart.

python3 manage.py 
- Lists available subcommands

python3 manage.py makemigrations {app-name}
- In this case, "sjspencer" is the project name, and the app is "gallery"
- This creates new migration files based on the definitions in models.py

python3 manage.py migrate
- This actually updates the database based on the new migration file

python3 manage.py createsuperuser



