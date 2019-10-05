#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:10:17 2019

@author: tata
"""
import sqlite3

connection = sqlite3.connect("inspections and violations.db")
connection1 = sqlite3.connect("Previous Violations.db")

cursor = connection.cursor()
cursor1 = connection1.cursor()

## use sql command to get data
commond  = """
SELECT inspections.facility_name,inspections.facility_address,inspections.facility_zip,inspections.facility_city FROM inspections,violations WHERE inspections.serial_number = violations.serial_number
GROUP BY inspections.facility_name
ORDER BY facility_name
"""

comm=cursor.execute(commond)
array = comm.fetchall()

## create data and show the data type
sql = """
create table if not exists PreviousViolations(
        name VARCHAR(30),
        address VARCHAR(30),
        zip_code INTEGER(15),
        city VARCHAR(20)
        
)"""
cursor1.execute(sql);
cursor1.fetchall()

## insert the data
for i in array:
    sql_comm ="""
    INSERT INTO PreviousViolations values(?,?,?,?)
    """
    cursor1.execute(sql_comm,i)


connection1.commit()
connection1.close()
connection.close()


