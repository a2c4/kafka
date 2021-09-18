from _global_imports import *
from _constants import *

con = sqlite3.connect('driving_data.db')
cur = con.cursor()

# Drop and create table
try:
    cur.execute("DROP TABLE driving_data")
except:
    pass

cur.execute("CREATE TABLE driving_data (Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, data text)")

def update_db(value):
    con = sqlite3.connect('driving_data.db')
    cur = con.cursor()
    # Insert a row of data
    cur.execute("INSERT INTO driving_data(data) VALUES ('" + str(value) + "')")
    # Save (commit) the changes
    con.commit()
    con.close()
con.close()

#update_db("afaf")
