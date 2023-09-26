
# Apartment Price system # 
Apartment price system allow user to know about update apartment prices from just single query, internal function of this service is fetch data from api, make db , data cleaning and convert into vector for apply cousin similarity between the user query and embedded documents, this service build using [langchain](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa)
# Fetch Open API data:
config file is contain all the URLs and columns name to fetch the data from naverapi if user want to add more url, it can be added in ```config.josnl``` file.
### Create database of fetched data: ###
once config file is being set with update urls we can make tem.db where all data will save, using command
```
python createdb.py
```
### Convert Raw data into Vector ###
Once We fetch the data we have to clear this data drop null value perform analysis, translate and merge using object identifier for make single file  and vector db.
```
python loaddb.py
```
it will generate two csv file for testing and vector database with following the directory hierarchy
```
docs
 |___aps.db
 |    |___index.faiss
 |    |___index.pkl
 |___full.csv
 |___filter.csv

```
# Run Pipeline
In file ```main_qa.py``` we call function ```aps(text)``` to generate ouput.
```
from main_qa import aps
output=aps("대구 남구 대봉로26길 가격을 알려주세요")
print(output)
```
Note: this agents is only know the address information mentioned in ```docs/filter.csv```
