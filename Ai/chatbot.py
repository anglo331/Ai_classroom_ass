from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="phi3:latest")

prompt = ChatPromptTemplate([
    ('system', 'you are teaching assistance your main goole to help the teacher, profesore. to find the best way to explane for there students'),
    ('user', '{in_}')
])

while True:
    in_ = input('> ')

    chain = prompt | model | StrOutputParser()

    res = chain.stream({"in_": in_})

    for chunk in res:
        print(chunk, end='')
    print()
