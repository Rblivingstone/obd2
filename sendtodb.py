# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 08:47:30 2018

@author: Skippy
"""

import obd
import sqlite3

sql_conn = sqlite3.connect('c:\\users\\Skippy\\Desktop\\obd2.db')
c = sql_conn.cursor()
obd_conn = obd.Async()


obd_conn.watch(obd.commands.RPM)
obd_conn.watch(obd.commands.SPEED)
obd_conn.watch(obd.commands.THROTTLE_POS)
obd_conn.watch(obd.commands.RELATIVE_ACCEL_POS)
obd_conn.watch(obd.commands.FUEL_RATE)
obd_conn.watch(obd.commands.FUEL_LEVEL)
obd_conn.watch(obd.commands.AMBIANT_AIR_TEMP)
obd_conn.watch(obd.commands.BAROMETRIC_PRESSURE)

obd_conn.start()
c.execute("""INSERT INTO observations (
                                       rpm,
                                       speed,
                                       throttle,
                                       relative_accel_pos,
                                       fuel_rate,
                                       fuel_level,
                                       ambiant_air_temp
                                      )
                         VALUES(
                                {0},
                                {1},
                                {2},
                                {3},
                                {4},
                                {5},
                                {6}
                                )""".format(obd_conn.query(obd.commands.RPM),
                                obd_conn.query(obd.commands.SPEED),
                                obd_conn.query(obd.commands.THROTTLE_POS),
                                obd_conn.query(obd.commands.RELATIVE_ACCEL_POS),
                                obd_conn.query(obd.commands.FUEL_RATE),
                                obd_conn.query(obd.commands.FUEL_LEVEL),
                                #obd_conn.query(obd.commands.AMBIANT_AIR_TEMP),
                                #obd_conn.query(obd.commands.BAROMETRIC_PRESSURE)
                                            ))
sql_conn.commit()
