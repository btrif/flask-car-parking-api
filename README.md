
#  Setup

### Clone project from Github on your local machine 
```bash
git clone https://github.com/btrif/oracle-car-parking.git
```
### Setup virtual env
#### Create new environment
Go to project folder and create the virtual env :
```bash
python -m venv .parking_venv
```
#### Activate virtual environment
 
```bash
.parking_venv\Scripts\activate.bat           (Windows)
./.parking_venv/bin/activate                 (Linux, Mac)
```
Install the Python libraries inside virtual environment :
```bash
(.parking_venv) D:\workspace\oracle-car-parking> pip install -r requirements.txt
```



##  Setup Flask 

NOTE : The Flask API is using a simple SQLite Toolkit with DB, 
SQLAlchemy as ORM.

### Set Environment Variables
```bash
(.parking_venv) D:\workspace\oracle-car-parking>set FLASK_APP=app
```
###  Setup Database
You can use the existing Database created and which comes with the app.
Or you can set up a new empty one as follows 
( Please note that it must be done before application was started):


Open the Python console of the virtual env start a python session

```bash
(.parking_venv) D:\workspace\oracle-car-parking>python
Python 3.9.6 (tags/v3.9.6:db3ff76
```
```python
>>> from app import db
>>> db.create_all()
```

###  Start Flask
```bash
flask run --port=7000
or
python app.py
```

When you access in web browser:
```http://localhost:port```
should open the index of the app with a help to use the API.

### Settings
Parking Settings are hold within the Settings class
where you can change parking capacity and also the daily or hourly tariffs.

# Docker alternative
If you have installed Docker locally on you machine you can do the following
in the root folder of the application :

```bash
D:\workspace\oracle-car-parking>docker build -t oracle-car-parking:latest
D:\workspace\oracle-car-parking>docker run -p 7000:7000 oracle-car-parking-flask
```

and you can already use in the same way the host machine web browser  Application API.
You should get something like this :
```bash

* Serving Flask app 'settings' (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on all addresses (0.0.0.0)
  WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://127.0.0.1:7000
* Running on http://172.17.0.2:7000 (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 804-900-018
  172.17.0.1 - - [26/May/2022 14:50:27] "GET /available_places HTTP/1.1" 200 -
  172.17.0.1 - - [26/May/2022 14:50:27] "GET /favicon.ico HTTP/1.1" 404 -
  172.17.0.1 - - [26/May/2022 14:52:46] "GET / HTTP/1.1" 200 -
  172.17.0.1 - - [26/May/2022 14:52:50] "GET /cars HTTP/1.1" 200 -
  172.17.0.1 - - [26/May/2022 14:53:01] "GET /delete/13 HTTP/1.1" 404 -
  172.17.0.1 - - [26/May/2022 14:53:33] "GET /remove/13 HTTP/1.1" 200 -```






