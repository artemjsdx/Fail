import sqlite3

class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, create_table_sql):
        """Create a table from the create_table_sql statement."""
        self.cursor.execute(create_table_sql)

    def insert_record(self, table, columns, values):
        """Insert a new record into the specified table."""
        placeholders = ', '.join(['?' for _ in values])
        sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(sql, values)

    def fetch_all(self, table):
        """Fetch all records from the specified table."""
        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.commit()
        self.connection.close()