import xlrd
from xlrd import open_workbook
import pymysql
from trash import trash  # Stored password here not in github file
import datetime
import os
from re import sub
from decimal import Decimal

hostname='localhost'
username='root'
password=trash
database='Test'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
curs = conn.cursor()

wb = open_workbook('FluData_VCU_MDA_Corrected.xlsx')
sheets = wb.sheets()
for s in sheets:
    if s.name == 'FLU_EXPENSES_ONLY':
        fluOnly = s
    if s.name == 'FLU_SHOT_DATA':
        fluShot = s
    if s.name == 'FLU_RELATED_EXPENSES':
        fluRelated = s

sql = ""

if False:
    for row in range(1,fluOnly.nrows):
            clNum = fluOnly.cell(row,0).value
            memId = fluOnly.cell(row,1).value
            clmDt = fluOnly.cell(row,2).value
            fscYr = fluOnly.cell(row,3).value
            mnth = fluOnly.cell(row,4).value
            pdAmt = fluOnly.cell(row,5).value
            lblCod = fluOnly.cell(row,6).value
            lblName = fluOnly.cell(row,7).value
            type = fluOnly.cell(row,8).value 
            age = fluOnly.cell(row,9).value
            plan = fluOnly.cell(row,10).value
            sex = fluOnly.cell(row,11).value
            region = fluOnly.cell(row,12).value
            city = fluOnly.cell(row,13).value
            fips = fluOnly.cell(row,14).value
            place = fluOnly.cell(row,15).value
            
            pdAmt = Decimal(pdAmt)
            
            if fscYr is None:
                fscYr = 0
            if age is None:
                age = -1
            if fips =="NULL":
                fips = -1
            
            mnth = xlrd.xldate_as_tuple(mnth,wb.datemode)
            clmDt = xlrd.xldate_as_tuple(clmDt,wb.datemode)
            mnth = datetime.datetime(year=mnth[0],month=mnth[1],day=mnth[2])
            mnth = mnth.strftime("%Y-%m-%d")
            clmDt = datetime.datetime(year=clmDt[0],month=clmDt[1],day=clmDt[2])
            clmDt = clmDt.strftime("%Y-%m-%d")
            try:
                sql += "insert into flu_exp_only "
                sql += "(claim_num,member_id,claim_date,fiscal_year,month,paid_amt,"
                sql += "l_d_code,l_d_desc,type,age,plan,sex,region,city_county,fips,place)"
                sql += " values ("
                sql += "'" + str(clNum) + "','" + str(memId) + "','" + str(clmDt) + "','" + str(int(fscYr)) + "','" + str(mnth) + "'," + str(pdAmt) + ",'" + str(lblCod) + "',"
                sql += "'" + str(lblName) + "','" + str(type) + "','" + str(int(age)) + "','" + str(plan) + "','" + str(sex) + "','" + str(region) + "','" + str(city) + "','" + str(int(fips)) + "','" + str(place) + "');"
            except Exception as e:
                print str(fscYr) + " " + str(age) + " "  + str(fips)
                print str(e)
                print str(sql)
            print row
            #try:
            
            if row % 1000 == 0:
                #curs.execute(sql)
                #conn.commit()
                sql = ""
            #except Exception as e:
            #print sql
    #curs.execute(sql)
    
