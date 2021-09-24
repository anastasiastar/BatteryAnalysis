from app import db,app
from app.models import Test1

@app.route('/')
@app.route('/index')
def index():

    u = Test1(temperature=25.7, voltage=17)
    db.session.add(u)
    db.session.commit()
    return "Hello, World!"