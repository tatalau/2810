# 2810
This report will contain four tasks which uses python to achieve interaction with python code, excel, numpy and matplotlib. <br>
The task1 is to create python script to achieve the function of getting data from excel document and insert data to database. <br>
The task2 is to use sql’s statement to query the database. <br>
The task3 is to use sql’s statement to select violation data and put the data into a new excel document. <br>
The task 4 is to write the report documentation and do the summary. <br>

## function: <br>
1.	Connection = sqlite3.conncet connect the database <br>
2.	Openpyxl.load_workbook(“inspection.xlsx”) open the excel files <br>
3.	Openpyxl.load_workbook(“violation.xlsx”) open the excel files <br>
4.	Cursor = conncetion.cursor() <br>
5.	Sqlcommand=”””create table if not exists inspections()””” to create table named inspection <br>
6.	Sqlcommand1=”””create table if not exists violations()””” to create table named violations <br>
7.	For i in range <br>
8.	From openpyxl import workbook <br>
9.	Import sqlite3 <br>
