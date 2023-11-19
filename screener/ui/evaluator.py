# We want two evaluator functions: 
#   The meta-evaluator that interacts with the UI
#       - Interacts with granular evaluator to compile granular summaries into 
#       higher level summary
#       - Outputs higher level summary to UI
#   A more granular evaluator that takes in and evaluates a skill
#       - Loops through relevant github files
#       - Outputs evaluations to meta-evaluator

from google.cloud import aiplatform
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain, StuffDocumentsChain
from langchain.text_splitter import CharacterTextSplitter
## DocumentLoaders and TextSplitters are not included here. These are super useful to process/chunk large inputs into prompts

#Setup VertexAI model for langchain
llm = VertexAI(model_name="code-bison",max_output_tokens=1000,temperature=0.3)

# Map Step 1: file -> file description
file_map_template 
#
# Reduce Step 1: file descriptions -> repo description

# Reduce Step 2: Repo descriptions -> candidate description

def meta_eval(descriptions, skills):
    # Map step: file descriptions -> repository description
    # This basically asks for all of the file descriptions at once -- prob inefficient
    # Need to specify delimiting character betweeen files and some format for name, language, etc. of a file
    repo_map_template = """You are a technical hiring manager trying to judge the skills and quality of a candidate.
    Your direct report has produced this set of descriptions of files within this candidates git repository. 
    Based on this list of reports, please summarize the quality of this repository and provide a detailed overview of the code.
    Think step by step. 
    ```
    {descriptions}
    ```
    Helpful Summary: """
    
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm,prompt=map_prompt)

    # Reduce step: repository descriptions -> Candidate evaluation
    reduce_template = """You are a technical hiring manager trying to judge the capabilities of a candidate.
    The following is a set of descriptions and judgements of various code repositories that the candidate has authored. 
    {repo_descriptions}
    Take these and organize these into a final, consolidated judgement of this candidate's strenghts and weaknesses.
    Compare the skills and weaknesses with the following list of skills from the candidate's resume.
    {skills}
    At the end of your description of the candidate, give your definitive recommendation on whether this candidate deserves an interview. 
    """

    reduce_prompt = PromptTemplate(template=reduce_template,input_variables=["descriptions","skills"])
    reduce_chain=LLMChain(llm=llm,prompt=reduce_prompt)

    combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="repo_descriptions"
    )

    reduce_documents_chain = ReduceDocumentsChain(
            combine_documents_chain=combine_documents_chain,
            collapse_documents_chain=combine_documents_chain,
            token_max=4000
    )

    map_reduce_chain = MapReduceDocumentsChain(
            llm_chain=map_chain,
            reduce_documents_chain=reduce_documents_chain,
            document_variable_name="descriptions",
            return_intermediate_steps=False
    )

    # Running the MapReduce Chain
    evaluation = map_reduce_chain.run(doc_captions)
    return evaluation


def granular_eval():
    # Take each file, summarize and judge it
    # get from Josue
    pass

def get_skills():
    # Get list of skills from resume
    # Get from Christopher
    pass
