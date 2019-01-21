import pymysql #pip install pymysql

conn = pymysql.connect(host="localhost",user="root",password="",db="iqbol")

q = conn.cursor()