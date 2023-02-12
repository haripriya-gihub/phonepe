

#Once created the clone of GIT-HUB repository then,
#Required libraries for the program
#aggregated transaction
import pandas as pd
import json
import os

#This is to direct the path to get the data as states

path="C:\\phonepe\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
pd.DataFrame(clm)


#db
import sqlite3
conn = sqlite3.connect('phonepe.db')
c = conn.cursor()

#create a table in the database
c.execute('''CREATE TABLE IF NOT EXISTS aggregate_transaction(
            State TEXT,
            Year TEXT,
            Quater TEXT,
            Transacion_type TEXT,
            Transacion_count TEXT,
            Transacion_amount TEXT
            )''')
#insert the All data into the table
c.executemany('INSERT INTO aggregate_transaction VALUES(?,?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['Transacion_type'], clm['Transacion_count'], clm['Transacion_amount']))

#show the data in the table
x=c.execute("SELECT * FROM aggregate_transaction")
x=c.fetchall()
for row in x:
    print(row)
    
d=c.execute("SELECT * FROM aggregate_transaction WHERE State='tamil-nadu' AND Year='2018' AND Quater='1' AND Transacion_type='Recharge & bill payments' AND Transacion_amount>0")
d=c.fetchall()
for row in d:
  print(row)
  import pandas as pd
import json
import os
#map transaction

path="C:\\phonepe\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'district':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    
    Agg_yr=os.listdir(p_i)   
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            
            Data=open(p_k,'r')
            D=json.load(Data)
            
            
            for z in D['data']['hoverDataList']:
                 Name = z['name']
                 count = z['metric'][0]['count']
                 amount = z['metric'][0]['amount']
                 clm['district'].append(Name)
                 clm['Transaction_count'].append(count)
                 clm['Transaction_amount'].append(amount)
                 clm['State'].append(i)
                 clm['Year'].append(j)
                 clm['Quater'].append(int(k.strip('.json')))
pd.DataFrame(clm)


c.execute('''CREATE TABLE IF NOT EXISTS transaction_map(
            State TEXT,
            Year TEXT,
            Quater TEXT,
            district TEXT,
            Transaction_count TEXT,
            Transaction_amount TEXT
            )''')
#insert the All data into the table
c.executemany('INSERT INTO transaction_map VALUES(?,?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['district'], clm['Transaction_count'], clm['Transaction_amount']))

#show the data in the table
x=c.execute("SELECT * FROM transaction_map")
x=c.fetchall()
for row in x:
    print(row)


import pandas as pd
import json
import os


path="C:\\phonepe\\pulse\\data\\top\\transaction\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#top transaction
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'Transaction_districts':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    
    Agg_yr=os.listdir(p_i)   
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            
            Data=open(p_k,'r')
            D=json.load(Data)
            
            data = D.get('data')
            districts = data.get('districts')
            pincodes = data.get('pincodes')

            for z in D['data']['districts'] or D['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                clm['Transaction_districts'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
pd.DataFrame(clm)
#print(clm)


              
c.execute('''CREATE TABLE IF NOT EXISTS top_transaction(
            State TEXT,
            Year TEXT,
            Quater TEXT,
            Transaction_districts TEXT,
            Transaction_count TEXT,
            Transaction_amount TEXT
            )''')
#insert the All data into the table
c.executemany('INSERT INTO top_transaction VALUES(?,?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['Transaction_districts'], clm['Transaction_count'], clm['Transaction_amount']))

#show the data in the table
x=c.execute("SELECT * FROM top_transaction")
x=c.fetchall()
for row in x:
    print(row)
   
d=c.execute("SELECT * FROM top_transaction WHERE State='tamil-nadu' AND Year='2018' AND Quater='1' AND Transaction_amount>0")
d=c.fetchall()
for row in d:
  print(row)
  


import pandas as pd
import json
import os
#aggregated user

path="C:\\phonepe\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'registered_users':[],'app_opens':[], 'phone_brand':[], 'phone_brand_count':[] ,'phone_percentage':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    
    Agg_yr=os.listdir(p_i)   
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            
            Data=open(p_k,'r')
            D=json.load(Data)
            registeredUsers = D['data']['aggregated']['registeredUsers']
            appOpens = D['data']['aggregated']['appOpens']
            
            data = D.get('data')
            usersByDevice = data.get('usersByDevice')

            for z in usersByDevice or []:
             
              Brand = z['brand']
              count = z['count']
              percentage = z['percentage']
              clm['registered_users'].append(registeredUsers)
              clm['app_opens'].append(appOpens)
              clm['phone_brand'].append(Brand)
              clm['phone_brand_count'].append(count)
              clm['phone_percentage'].append(percentage)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
pd.DataFrame(clm)
#print(clm)

#create a table in the database
c.execute('''CREATE TABLE IF NOT EXISTS aggregated_user(
            State TEXT,
            Year TEXT,
            Quater TEXT,
            registered_users TEXT,
            app_opens TEXT,
            phone_brand TEXT,
            phone_brand_count	TEXT,
            phone_percentage TEXT
            )''')
            
 #insert the All data into the table
c.executemany('INSERT INTO aggregated_user VALUES(?,?,?,?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['registered_users'], clm['app_opens'], clm['phone_brand'], clm['phone_brand_count'], clm['phone_percentage']))

#show the data in the table
x=c.execute("SELECT * FROM aggregated_user")
x=c.fetchall()
for row in x:
    print(row)
    


import pandas as pd
import json
import os
#map user
#------------

path="C:\\phonepe\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'district':[], 'map_registered_users':[], 'app_opens':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    
    Agg_yr=os.listdir(p_i)   
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            
            Data=open(p_k,'r')
            D=json.load(Data)
            # registeredUsers = D['data']['hoverData']['registeredUsers']
            # appOpens = D['data']['hoverData']['appOpens']
            
            data = D.get('data')
            hoverData = data.get('hoverData')
            for district, value in hoverData.items():
              registeredUsers = value.get('registeredUsers')
              appOpens = value.get('appOpens')
              clm['district'].append(district)
              clm['map_registered_users'].append(registeredUsers)
              clm['app_opens'].append(appOpens)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
pd.DataFrame(clm)



#create a table in the database
c.execute('''CREATE TABLE IF NOT EXISTS map_user(
            State TEXT,
            Year TEXT,
            Quater TEXT,
            district TEXT,
            map_registered_users TEXT,
            app_opens TEXT
            )''')
 #insert the All data into the table
c.executemany('INSERT INTO map_user VALUES(?,?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['district'], clm['map_registered_users'], clm['app_opens']))

#show the data in the table
x=c.execute("SELECT * FROM map_user")
x=c.fetchall()
for row in x:
    print(row)
    



import pandas as pd
import json
import os
#top user
#---------
path="C:\\phonepe\\pulse\\data\\top\\user\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[], 'district_name':[], 'registered_users':[]} 
for i in Agg_state_list:
    p_i=path+i+"/"
    
    Agg_yr=os.listdir(p_i)   
    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            districts = data.get('districts')
            pincodes = data.get('pincodes')
            for z in D['data']['districts'] or D['data']['pincodes']:
              districtsName = z['name']
              registeredUsers = z['registeredUsers']
              clm['registered_users'].append(registeredUsers)
              clm['district_name'].append(districtsName)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
pd.DataFrame(clm)



  #create a table in the database
c.execute('''CREATE TABLE IF NOT EXISTS top_user(
            State TEXT,
            Year TEXT,
            Quater TEXT,
             district_name TEXT,
            registered_users TEXT
            )''')
 #insert the All data into the table
c.executemany('INSERT INTO top_user VALUES(?,?,?,?,?)', zip(clm['State'], clm['Year'], clm['Quater'], clm['district_name'], clm['registered_users']))
c.commit()

#show the data in the table
x=c.execute("SELECT * FROM top_user")
x=c.fetchall()
for row in x:
    print(row)
            

