
## ==  Setup ==

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
You can use the existing Database created and which comes with the app
or you can set up a new one as follows

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
```cmd
flask run --port=7000
or
python app.py
```



