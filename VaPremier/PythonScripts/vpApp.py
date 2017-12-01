import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import math

# Simple function to show basic summary statistics and inspect frequencies of unique values for the column
def audit_column(data, column_name):
    pd.options.display.float_format = '{:20,.2f}'.format
    pd.options.display.max_rows = None
    print "--------- SUMMARY FOR: " + str(data.name) + " " + column_name + " ----------------"
    print data[column_name].describe()
    #print data[column_name].value_counts()
    print "--------- END SUMMARY -----------------------------------------------------------------"

def assignPercent(paid):
	if paid < 83.05:
		return 25
	if paid >= 83.05 and paid < 111.2:
		return 50
	if paid >= 111.2 and paid < 138.67:
		return 75
	if paid >= 138.67:
		return 100

def assignAgeBuckets(age):
	if age <= 5: 
		return "5 and under"
	if age > 5 and age <= 10:
		return "6 to 10"
	if age > 10 and age <= 15:
		return "11 to 15"
	if age > 15 and age <= 20:
		return "16 to 20"
	if age > 20 and age <= 25:
		return "21 to 25"
	if age > 25 and age <= 30:
		return "26 to 30"
	if age > 30 and age <= 35:
		return "31 to 35"
	if age > 35 and age <= 40:
		return "36 to 40"
	if age > 40 and age <= 45:
		return "41 to 45"
	if age > 45 and age <= 50:
		return "46 to 50"
	if age > 50 and age <= 55:
		return "51 to 55"
	if age > 55 and age <= 60:
		return "56 to 60"
	if age > 60 and age <= 65:
		return "61 to 65"
	if age > 65 and age <= 70:
		return "66 to 70"
	if age > 70 and age <= 75:
		return "71 to 75"
	if age > 75 and age <= 80:
		return "76 to 70"
	if age > 80 and age <= 85:
		return "81 to 85"
	if age > 85 and age <= 90:
		return "86 to 90"
		
	
#  Generic Function to filter a dataframe on a column using a test value and operator
def filterDataFrame(data, column, operator, testValue):
    if operator == "=":
        return data[data[column] == testValue]
    if operator == "<":
        return data[data[column] < testValue]
    if operator == "<=":
        return data[data[column] <= testValue]
    if operator == ">":
        return data[data[column] > testValue]
    if operator == ">=":
        return data[data[column] >= testValue]
	
def hadShot(claimNumber):
	if math.isnan(claimNumber):
		return 'False'
	else:
		return 'True'
	
fluExpOnly_df = pd.read_excel('FluData_VCU_MDA_Corrected.xlsx','FLU_EXPENSES_ONLY')
fluExpOnly_df.name = 'Flu Expenses Only'
fluShotData_df = pd.read_excel('FluData_VCU_MDA_Corrected.xlsx','FLU_SHOT_DATA')
fluShotData_df.name = 'Flu Shot Data'
fluRelatedExp_df = pd.read_excel('FluData_VCU_MDA_Corrected.xlsx','FLU_RELATED_EXPENSES')
fluRelatedExp_df.name = 'Flu Related Expenses'
uniqueShotCount = len(fluShotData_df.groupby(['MEMBER_ID','FISCAL_YEAR']))
print uniqueShotCount

audit_column(fluExpOnly_df, 'PAID_AMT')
audit_column(fluRelatedExp_df, 'PAID_AMT')
audit_column(fluShotData_df, 'PAID_AMT')

sys.exit()

fluExp2016 = filterDataFrame(fluExpOnly_df,'FISCAL_YEAR','=',2016)
fluShot2016 = filterDataFrame(fluShotData_df,'FISCAL_YEAR','=',2016)
fluShot2016 = fluShot2016.drop_duplicates(['MEMBER_ID'])
print "Number of Shots 2016 " + str(len(fluShot2016))
flu2016 = fluExp2016.merge(fluShot2016,on=['MEMBER_ID'],how='left')
flu2016['HAD_SHOT'] = flu2016['CLAIM_NUM_y'].apply(hadShot)

writer = pd.ExcelWriter('flu2016.xlsx')
flu2016.to_excel(writer,'FLU_EXP_ONLY_WITH_SHOTS_2016')
writer.save()

flu2016withShot = flu2016[flu2016['HAD_SHOT']=='True']
flu2016withShot.name = 'Flu 2016 with Shot'
flu2016withNoShot = flu2016[flu2016['HAD_SHOT']=='False']
flu2016withNoShot.name = 'Flu 2016 with No Shot'

