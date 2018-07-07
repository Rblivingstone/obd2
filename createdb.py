# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:38:03 2018

@author: Skippy
"""

import sqlite3

sql_conn = sqlite3.connect('c:\\users\\Skippy\\Desktop\\obd2.db')
c = sql_conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS observations (
                   id INTEGER PRIMARY KEY,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                   rpm REAL,
                   speed REAL,
                   throttle REAL,
                   relative_accel_pos REAL,
                   fuel_rate REAL,
                   fuel_level REAL,
                   ambiant_air_temp REAL,
                   barometric_pressure REAL
                  )""")
sql_conn.commit()