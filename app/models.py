from app import db

class Test1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature= db.Column(db.Float)
    voltage = db.Column(db.Float)
 

    def __repr__(self):
        return '<Test1 {}>'.format(self.voltage)