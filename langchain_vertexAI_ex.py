from google.cloud import aiplatform
import google.auth
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Enter your project_id
creds, _ = google.auth.default(quota_project_id='git-code-scoring')

## DocumentLoaders and TextSplitters are not included here. These are super useful to process/chunk large inputs into prompts


#Setup VertexAI model for langchain
llm = VertexAI(model_name="code-bison",max_output_tokens=1000,temperature=0.3)

#Create a template that acts as context...We can pass string variables into this
template = """ You are an expert in {topic}. Answer a the users question. Think step by step.

Question: {question}

Answer:
"""

##Setup a prompt
prompt = PromptTemplate(template=template, input_variables=["topic","question"])

## Sending prompt to LLM - via Chain, there are many flavors of Chains (Ex QA, Human/Ai prompt, many more....)
# 
topic = "Python"
question = "What is the code for calculating Fibbonnaci numbers? What is it's time complexity"

llm_chain = LLMChain(prompt=prompt,llm=llm)

#Run the prompt
response = llm_chain.run({"topic":topic,"question":question})
print(response)

