"""Client depends only on factory operations."""
class SqliteConnection:
    def execute(self): return "sqlite query"
class SqliteFactory:
    def connection(self): return SqliteConnection()

def run_report(database_factory):
    return database_factory.connection().execute()

print(run_report(SqliteFactory()))
