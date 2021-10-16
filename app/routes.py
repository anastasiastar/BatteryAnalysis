import sqlalchemy
from app import db,app
from app.models import Test1
import pandas as p
#import matplotlib.pyplot as plt
#import pylab 
#file_location = "C:\\Users\\anast\\Desktop\\visual studios\\randomData.xlsx"
#var = pd.read_excel('C:\\Users\\anast\\Desktop\\visual studios\\randomData.xlsx')
voltage1 =p.read_excel('C:\\Users\\anast\\Downloads\\wykht8y7tg-1\\Panasonic 18650PF Data\\-20degC\\n20degVoltage.xls')
#time1    =p.read_excel('C:\\Users\\anast\\Downloads\\wykht8y7tg-1\\Panasonic 18650PF Data\\-20degC\\n20degTime.xls')
#current =p.read_excel('C:\\Users\\anast\\Downloads\\wykht8y7tg-1\\Panasonic 18650PF Data\\-20degC\\n20degCurrent.xls')
#power =p.read_excel('C:\\Users\\anast\\Downloads\\wykht8y7tg-1\\Panasonic 18650PF Data\\-20degC\\n20degPower.xls')
#Ah =p.read_excel('C:\\Users\\anast\\Downloads\\wykht8y7tg-1\\Panasonic 18650PF Data\\-20degC\\n20degAh.xls')
#engine=sqlalchemy('postgresql://username:password@databasehost:port/databasename')
voltage2=voltage1.to_sq1()
@app.route('/')
@app.route('/index')
def index():

    u = Test1(temperature=25.3, voltage=voltage2)
    #u = time
    db.session.add(u)
    db.session.commit()
    return "Hello, World!"