import requests
import sqlite3

# Step 1: Send a GET request to the API and get the returned JSON data
response = requests.get("https://cat-fact.herokuapp.com/facts")
cat_facts = response.json()

# Step 2: Create an SQLite database to store the retrieved data
conn = sqlite3.connect('cat_facts.db')
c = conn.cursor()

# Step 3: Create a table to store cat facts
c.execute('''CREATE TABLE IF NOT EXISTS facts (
                id TEXT PRIMARY KEY,
                text TEXT
            )''')

# Step 4: Save cat facts retrieved from the API to the SQLite database
for fact in cat_facts:
    c.execute("INSERT OR IGNORE INTO facts (id, text) VALUES (?, ?)", (fact['_id'], fact['text']))

conn.commit()

# Step 5: View cat facts saved to the database in the terminal/powershell
c.execute("SELECT * FROM facts")
rows = c.fetchall()

for row in rows:
    print(f"ID: {row[0]}")
    print(f"Fact: {row[1]}")
    print()

conn.close()
