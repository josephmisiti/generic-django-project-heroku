generic-django-project-heroku
=============================

Generic project directory structure for new django applications.

For more info, read my blog post:

https://medium.com/cs-math/f29f6080c131


#### Installation

First, get cookiecutter

```
$ pip install cookiecutter
```

Then execute the following command:

```
$ cookiecutter https://github.com/josephmisiti/generic-django-project-heroku.git
```

heroku buildpacks:set git://github.com/heroku/heroku-buildpack-python.git


#### Setting Up The Database

Login to Heroku and go here:

https://postgres.heroku.com/databases

Choose `Dev Plan` (free) and you should end up with a postgres database

https://postgres.heroku.com/databases/heroku-postgres-da4ace14-heroku-postgresql-olive

Dont worry about anything else, `databases_url` will take care of the rest


If you have any questions or what to help out, send a pull request or reach out at [@josephmisiti](http://www.twitter.com/josephmisiti)


#### Example Usage

First create your project:

```
(bar)JOSEPH-MISITI:Downloads josephmisiti$ cookiecutter https://github.com/josephmisiti/generic-django-project-heroku.git
You've cloned /Users/josephmisiti/.cookiecutters/generic-django-project-heroku before. Is it okay to delete and re-clone it? [Y/n] Y
Cloning into 'generic-django-project-heroku'...
remote: Counting objects: 158, done.
remote: Compressing objects: 100% (123/123), done.
remote: Total 158 (delta 54), reused 123 (delta 19), pack-reused 0
Receiving objects: 100% (158/158), 32.38 KiB | 0 bytes/s, done.
Resolving deltas: 100% (54/54), done.
Checking connectivity... done.
project_name (default is "project_name is the title of the project.")? heroku_test
repo_name (default is "repo_name is used for describing the directory structure.")? heroku_test
author_name (default is "Your Name")? Joseph Misiti
email (default is "Your email")? joe@getfetcher.com
description (default is "A short description of the project.")? Test Project
year (default is "2015")?
domain_name (default is "example.com")? heroku_test.com
version (default is "0.1.0")?
now (default is "2015/01/15")?
```

Next collect the static assets using `django-pipeline`:

```
pip install requirements.txt && ./manage.py collectstatic --noi
```

Finally run the server locally and go to `http://127.0.0.1:8000/`:


```
./manage.py runserver
```

OK, so it works locally, not lets push it to Heroku. Assuming you have an account, create an app (the name does not matter) and go to assuming you are setting in the base of your project folder:

```
heroku login
git init
heroku git:remote -a <HEROKU PROJECT NANE>
git add .
git commit -am "make it better"
heroku buildpacks:set git://github.com/heroku/heroku-buildpack-python.git
git push heroku master
```

Finally, sync your db on Heroku:

```
heroku run python manage.py syncdb
heroku run python manage.py migrate
```

And you should be able to login to the admin panel:

https://<HEROKU PROJECT NANE>.herokuapp.com/admin