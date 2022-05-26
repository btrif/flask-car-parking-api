
== Setup ==

= Setup virtual env =

pip install -r requirements.txt
then 
Activate your virtual environment

= Start Flask = 

set FLASK_APP=app

= Setup Database =
Open the Python console of the virtual env

from app import db
db.create_all()


= Run Flask =
flask run --port=7000




