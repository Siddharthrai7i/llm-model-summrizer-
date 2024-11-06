from langchain import HuggingFaceHub
import os
huggingface_api_token=os.environ.get("HUGGINGFACEHU_API_TOKEN")
llm_huggingface=HuggingFaceHub(repo_id="utrobinmv/t5_summary_en_ru_zh_base_2048",model_kwargs={"temperature":0,"max_length":200})
from fpdf import FPDF
from tkinter import*
from tkinter import filedialog
import pickle as pk
with open ('model.pkl' , 'wb') as file:
    pk.dump(llm_huggingface , file)

with open('model.pkl' , 'rb') as file:
    modal=pk.load(file)