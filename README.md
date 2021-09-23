# vindecode
VIN (Vehicle Identification Number) decoding api service

    The main project app - main

To run the project locally:
*   create virtual environment for python version > 3.8 
    
    `` python -m venv env ``
*   install all required libraries 

    `` pip install -r requirements.txt ``
*   setup postgres (create database, create .env and paste configuration below)
> SECRET_KEY = ''

> NAME = ''

> USER = ''

> PASSWORD = ''

> HOST = localhost

> PORT = 5432

*   migrate all db tables 
    
    ``python manage.py migrate / python manage.py migrate (main)``
*   run project server 

    ``python manage.py runserver``
*   open localhost with vin as endpoint (e.i 127.0.0.1:8000/2C4RC1DG3HR711964)

Test is available in main/test.py and coverage report saved in project root dir (coverage_report.txt)


