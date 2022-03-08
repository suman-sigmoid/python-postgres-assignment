import psycopg2
import xlsxwriter

try:
 connection = psycopg2.connect(host="localhost", database="python-sql-assignment-suman", user="postgres", password="@SumanNehra", port='5432')
 cursor = connection.cursor()
 query1 = "select t1.empno,t1.ename, t2.ename from emp t1 inner join emp as t2 on t1.mgr=t2.empno;"

 cursor.execute(query1)
 data = cursor.fetchall()

 workbook_Q1 = xlsxwriter.Workbook('task1.xlsx')
 worksheet = workbook_Q1.add_worksheet()
 worksheet.write('A1', 'Employee Number')
 worksheet.write('B1', 'Employee Name')
 worksheet.write('C1', 'Manager Name')
 row = 1
 col = 0
 for num, name, mgr in (data):
  worksheet.write(row, col, num)
  worksheet.write(row, col + 1, name)
  worksheet.write(row, col + 2, mgr)
 row += 1

 query2 = "select emp.empno, emp.ename,dept.dname, CASE WHEN enddate IS NOT NULL then EXTRACT(year FROM age(" \
 "enddate,startdate))*12 + EXTRACT(month FROM age(enddate,startdate)) else EXTRACT(year FROM age(" \
 "'2022-03-04',startdate))*12 + EXTRACT(month FROM age('2022-03-04',startdate)) END *emp.sal " \
 "Compensation,CASE WHEN enddate IS NOT NULL then EXTRACT(year FROM age(enddate,startdate))*12 + EXTRACT(" \
 "month FROM age(enddate,startdate)) else EXTRACT(year FROM age('2022-03-04',startdate))*12 + EXTRACT(" \
 "month FROM age('2022-03-04',startdate)) END Total_Months from emp join jobhist on " \
 "emp.empno=jobhist.empno join dept on dept.deptno=jobhist.deptno; "

 cursor.execute(query2)
 data = cursor.fetchall()
 for i in data:
  print(i)
 workbook_Q2 = xlsxwriter.Workbook('task_2.xlsx')
 worksheet = workbook_Q2.add_worksheet()
 worksheet.write('A1', 'Employee Number')
 worksheet.write('B1', 'Employee Name')
 worksheet.write('C1', 'Department Name')
 worksheet.write('D1', 'Compensation')
 worksheet.write('E1', 'Total Months')

 row = 1
 col = 0
 for num, name, dname, comp, month in (data):
  worksheet.write(row, col, num)
  worksheet.write(row, col + 1, name)
  worksheet.write(row, col + 2, dname)
  worksheet.write(row, col + 3, comp)
  worksheet.write(row, col + 4, month)
 row += 1
except:
    print("errorr in connection")
finally:
 connection.close()
 workbook_Q1.close()
