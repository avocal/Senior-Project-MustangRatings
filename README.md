# MustangRatings
A rebuilt website of Polyratings for Cal Poly; Senior Project

# Setup Django 

Note: Better to run on Linux/MacOS

Using Ubuntu - Setting up System for Django 

**Step 1: Install python3**
> sudo apt udpate

> sudo apt install python3

**Step 2: Install pip**
> sudo apt update

> sudo apt install pip

**Step 3: Install virtual environment**
> sudo apt update

> sudo apt install virtualenv

**Step 4: Create virtual environment in a directory**
* ex: 
    > $ mkdir Django_tutorial

    > $ cd Django_tutorial 

    > $ python3 -m virtualenv env //creates a virtual environment called env

**Step 5: Activate virtual environment**
* > $ source env/bin/activate

* Should see something like: 
    > (env) avocal@ubuntu:~$ 

* To deactivate run: 
    > $ deactivate 

**Step 6: Install requirements in virtual environment**
> (env) $ pip install -r requirements.txt

**Step 7: Create secrets.json file in /etc/ directory (if using Ubuntu) or somewhere on your local machine**

To create a secret key to use run the following command via the command line and copy to the secret.json file: 
> (env) python -c "import secrets; print(secrets.token_urlsafe())"

_Example:_
```json
{
    "SECRET_KEY": "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
}
```

# How to Run 

Go to the folder where manage.py is located (mustangratings folder). 
**MAKE SURE YOU ARE IN A VIRTUAL ENVIRONMENT** 
and run: 
> $ python manage.py runserver 

on the command line and go to the link, should see website.

