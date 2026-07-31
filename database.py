import sqlite3

DB = "mirza.db"


def connect():
    return sqlite3.connect(DB)


def create_db():
    con = connect()
    cur = con.cursor()

    # کاربران
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # سرویس‌ها
    cur.execute("""
    CREATE TABLE IF NOT EXISTS services(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        config TEXT,
        volume TEXT,
        days INTEGER,
        status TEXT DEFAULT 'active'
    )
    """)

    # سفارش‌ها
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        status TEXT DEFAULT 'pending'
    )
    """)

    con.commit()
    con.close()


def add_user(user_id, username):

    con = connect()
    cur = con.cursor()

    cur.execute(
        """
        INSERT OR IGNORE INTO users(id, username)
        VALUES(?,?)
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

    result = cur.fetchone()[0]

    con.close()

    return result


def add_service(user_id, name, config, volume, days):

    con = connect()
    cur = con.cursor()

    cur.execute(
        """
        INSERT INTO services
        (user_id,name,config,volume,days)
        VALUES(?,?,?,?,?)
        """,
        (user_id,name,config,volume,days)
    )

    con.commit()
    con.close()


def get_user_services(user_id):

    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM services WHERE user_id=?",
        (user_id,)
    )

    data = cur.fetchall()

    con.close()

    return data
