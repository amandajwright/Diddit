#import sqlite3
#from os.path import exists, isfile
#import re
#
#def get_db():
#	# db_path = 'file:static/db/to_do_list.db'
#	db_path = 'static/db/to_do_list.db'
#	return db_path
#
#def check_db(db_path):
#    if isfile(db_path):
#        return db_path
#    else:
#        return False
#
#def connect_db(db_path):
#	# if check_db(db_path):
#	try:
#		conn = sqlite3.connect(db_path)
#		c = conn.cursor()
#		return conn, c
#	except:
#		raise
#	else:
#	# 	print('Error - wrong path')
#		return False
#
#def create_db(db_path, connection, cursor):
#    if get_db():
#        cursor.execute('DROP TABLE IF EXISTS to_do_list')
#        cursor.execute('CREATE TABLE to_do_list(id REAL, title TEXT, description TEXT, status TEXT, priority TEXT, start_date TEXT, end_date TEXT)')
#        connection.commit()
#    else:
#        raise('Unable to create table')
#
#def list_columns_db():
#	db_path = get_db()
#	if check_db(db_path):
#		try:
#			conn, c = connect_db(db_path)
#			# db_path = 
#			# query = 'FROM {} SELECT *'.format(db_path)
#			# cursor.execute(query)
#			c.execute('PRAGMA table_info(to_do_list);')
#			data = c.fetchall()
#			list_columns = [item[1] for item in data]
#			close_db()
#			return list_columns
#		except Exception as e:
#			print(e)
#
#def list_all_db():
#	db_path = get_db()
#	if check_db(db_path):
#		try:
#			conn, c = connect_db(db_path)
#			# db_path = 
#			# query = 'FROM {} SELECT *'.format(db_path)
#			# cursor.execute(query)
#			c.execute('SELECT * FROM to_do_list')
#			list_all = c.fetchall()
#			close_db()
#			return list_all
#		except Exception as e:
#			print(e)
#		
#def close_db():
#	c.close()
#	conn.close()
#
#if __name__ == '__main__':
#	db_path = get_db()
#	conn, c = connect_db(db_path)
#	create_db(db_path, conn, c)
#	c.close()
#	conn.close()
