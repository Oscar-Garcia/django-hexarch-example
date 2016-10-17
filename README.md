# django-hexarch-example

This repository contains an example of how to use the concept of Hexagonal Architectures in a Django Project.
For the example we are going to start from the [Django Tutorial Poll example](https://docs.djangoproject.com/en/1.10/intro/tutorial01/).

## Step 0: Getting started

On this step we are going to start with the example as if we had just finished to complete the Django Tutorial. The only difference
in the code is that I have added some bootstrap CSS to the Django Templates.

For run the example you need to:
- Get the code: `git clone https://github.com/Oscar-Garcia/django-hexarch-example.git`
- Work on the Step 0: `git checkout step_0`
- Execute migrations: `python manage.py migrate`
- Create the superuser: `python manage.py createsuperuser`
- Run Django: `python manage.py runserver`

You should be able to navigate to the [admin](http://localhost:8000/admin) and add some polls and then fill some of
them in the [main page](http://localhost:8000/polls)

