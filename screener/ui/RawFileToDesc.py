from google.cloud import aiplatform
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from git_output_sample_data.json_nico import test_dict

def rawToDesc(skills, rawFile, repoName, readMe): #skills string, rawFile string, repoDesc string
    template = """The following is a list of skills provided from this candidates resume.
    An optional repo description from this users Github is provided.
    The optional ReadMe is provided as well. Do not fill in any unprovided details.

    Skills: {skills}

    Raw File: {rawFile}

    Repository Name: {repoName}

    ReadMe: {readMe}
    
    Structure your answer as follows:

    ```json
        {
            "action": "Provide a one line description of this file and how it relates to the repository.",
            "concept 1": "Provide and score (on a scale from 1 to 10) one programming concept that this file excels in."
            "concept 2": "Provide and score (on a scale from 1 to 10) one programming concept that this file excels in."
            "concept 3": "Provide and score (on a scale from 1 to 10 -- note that this is a negative signal) one programming concept that this file strugles in."
            "concept 4": "Provide and score (on a scale from 1 to 10 -- note that this is a negative signal) one programming concept that this file struggles in."
        }
    ```
    Answer:
    """

    llm = VertexAI(model_name="code-bison",max_output_tokens=1000,temperature=0.3)
    prompt = PromptTemplate(template=template, input_variables=["skills","rawFile","repoName","readMe"])


    llm_chain = LLMChain(prompt=prompt,llm=llm)

    response = llm_chain.run({"skills":skills,"rawFile":rawFile,"repoName":repoName,"readMe":readMe})
    return response


