import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="time_tracker",
        user="postgres",
        password="50028082"
    )
