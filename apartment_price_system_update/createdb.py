import requests
import pandas as pd
import sqlite3
import json
import googletrans
import glob




config = json.load(open('config.json', 'r',encoding='utf-8'))
conn=sqlite3.connect('tem.db')



# Get the data from the url
def get_data(url):
    app_key = 'l7xxoz7zDiK3lu5bflAExeWJG8nLYRuCCfFC'
    response = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'},
                             data={'appKey': app_key})
    response.encoding = 'uft-8-sig'
    if response.status_code != 200 or response.content.decode('utf-8-sig') == "False" :
        print('url is not working',url)
        return False

    return response.content.decode('utf-8-sig')
    

def read_data_from_files():
    config = json.load(open('config.json', 'r',encoding='utf-8'))
    
    for filename in glob.glob('*temp/*.txt'):
        columns=config[filename.split('\\')[-1][:-4]]['columns']
        # print(filename.split('\\')[-1])
        df=pd.read_csv(filename,encoding='utf-8',delimiter='|')
        print(filename)
        df.columns=columns
        df.to_sql(filename.split('\\')[-1][:-4], conn, if_exists='replace', index=False)
        

# read_data_from_files()


def create_temp_data(data,column_names,table_name):
    data = data.split('\n')
    data = [i.split('|') for i in data]
    # print(data)
    data = pd.DataFrame(data, columns=column_names,index=None)
    # data = data.drop([''], axis=1)
    # data = data.dropna(axis=0)
    data = data.reset_index(drop=True)
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    return data

def create_db():
    config = json.load(open('config.json', 'r',encoding='utf-8'))
    for i in config['all_apis_key']['names']:
     
        url=config[i]['url']
        columns=config[i]['columns']
        table_name=config[i]['table_name']
        data=get_data(url)
        if not data:
            continue
        data=create_temp_data(data,columns,table_name)

#Run create_db() to create the database and call apis
create_db()






    
    

