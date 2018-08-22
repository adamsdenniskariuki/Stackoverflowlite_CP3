from dbconfig import open_connection, close_connection, open_test_connection

QUERIES = [
  """
  CREATE TABLE IF NOT EXISTS users(
          user_id SERIAL PRIMARY KEY NOT NULL,
          username VARCHAR NOT NULL,
          email VARCHAR NOT NULL,
          password VARCHAR NOT NULL,
          questions VARCHAR[]

          )
  """,

  """
  CREATE TABLE IF NOT EXISTS questions(
          question_id SERIAL PRIMARY KEY NOT NULL,
          question_desc VARCHAR NOT NULL,
          user_id INT REFERENCES users(user_id),
          answers VARCHAR[]
          )
  """,

  """
  CREATE TABLE IF NOT EXISTS answers(
          id SERIAL PRIMARY KEY NOT NULL,
          answer_desc VARCHAR NOT NULL,
          question_id INT REFERENCES questions(question_id),
          user_id INT REFERENCES users(user_id)
        
          )
  """,

  """
    CREATE TABLE IF NOT EXISTS blacklist(
        token_id SERIAL PRIMARY KEY NOT NULL,
        token VARCHAR NOT NULL)
  """

]


def create_tables():
    """ Create main app tables """
    conn = open_connection()
    cur = conn.cursor()

    for query in QUERIES:
        cur.execute(query)

    close_connection(conn)


def create_test_tables():
    """ Create tables for tests """
    conn = open_test_connection()
    cur = conn.cursor()

    for query in QUERIES:
        cur.execute(query)

    cur.close()
    close_connection(conn)


def drop_test_tables():
    """ Delete test database after running tests """

    queries = [
        'DROP table answers',
        'DROP table questions',
        'DROP table users',
        'DROP table blacklist'
    ]

    conn = open_test_connection()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)
    cur.close()
    close_connection(conn)


