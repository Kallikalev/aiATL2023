from google.cloud import aiplatform
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import TextLoader

#from git_output_sample_data.json_nico import test_dict

#Input is summary of all the repos
# List of skills
# summarize all summaries

def fileToRepoDesc(RepositorySummaries, skillList): #skills string, rawFile string, repoDesc string
    
    RepositorySummaries = '\n\n'.join(RepositorySummaries)

    template = """ You are a technical hiring manager trying to judge the capabilities of a candidate.
    The following is a set of descriptions and judgments of various code rpeositories that the candidate has author
    {repo_summaries}
    Take these and organize these into a final, consolidated judgment of this candidate's stregths and weaknesses.
    Compare theskills and weaknesses with the following list of skills from the candidate's resume.
    At the end of your description of the candidate, give your definitive reccomendation.
    """

    llm = VertexAI(model_name="text-bison",max_output_tokens=500,temperature=0.3)
    prompt = PromptTemplate(template=template, input_variables=["repo_summaries","skill_list"])


    llm_chain = LLMChain(prompt=prompt,llm=llm)
    
    # Define StuffDocumentsChain
    #stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    #loader = TextLoader(RepositorySummaries)

    response = llm_chain.run({"repo_summaries":RepositorySummaries,"skill_list":skillList})
    return response

if __name__ == "__main__":
    dummy_list = '[Relational Database Design, Data Modeling, SQL Programming, Data Integrity, Normalization, Natural Language Processing (NLP), Machine Learning, Artificial Intelligence (AI), Conversational AI, Chatbot Development, Command-Line Interface (CLI) Programming, User Experience Design, Software Development Methodologies, Task Automation, User Interaction]'
    with open('/home/boon/GThack/chad_giga_repo.txt','r') as f:
        dummy_sum = f.read()
    print(fileToRepoDesc(dummy_sum,dummy_list))
