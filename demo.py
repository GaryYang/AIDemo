
# from langchain.llms import HuggingFacePipeline
# from langchain.llms import HuggingFaceHub
from langchain_openai.llms import OpenAI

from langchain_openai.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("hi!")


chat_model.predict("hi!")



print("hello world!!!")
