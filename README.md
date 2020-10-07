# intern_test
To run locally, do the usual:-

Create a Python 3.8 virtualenv
Create a virtual environment
Install Django==3.0.5
Connect to database(database name==db_mr)
Run the following commands in cmd in the project folder
>>python manage.py collectstatic
>>python manage.py makemigrations
>>python manage.py migrate
Now run the server using 
>>python manage.py runserver
