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

When you push, you should see Heroku detect your Python app, the output should look similiar to this

```
(bar)JOSEPH-MISITI:tester josephmisiti$ git push heroku master
Counting objects: 61, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (47/47), done.
Writing objects: 100% (61/61), 89.76 KiB | 0 bytes/s, done.
Total 61 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Fetching custom git buildpack... done
remote: -----> Python app detected
remote: -----> Installing runtime (python-2.7.10)
remote: -----> Installing dependencies with pip
remote:        Collecting Django<1.8 (from -r requirements/common.txt (line 1))
remote:          Downloading Django-1.7.9-py2.py3-none-any.whl (7.4MB)
remote:        Collecting psycopg2==2.5.4 (from -r requirements/common.txt (line 2))
remote:          Downloading psycopg2-2.5.4.tar.gz (682kB)
remote:        Collecting django-model-utils==2.0.3 (from -r requirements/common.txt (line 3))
remote:          Downloading django_model_utils-2.0.3-py2.py3-none-any.whl
remote:        Collecting django-pgfields==1.4.4 (from -r requirements/common.txt (line 4))
remote:          Downloading django-pgfields-1.4.4.tar.gz
remote:        Collecting djorm-pgarray==1.0 (from -r requirements/common.txt (line 5))
remote:          Downloading djorm-pgarray-1.0.tar.gz
remote:        Collecting django-jsonfield (from -r requirements/common.txt (line 6))
remote:          Downloading django-jsonfield-0.9.13.tar.gz
remote:        Collecting django-localflavor==1.0 (from -r requirements/common.txt (line 7))
remote:          Downloading django_localflavor-1.0-py2.py3-none-any.whl (1.6MB)
```


Finally, sync your db on Heroku:

```
heroku run python manage.py syncdb
heroku run python manage.py migrate
```

And you should be able to login to the admin panel:

```
https://<HEROKU PROJECT NANE>.herokuapp.com/admin
```