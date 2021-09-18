from _global_imports import *
from _constants import *

con = sqlite3.connect('driving_data.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM driving_data ORDER BY Timestamp'):
    print((row[0],json.loads(bytes.fromhex(row[1]))))
