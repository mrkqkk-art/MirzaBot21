import sqlite3

DB = "users.db"


def connect():
    return sqlite3.connect(DB)


def create_db():
    con = connect()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        status TEXT DEFAULT 'active'
    )
    """)

    con.commit()
    con.close()


def add_user(user_id, username):

    con = connect()
    cur = con.cursor()

    cur.execute(
        """
        INSERT OR IGNORE INTO users
        (id, username)
        VALUES (?, ?)
        """,
        (user_id, username)
    )

    con.commit()
    con.close()


def users_count():

    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cur.fetchone()[0]

    con.close()

    return count


def get_users():

    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT id FROM users WHERE status='active'"
    )

    users = cur.fetchall()

    con.close()

    return users


def block_user(user_id):

    con = connect()
    cur = con.cursor()

    cur.execute(
        "UPDATE users SET status='blocked' WHERE id=?",
        (user_id,)
    )

    con.commit()
    con.close()
