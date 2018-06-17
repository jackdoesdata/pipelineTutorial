import pandas as pd
import numpy as np
import datetime as dt
import MySQLdb
from sqlalchemy import create_engine
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('pipelineTutorial-8fff96610970.json', scope)
client = gspread.authorize(creds)
sheet = client.open('pipelineSampleTable').sheet1
data = pd.DataFrame(sheet.get_all_values())
header = data.iloc[0]
data = data[1:]
data.columns = header

dates = ['DOB', 'signUpDate']

for i in dates:
    data[i] = pd.to_datetime(data[i], infer_datetime_format=True)
    data[i] = data[i].dt.date

data['firstName'] = data['Name'].map(lambda x:x.split(' ', 1)[0])
data['lastName'] = data['Name'].map(lambda x:x.split(' ', 1)[-1])

engine = create_engine('mysql://jack:jack1620@tutorials.clpvlhaqk6id.us-east-1.rds.amazonaws.com:3306/tutorialDB')
data.to_sql(name='pipelineTable', con=engine, if_exists='replace', index=False, chunksize=1000)