if False:
    sql = ""
    for row in range(1,fluShot.nrows):
            clNum = fluShot.cell(row,0).value
            memId = fluShot.cell(row,1).value
            clmDt = fluShot.cell(row,2).value
            fscYr = fluShot.cell(row,3).value
            mnth = fluShot.cell(row,4).value
            pdAmt = fluShot.cell(row,5).value
            lblCod = fluShot.cell(row,6).value
            lblName = fluShot.cell(row,7).value
            type = fluShot.cell(row,8).value 
            age = fluShot.cell(row,9).value
            plan = fluShot.cell(row,10).value
            sex = fluShot.cell(row,11).value
            
            mnth = xlrd.xldate_as_tuple(mnth,wb.datemode)
            clmDt = xlrd.xldate_as_tuple(clmDt,wb.datemode)
            mnth = datetime.datetime(year=mnth[0],month=mnth[1],day=mnth[2])
            mnth = mnth.strftime("%Y-%m-%d")
            clmDt = datetime.datetime(year=clmDt[0],month=clmDt[1],day=clmDt[2])
            clmDt = clmDt.strftime("%Y-%m-%d")
            
            region = fluShot.cell(row,12).value
            city = fluShot.cell(row,13).value
            fips = fluShot.cell(row,14).value
            place = fluShot.cell(row,15).value
            
            pdAmt = Decimal(pdAmt)
            
            if fscYr is None:
                fscYr = 0
            if age is None:
                age = -1
            if fips =="NULL":
                fips = -1
            
            try:
                sql += "insert into flu_shot_data "
                sql += "(claim_num,member_id,claim_date,fiscal_year,month,paid_amt,"
                sql += "l_d_code,l_d_desc,type,age,plan,sex,region,city_county,fips,place)"
                sql += " values ("
                sql += "'" + str(clNum) + "','" + str(memId) + "','" + str(clmDt) + "','" + str(int(fscYr)) + "','" + str(mnth) + "'," + str(pdAmt) + ",'" + str(lblCod) + "',"
                sql += "'" + str(lblName) + "','" + str(type) + "','" + str(int(age)) + "','" + str(plan) + "','" + str(sex) + "','" + str(region) + "','" + str(city) + "','" + str(int(fips)) + "','" + str(place) + "');"
            except Exception as e:
                print str(fscYr) + " " + str(age) + " "  + str(fips)
                print str(e)
                print str(sql)
            print row
            #try:
            
            if row % 1000 == 0:
                curs.execute(sql)
                conn.commit()
                sql = ""
            #except Exception as e:
            #print sql
    curs.execute(sql)
    
if True:
    sql = ""
    for row in range(1,fluRelated.nrows):
            clNum = fluRelated.cell(row,0).value
            memId = fluRelated.cell(row,1).value
            clmDt = fluRelated.cell(row,2).value
            fscYr = fluRelated.cell(row,3).value
            mnth = fluRelated.cell(row,4).value
            pdAmt = fluRelated.cell(row,5).value
            
            cat = fluRelated.cell(row,6).value
            cat2 = fluRelated.cell(row,7).value
            cat3 = fluRelated.cell(row,8).value
            
            age = fluRelated.cell(row,9).value
            plan = fluRelated.cell(row,10).value
            sex = fluRelated.cell(row,11).value
            
            mnth = xlrd.xldate_as_tuple(mnth,wb.datemode)
            clmDt = xlrd.xldate_as_tuple(clmDt,wb.datemode)
            mnth = datetime.datetime(year=mnth[0],month=mnth[1],day=mnth[2])
            mnth = mnth.strftime("%Y-%m-%d")
            clmDt = datetime.datetime(year=clmDt[0],month=clmDt[1],day=clmDt[2])
            clmDt = clmDt.strftime("%Y-%m-%d")
            
            region = fluRelated.cell(row,12).value
            city = fluRelated.cell(row,13).value
            fips = fluRelated.cell(row,14).value
            place = fluRelated.cell(row,15).value
            
            pdAmt = Decimal(pdAmt)
            
            if fscYr is None:
                fscYr = 0
            if age is None:
                age = -1
            if fips =="NULL":
                fips = -1
            
            try:
                sql += "insert into flu_related_exp "
                sql += "(claim_num,member_id,claim_date,fiscal_year,month,paid_amt,"
                sql += "cat,cat2,cat3,age,plan,sex,region,city_county,fips,place)"
                sql += " values ("
                sql += "'" + str(clNum) + "','" + str(memId) + "','" + str(clmDt) + "','" + str(int(fscYr)) + "','" + str(mnth) + "'," + str(pdAmt) + ",'" + str(cat) + "',"
                sql += "'" + str(cat2) + "','" + str(cat3) + "','" + str(int(age)) + "','" + str(plan) + "','" + str(sex) + "','" + str(region) + "','" + str(city) + "','" + str(int(fips)) + "','" + str(place) + "');"
            except Exception as e:
                print str(fscYr) + " " + str(age) + " "  + str(fips)
                print str(e)
                print str(sql)
            print row
            #try:
            
            if row % 1000 == 0:
                curs.execute(sql)
                conn.commit()
                sql = ""
            #except Exception as e:
            #print sql
    curs.execute(sql)

conn.commit()
curs.close()
conn.close()






















