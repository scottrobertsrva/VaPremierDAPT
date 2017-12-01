# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from .models import *
import json
import os.path

@login_required
def index(request):
    claims = FluExpOnly.objects.filter(fiscal_year='2017').filter(
        member_id__in=[x.member_id for x in FluShotData.objects.filter(fiscal_year='2017')]
    ).aggregate(Sum('paid_amt'))
    
    context = {'claims':[str(claims['paid_amt__sum'])]}
    return render(request,'vpApp/index.html',context)

def fy(request,fy):
    response = "FY is %s"
    return HttpResponse(response % fy)

@login_required
def objectApi(request):
    yr = '2017'
    if request.is_ajax():
        yr = request.GET.get('fy')
    try:
        if not os.path.isfile('/var/www/VaPremier/dirty.json'):
            print "no json file"
            expenses = {}
            exp = FluRelatedExp.objects.all()
            maxWkAmt = 0
            for e in exp:
                if len(e.fips) == 1:
                    e.fips = "00" + e.fips
                if len(e.fips) == 2:
                    e.fips = "0" + e.fips
                #print "FIPS " + str(e.fips)
                start = e.claim_date - timedelta(days = e.claim_date.weekday())
                end = start + timedelta(days=6)
                if e.fiscal_year not in expenses:
                    expenses[e.fiscal_year] = {}
                    expenses[e.fiscal_year][start.strftime("%m/%d/%Y")] = {}
                    if e.paid_amt is not None:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = float(e.paid_amt)
                    else:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = 0
                elif start.strftime("%m/%d/%Y") not in expenses[e.fiscal_year]:
                    expenses[e.fiscal_year][start.strftime("%m/%d/%Y")] = {}
                    if e.paid_amt is not None:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = float(e.paid_amt)
                    else:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = 0
                elif e.fips not in expenses[e.fiscal_year][start.strftime("%m/%d/%Y")]:
                    if e.paid_amt is not None:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = float(e.paid_amt)
                    else:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] = 0
                else:
                    if e.paid_amt is not None:
                        expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] += float(e.paid_amt)
                        if expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips] > maxWkAmt:
                            maxWkAmt = expenses[e.fiscal_year][start.strftime("%m/%d/%Y")][e.fips]
            try:
                for year in expenses:
                    #print str(year)
                    for week in expenses[year]:
                        #print str(week)
                        count = 0
                        totalPaid = 0
                        for fips in expenses[year][week]:
                            totalPaid += expenses[year][week][fips]
                            #print str(fips)
                            count += 1
                        expenses[year][week]['totalPaid'] = totalPaid
                        expenses[year][week]['fipsCount'] = count
            except Exception as e:
                print str(e)
            
            for week in expenses['2017']:
                wkMax = 0
                for fips in expenses['2017'][week]:
                    #print expenses['2017'][week][fips]
                    if expenses['2017'][week][fips] > wkMax:
                        wkMax = expenses['2017'][week][fips]
                #print week + " MAX " + str(wkMax)
            

            with open('dirty.json','w') as outfile:
                json.dump(expenses,outfile)

            jsonObjs = json.dumps(expenses,default=lambda o:o.__dict__)
            data = {'data':jsonObjs}
            return JsonResponse(data)
        else:
            print "json file"
            with open('/var/www/VaPremier/dirty.json') as json_data:
                returnData = json.load(json_data)
            #print str(returnData)
            json_data.close()
            return JsonResponse(returnData)
    except Exception as e:
        print str(e)

