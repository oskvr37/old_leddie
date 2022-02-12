from tinydb import TinyDB, Query
db = TinyDB('db.json')
table_latest = db.table('latest')
table_latest.insert((255, 255, 0))
