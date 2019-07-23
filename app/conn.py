# import psycopg2, os
# from flask import current_app, Flask
# from instance.config import Config, Testing

# app = Flask(__name__)
# url = "dbname='questioner_app' user='postgres' host='localhost' password='pop'"
# test_url ="dbname='questioner_test' user='postgres' host='localhost' password='pop'"

# def init_db():
#     """ Method to initialize the database """
#     with app.app_context():
#         conn = psycopg2.connect(url)
#         # url_db = Config.DATABASE_URL
#         # conn = psycopg2.connect(url_db)
#         cursor = conn.cursor()
#         sql = current_app.open_resource('tables.sql', mode='r')
#         cursor.execute(sql.read())
#         conn.commit()
#         return conn

# def connect_to(url):
#     conn = psycopg2.connect(url)
#     return conn

# def _init_db():
#     """ Initialize database for test """
#     with app.app_context():
#         conn = psycopg2.connect(test_url)
#         destroy_db()
#         cursor = conn.cursor()
#         sql_file = current_app.open_resource('tables.sql', mode='r')
#         cursor.execute(sql_file.read())
#         conn.commit()
#         return conn

# def destroy_db():
#     """ Destroy database for test """
#     with app.app_context():
#         conn = psycopg2.connect(test_url)
#         cursor = conn.cursor()
#         users = "DROP TABLE IF EXISTS users CASCADE"
#         tables = [users]
#         try:
#             for table in tables:
#                 cursor.execute(table)
#             conn.commit()
#         except Exception as e:
#             print("Database exception: %s" % e)
# """
# def tables():
# 	tb1 = """
		
# """
# 	queries = [tb1]
# 	return queries

# """