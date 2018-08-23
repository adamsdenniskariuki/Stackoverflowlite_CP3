import psycopg2


def connect_db():
  '''Connect to database'''

  db_details = "dbname='stackoverflowlite' user='postgres' host='localhost' password='password'"
  try:
      return psycopg2.connect(db_details)
  except:
      print ("Unable to establish connection to database")


def open_connection():
    """ Open connection to run queries """
    conn = connect_db()
    print(conn)
    return conn


def close_connection(conn):
    """ Close connection after queries """
    conn.commit()
    conn.close()






