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



If you have any questions or what to help out, send a pull request or reach out at [@josephmisiti](http://www.twitter.com/josephmisiti)
