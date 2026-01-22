from tokenize import group

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("packet_history_3047430194_21-11_to_21-11-2023.csv")
#print(df.head())
#sample=df['Message Type']
#print(sample)
#selected_rows=df.loc[[0,50]]
#print(selected_rows)
#particular_message_type=df[df['Message Type']=='TRIP_START']
#print(particular_message_type)
#sample=df['Sequence Number'].max()
#print(sample)
#sample=df['Sequence Number'].min()
#print(sample)
#sample=df.describe()
#print(sample)
#sample=df['Message Type'].describe()
#print(sample)
#df.info()
#sample=df[["Message Type","Sequence Number","Packet Status"]]
#print(sample)
#count_values=sample['Message Type'].value_counts()
#print(count_values)
sample=df[df['Message Type']=='LCV_BS6_OBD2_PERIODIC'] [['Message Type','Sequence Number']]
sample['diffrence']=sample['Sequence Number'].diff()

print(sample)