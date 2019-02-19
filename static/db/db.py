import sqlite3
from os.path import exists, isfile

def get_db():
	# db_path = 'file:static/db/to_do_list.db'
	db_path = 'static/db/to_do_list.db'
	return db_path

def check_db(db_path):
    if isfile(db_path):
        return db_path
    else:
        return False

def connect_db(db_path):
	# if check_db(db_path):
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		return conn, c
	except:
		raise
	else:
	# 	print('Error - wrong path')
		return False

def create_db(db_path, connection, cursor):
    if get_db():
        cursor.execute('DROP TABLE IF EXISTS to_do_list')
        cursor.execute('CREATE TABLE to_do_list(id REAL, title TEXT, description TEXT, status TEXT, priority TEXT, start_date TEXT, end_date TEXT)')
        connection.commit()
    else:
        raise('Unable to create table')

if __name__ == '__main__':
	db_path = get_db()
	conn, c = connect_db(db_path)
	create_db(db_path, conn, c)
	c.close()
	conn.close()