audit_column(flu2016withShot,'PAID_AMT_x')
audit_column(flu2016withNoShot,'PAID_AMT_x')


fluShotData_df = fluShotData_df.drop_duplicates(subset=['MEMBER_ID','FISCAL_YEAR'])
print len(fluShotData_df)

expOnly_with_shots_df = fluExpOnly_df.merge(fluShotData_df,on=['MEMBER_ID','FISCAL_YEAR'], how='left')
expOnly_with_shots_df['HAD_SHOT'] = expOnly_with_shots_df['CLAIM_NUM_y'].apply(hadShot)

writer = pd.ExcelWriter('FluOnlyExp_WithShotData.xlsx')
expOnly_with_shots_df.to_excel(writer,'FLU_EXP_ONLY_WITH_SHOTS')
writer.save()

fluExpHadShot = expOnly_with_shots_df[expOnly_with_shots_df['HAD_SHOT'] == 'True']
fluExpHadShot.name = "Flu Exp Only with Shot"
fluExpNoShot = expOnly_with_shots_df[expOnly_with_shots_df['HAD_SHOT'] == 'False']
fluExpNoShot.name = "Flu Exp Only with No Shot"

audit_column(fluExpHadShot, 'PAID_AMT_x')

audit_column(fluExpNoShot, 'PAID_AMT_x')



#fluExpOnly_df.sort_values(by='PAID_AMT',axis=0,ascending=False,inplace=True)

#audit_column(fluExpOnly_df,'PAID_AMT')
fluExpOnly_df.name = "Flu Expenses Only"
audit_column(fluExpOnly_df,'AGE')

fluExpOnly_df['quartile'] = fluExpOnly_df['PAID_AMT'].apply(assignPercent)
fluExpOnly_df['ageBuckets'] = fluExpOnly_df['AGE'].apply(assignAgeBuckets)
fluOnly_fy2017 = filterDataFrame(fluExpOnly_df,'FISCAL_YEAR','=',2017)

dfAmtByAge = fluOnly_fy2017.groupby(['ageBuckets'])['PAID_AMT'].sum()
dfAmtByAge = dfAmtByAge.sort_values(ascending=False)
axes = dfAmtByAge.plot(kind="bar")
plt.title("Expenses by Age")
plt.tight_layout()
plt.show()

totalExp = fluOnly_fy2017['PAID_AMT'].sum()
print "TOTAL EXP: " + str(totalExp)

kidsBuckets = ['5 and under','6 to 10','11 to 15','16 to 20']

dfKids = fluOnly_fy2017[fluOnly_fy2017['ageBuckets'].isin(kidsBuckets)]

plt.hist(dfKids['quartile'])
plt.show()

dfKidsByDiag = dfKids.groupby(['LABEL_NAME/DIAG_CODE'])['PAID_AMT'].sum()
dfKidsByDiag = dfKidsByDiag.sort_values(ascending=False);
axes = dfKidsByDiag.plot(kind="bar")
plt.title("Total Amt Paid Grouped by Diagnosis Code (Age < 21)")
plt.tight_layout()
plt.show()

#sys.exit()

audit_column(fluExpOnly_df,'quartile')
plt.hist(fluExpOnly_df['quartile'])
plt.show()

df_amt_by_quartile = fluExpOnly_df.groupby(['quartile'])['PAID_AMT'].sum()
axes = df_amt_by_quartile.plot(kind="bar")
plt.title("Total Amt Paid Grouped by Quartile")
plt.tight_layout()
plt.show()

audit_column(fluExpOnly_df,'LABEL_NAME/DIAG_CODE')

df_amt_by_diag = fluExpOnly_df.groupby(['LABEL_NAME/DIAG_CODE'])['PAID_AMT'].sum()
axes = df_amt_by_diag.plot(kind="bar")
plt.title("Total Amt Paid Grouped by Diagnosis Code")
plt.tight_layout()
plt.show()


topQtr = filterDataFrame(fluExpOnly_df,'quartile','=',100)
topQtrAmts = topQtr.groupby(['LABEL_NAME/DIAG_CODE'])['PAID_AMT'].sum()
axes = topQtrAmts.plot(kind="bar")
plt.title("Total Amt for Diagnosis Code for Top Quartile")
plt.tight_layout()
plt.show()




