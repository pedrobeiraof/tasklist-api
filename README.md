# tasklist-api

Task List API
===================================

Task List project based on gitlab board.

Developed using [Django Rest](https://www.django-rest-framework.org).

https://pedrobeiraof-tasklist.herokuapp.com

## Getting Start
### clone projetct

* first download the project from git, you can do with this command
`git clone https://github.com/pedrobeiraof/tasklist-api.git`

### create virtualenv 

* assuming you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) and python3 run the commands
```
mkvirtualenv tasklist -p python3
workon tasklist
```

### Configure env variables

* To speed up the testing process the env file will temporarily be configured on the project

### download project dependencies

* Install all dependencies using pip
```
cd tasklist-api/
pip install -r requirements.txt 
```

### Run Project

* Run django project manager
```
python manage.py runserver
```
