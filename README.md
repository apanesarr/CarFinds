# CarFinds

Finds cars from multiple websites to ensure the lowest price. Currently the REST API is the only module that has been implemented. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install Django along with other libraries. Also probably a good idea to run a virtual environment. 

```
pip install django

pip install djangorestframework

pip install django-rest-auth

pip install django-allauth

pip install httpie

```
Since the db is not provided you must run migrate to create one. Also need a user to create an auth token. 

```
python manage.py migrate

python manage.py createsuperuser --email <SomeEmail> --username <SomeUsername>

python manage.py drf_create_token <UsernameFromBefore>

```
*Make sure to hold on to the auth token

## Deployment

To deploy run manage.py 

```
python manage.py runserver

```
## Usage
### Populate DB

Running populate_db command will add data to the db 

```
python manage.py populate_db

```

The webscraper has not been built yet but would follow the same command

### API 
Currently only endpoint is /api/v1/cars which returns the whole db with cars

Example call:

```
http http://127.0.0.1:8000/api/v1/cars/ "Authorization: Token <GeneratedAuthToken>"

```

Response:

```
[
    {
        "img": "https://www.topgear.com/sites/default/files/styles/fit_1960x1102/public/images/news-article/carousel/2019/01/6bb7a65acd31f46e9197dcc7edd94d02/supra_edit_2.jpg?itok=dD8aNfIH",
        "name": "Supra",
        "price": 60000,
        "vendor": "Toyota"
    }
]


```



