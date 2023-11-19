import os
from google.cloud import aiplatform
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import langchain



## Pass resume_result.txt given by DocumentAI.py
resume_dir = "/home/boon/GThack/prototype/aiATL2023/screener/document_scan/test_resume/result.txt"

with open(resume_dir) as f:
    resume_txt = f.read()

## Describe_txt can be deleted
def describe_txt(raw_txt):
    loader = TextLoader(resume_dir)
    document = loader.load()
    for i, doc in enumerate(document):
        print(f'content page {i} : {doc.page_content}')
        print(f'metadata page {i} : {doc.metadata}')
        print(len(doc.page_content))
        if i == 5: break


# Setup Recursive Text Splitter - by default splits by
# ["/n/n", "/n", " ", ""] in order from left to right
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 200,
    chunk_overlap  = 20,
    length_function = len,
    is_separator_regex = False,
)

split_text = text_splitter.create_documents([resume_txt])
llm = VertexAI(model_name="code-bison",max_output_tokens=1000, temperature=0.1)

template = """
You are an technical recruiter screening candidate resumes.
Identify the candidates skills specific to programming and software development, and output in a array list format. 
Example Output: ['skill 1','skill 2', 'skill 3']

Resume: {resume}
"""

input_variables = ["resume"]
def try_prompt(template,input_variables,txt_dir,llm):
    prompt = PromptTemplate(template=template,input_variables=["resume"])
    llm_chain = LLMChain(prompt=prompt,llm=llm)
    loader = TextLoader(txt_dir)
    document = loader.load()
    output = llm_chain.run(document)
    return document, output

doc, output= try_prompt(template=template,input_variables=input_variables,txt_dir=resume_dir,llm =llm)

#OUTPUT IS STRING OF SKILL LIST
print(output)
