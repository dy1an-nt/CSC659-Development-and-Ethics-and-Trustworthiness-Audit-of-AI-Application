import sqlite3

def get_user_secure(conn, user_id):
    query = "SELECT * FROM users WHERE id = ?"
    cursor = conn.execute(query, (user_id,))
    return cursor.fetchall()

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.execute("INSERT INTO users VALUES (2, 'Bob')")
conn.commit()

print("Safe query result:", get_user_secure(conn, 1))

malicious_input = "1 OR 1=1"
result = get_user_secure(conn, malicious_input)
print("Attempted injection result:", result)

conn.close()
