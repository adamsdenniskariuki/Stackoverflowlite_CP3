from db.dbconfig import open_connection, close_connection

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
    """ Create tables """
    conn = open_connection()
    cur = conn.cursor()

    for query in QUERIES:
        cur.execute(query)

    close_connection(conn)


def drop_tables():
    """ Delete tables after tests """

    queries = [
        'DROP table users CASCADE',
        'DROP table questions CASCADE',
        'DROP table answers CASCADE',
        'DROP table blacklist CASCADE'
    ]

    conn = open_connection()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)

    cur.close()
    conn.commit()



