import urllib3

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']


def test_homepage():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/')
    assert 200  == r.status

def test_activities():                                                      #tests if page exists(Activities)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/Activities')
    assert 200  == r.status

def test_location():                                                        #tests if page exists(Locations)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/Locations')
    assert 200  == r.status

def test_nonpage():                                                         #tests if page doesn't exist
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.197.207.209:5000/About')
    assert 404  == r.status

def test_select():                                               #select test
    with app.app_context():
        cur= mysql.connection.cursor()
        num_of_records=cur.execute('SELECT * FROM Location')    #test made on the table that's not used for CRUD 
        mysql.connection.commit()
        cur.close()
        assert 12 == num_of_records                             #checks if the number of records in the database matches the number of entries expected to have in the table

def test_insert():                                              #insert test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Activity')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('INSERT INTO Activity (Name) VALUES ("test")')  #inserts at an autoincrement ID the value 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Activity')
        new_num_records=cur.fetchall()
        cur.close()
    recordb = len(num_of_records)                               #finds length of the records list before insertion
    new_id = num_of_records[recordb-1][0]+1                     #finds the id of the previous record and + 1 for autoincrement new record
    recorda = len(new_num_records) 
    assert (new_id ,'test') == new_num_records[recorda-1]  

