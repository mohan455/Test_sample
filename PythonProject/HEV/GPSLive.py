import pandas as pd



df=pd.read_csv("2nd_All_messages_Data.csv")
#GPSLIVE=df[df['parsedData.messagetype']=='gpslive'].sort_values('createdDatetime')
#print(GPSLIVE)
Sorted_Data=(df[df['parsedData.messagetype']=='gpslive'][['parsedData.messagetype','parsedData.SequenceNo']])

print(Sorted_Data['parsedData.SequenceNo'].dtype)

Sorted_Data['parsedData.SequenceNo']=pd.to_numeric(Sorted_Data['parsedData.SequenceNo'].astype(str).str.replace(',',''),errors='coerce')
print(Sorted_Data['parsedData.SequenceNo'].dtype)

Sorted_Data['difference']=Sorted_Data['parsedData.SequenceNo'].diff()
# print(Sorted_Data.head())
print(Sorted_Data.sort_values(by='parsedData.SequenceNo',ascending=True))