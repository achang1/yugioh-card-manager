# Yu-Gi-Oh Card Manager

## Install
python 3.7\
optional: Docker

## Running using a virtual environment
###### Windows
```
python -m venv myenv
myenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
###### Linux or OS X
```
python3 -m venv myenv
source myenv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running using Docker
```
docker-compose run web python3 Yugioh_Card_Manager/manage.py migrate
docker-compose build
docker-compose up
```

## Start app
```
cd Yugioh_Card_Manager
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Stop and remove the environment run
###### For venv
```
deactivate
```
###### For Docker
```
docker-compose down
```