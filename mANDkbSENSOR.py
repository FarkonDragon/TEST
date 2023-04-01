import mouse
import keyboard
import sqlite3
import time, random

# conn = sqlite3.connect('mouse_event.db')a
# cur.execute("""
# CREATE TABLE IF NOT EXISTS mouse(
# id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
# event TEXT);
# """)

def start():
    events = []
    mouse.hook(events.append)
    keyboard.wait("a")
    mouse.unhook(events.append)
    print(events)
    mouse.play(events)
    for i in range(len(events)):
        mevent=str(events[i])
        print(mevent)
#         cur.execute(f'INSERT INTO mouse (event)VALUES {mevent}')
#         conn.commit()
# 
#     cur.execute('SELECT * FROM mouse;')
#     all_results = cur.fetchall() 
#     print(all_results)
# time.sleep(3)
start()