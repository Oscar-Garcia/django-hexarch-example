# django-hexarch-example

I have made some [slides](https://github.com/Oscar-Garcia/django-hexarch-example/blob/master/hexagonal_django.pdf) 
of how Hexagonal Architectures can be used in Django. 

For testing the presented concepts that I have created an example in this repository based on the 
[Django Tutorial Poll example](https://docs.djangoproject.com/en/1.10/intro/tutorial01/).

There are different branches to be able to understand the transformations on the code step by step.

## Step 0: Getting started

On this step we are going to start with the example as if we had just finished to complete the Django Tutorial. The only difference
in the code is that I have added some bootstrap CSS to the Django Templates.

For run the example you need to:
- Get the code: `git clone https://github.com/Oscar-Garcia/django-hexarch-example.git`
- [Install and create a virtualenv](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
- Install required libraries: `pip install -r requirements.txt` 
- Execute migrations: `python manage.py migrate`
- Create the superuser: `python manage.py createsuperuser`
- Run Django: `python manage.py runserver`

You should be able to navigate to the [admin](http://localhost:8000/admin) and add some polls and then fill some of
them in the [main page](http://localhost:8000/polls)

## Step 1: Adding some tests 

On this step some tests are added using [Py.test](http://pytest.org/) to be sure everything works as expected.

- Work on the Step 1: `git checkout step_1`
- Install new dependencies: `pip install -r requirements.txt`
- Run tests: `py.test`

Tests should run fine!

## Step 2: Cleaning the view

The view had some application and business logic and it is accessing the database, we are going to remove those
dependencies on this step and apply hexagonal architecture.

After the changes tests should pass unmodified and the application should be fully functional.

- Work on the Step 2: `git checkout step_2`
- Run tests: `py.test`
- Run Django: `python manage.py runserver`

## Step 3: Exploiting the benefits of the hexagonal Architecture.

In this final database we show the possibility of run tests on the domain isolated from the framework, also we
see how different views can be used without changes in the core model. As an example the same logic is used for
displaying the polls in HTML and in JSON.

- Work on the Step 3: `git checkout step_3`
- Run tests: `py.test`
- Run Django: `python manage.py runserver`
