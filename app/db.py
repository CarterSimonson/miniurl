import sqlite3

# SQLite datatypes:
# NULL, INTEGER, REAL, TEXT, BLOB

DB_PATH = '/etc/url-db/miniurl.sqlite'

def setup():
  con = sqlite3.connect(DB_PATH)
  cur = con.cursor()

  cur.execute('''
    CREATE TABLE IF NOT EXISTS shortened (
      id TEXT CONSTRAINT shortened_pk PRIMARY KEY,
      url TEXT
    )
  ''')

  con.commit()
  con.close()

setup()

# DB operations
def get_shortened(id):
  con = sqlite3.connect(DB_PATH)
  cur = con.cursor()

  cur.execute("SELECT * FROM shortened WHERE id = (?)", (id,))
  item = cur.fetchone()

  con.commit()
  con.close()

  return item

def add_shortened(id, url):
  con = sqlite3.connect(DB_PATH)
  cur = con.cursor()

  cur.execute("INSERT INTO shortened VALUES (?,?)", (id, url))

  con.commit()
  con.close()
