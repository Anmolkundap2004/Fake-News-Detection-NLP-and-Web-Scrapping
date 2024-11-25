import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("fake_news.db", check_same_thread=False)
cursor = conn.cursor()

# Create table for storing results
cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_text TEXT,
        result TEXT,
        articles TEXT
    )
''')
conn.commit()

def save_result(user_text, result, articles):
    """
    Saves the result in the database.
    """
    articles_str = "|".join(articles)
    cursor.execute("INSERT INTO results (user_text, result, articles) VALUES (?, ?, ?)", 
                   (user_text, result, articles_str))
    conn.commit()

def fetch_results():
    """
    Fetches all saved results from the database.
    """
    cursor.execute("SELECT * FROM results")
    return cursor.fetchall()
