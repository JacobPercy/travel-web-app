# Travel-App (Tapp)
> Saving tourists on a day to day basis!


## Developing
Run the following commands:

> [!TIP]
> If you're on windows, replace ``python3`` with ``python``

First you will need to install ``python`` 3.11 and ``pipenv``.
You can look at their respective documentation to find out
which to install.

Then run the following script:
```shell
git clone https://github.com/JacobPercy/travel-web-app.git tapp
cd tapp
pipenv install
python3 manage.py migrate
python3 manage.py runserver
```
Then head over to http://localhost:8000/ to see the app running!
