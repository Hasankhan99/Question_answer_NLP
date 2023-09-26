# Question Answer Service # 
This Service used for question answer data from custom data using open ai it will take question from user and generate useful output from data we provided to model, framework used in this service is [langchain](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa)
# Prepare Custom dataset
It will make the vector database form the file context present in ```en_data.txt```
```
python ingest.py
```
it will save vector database into folder ```vector_db``` 
```
vector
  |____docs.index
  |____faiss_store.pkl
```
# Output:
In ```main.qa``` input call function predict and pass you text parameter into it, it will generate output using chat history memory and documents fetch from retriever using cousin similarity and generate answer using both information.
``` 
print(predict('What is metastar usage fees?'))
```

