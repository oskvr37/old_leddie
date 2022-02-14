from tinydb import TinyDB, Query


class Table:
    def __init__(self, db: TinyDB, name: str, limit=10) -> None:
        self.name = name
        self.db = db
        self.table = self.db.table(name)
        self.documents = self.table.all()
        print(f'table {name} has got {len(self.documents)} documents')
        print(self.documents)

    def insert(self, document):
        documents = self.table.all()

    def delete_oldest(self):
        documents = self.table.all()
        oldest = documents[0]
        print(oldest)
        Color = Query()
        self.db.remove(Color.hex == oldest['hex'])
        s = self.db.search(Color.hex == '#213769')
        print(s)

class Database:
    def __init__(self) -> None:
        self.db = TinyDB('db.json')
        self.latest = Table(self.db, 'latest')
        self.favorites = Table(self.db, 'favorites')


d = Database()
# d.latest.table.insert({'hex': '#213768'})
# d.latest.table.insert({'hex': '#213769'})
# d.latest.table.insert({'hex': '#213770'})
d.latest.table.insert({'hex': '#213778'})
d.latest.delete_oldest()
