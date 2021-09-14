# vindecode
VIN (Vehicle Identification Number) decoding api service

The main progect app - main

To run the project locally:
*   create virtual environment (<i>python -m venv env</i>) for python version > 3.8 
*   install all required libraries (<i>pip install -r requirements.txt</i>)
*   setup postgres (create database, create .env and paste configuration below)
> SECRET_KEY = ''

> NAME = ''

> USER = ''

> PASSWORD = ''

> HOST = localhost

> PORT = 5432

*   migrate all db tables (<i>python manage.py migrate / python manage.py migrate (main)</i>)
*   run project server (<i>python manage.py runserver</i>)
*   open localhost with vin as endpoint (e.i 127.0.0.1:8000/2C4RC1DG3HR711964)

Test is available in main/test.py and coverage report saved in project root dir (coverage_report.txt)


