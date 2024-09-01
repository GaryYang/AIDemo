# from langchain.llms import Ollama
from langchain_community.llms import Ollama
input = input("What is your question?")
llm = Ollama(model="llama2-chinese")
res = llm.predict(input)
print (res)