from google.cloud import aiplatform
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from git_output_sample_data.json_nico import test_dict

def rawToDesc(skills, rawFile, repoDesc, readMe): #skills string, rawFile string, repoDesc string
    template = """The following is a list of skills provided from this candidates resume.
    An optional repo description from this users Github is provided.
    The optional ReadMe is provided as well. Do not fill in any unprovided details.

    Skills: {skills}

    Raw File: {rawFile}

    Repo Description: {repoDesc}

    ReadMe: {readMe}
    
    Action: Provide a one line description of this file and how it relates to the repo.
    Provide and rank (from a scale of 1-10) 2 programming concepts that this file excels in. 
    Provide and rank (from a scale of 1-10) 2 programming concepts that this file struggles with.

    Answer:
    """

    llm = VertexAI(model_name="code-bison",max_output_tokens=1000,temperature=0.3)
    prompt = PromptTemplate(template=template, input_variables=[skills,rawFile,repoDesc,readMe])


    llm_chain = LLMChain(prompt=prompt,llm=llm)

    response = llm_chain.run({"skills":skills,"rawFile":rawFile,"repoDesc":repoDesc,"readMe":readMe})
    return response

if __name__ == "__main__":
    print(test_dict)