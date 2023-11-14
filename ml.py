###############################################
#LOGIC
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import faiss
import os
#from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import openai
from langchain.chains import RetrievalQA


# Load .env file
#oad_dotenv()

doc_reader = PdfReader("text.pdf")

raw_text = ''
for i,page in enumerate(doc_reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(
    separator='n',
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
embeddings = OpenAIEmbeddings("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")

docsearch = faiss.FAISS.from_texts(texts,embeddings)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":4})
rqa = RetrievalQA.from_chain_type(llm=openai.OpenAI(),
                                  chain_type="stuff",
                                  retriever=retriever,
                                  return_source_documents= True)


##############################################