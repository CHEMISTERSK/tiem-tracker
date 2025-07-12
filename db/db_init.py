from db.db import get_connection

def connection_check():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        Select 1
    ''',)

    result = cur.fetchall()  
    conn.close()
    if result:
        return True
    else:
        return False

def save_task(task, time, date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO time_log (task, time, date)
        VALUES (%s, %s, %s)
    ''', (task, time, date))
    conn.commit()
    conn.close()
    print("Task saved successfully")