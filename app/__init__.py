from flask import Flask



from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///battery.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



#app.run(debug=True)

from app import routes, models