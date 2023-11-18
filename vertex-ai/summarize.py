import vertexai
from vertexai.language_models import TextGenerationModel

def summarize(prompt, context):
    vertexai.init(project="github-recruiter-405500", location="us-central1")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(
        f"""{prompt}\ncontext: {context}""",
        **parameters
    )
    return (f"Response from Model: {response.text}")

if __name__ == "__main__":
    prompt = """- Rate your confidence in the author of this code's skills as a developer (on a scale from 0 to 100) based on the following factors:
    - documentation & commenting (15 total points),
	- syntax errors (15 total points, this should be a negative signal, deduct points if there are errors present),
	- modularity (10 total points),
	- Impact (does this look like production code or isolated toy code) (5 total points),
	- reusability and level of abstraction (15 total points),
	- whether it includes tests and the quality of those tests (15 total points),
	- clarity of variable and function names (10 total points),
	- does this person seem to use good programming practices (15 total points)
    - Provide a short summary of your score and the breakdown for each category. Tell me what language the code is written in, and what the program seems to do. It is alright if you cannot come to a conclusion for a category, do not make up or falsify any conclusions."""

    context = """
        import pandas as pd
    from bs4 import BeautifulSoup
    import requests

    df = pd.read_csv('./file-history/concatenated.csv')

    def prepareUrl(url): #reformats HTML-URL to redirect to raw code for scraping
        out = ''
        out = url.replace('github.com', 'raw.githubusercontent.com')
        out = out.replace('/blob', '')
        return out

    df['RAW'] = df['HTML-URL'].apply(prepareUrl)

    urlList = df['RAW']
    print('URL editing complete')

    def fetchCode(url): #Calls BeautifulSoup to grab code from altered URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()
            
    print('start')
    df['CODE'] = urlList.apply(fetchCode) 
    #1108 Entries will take ~220 Seconds to fetch all data (WILL VARY ON CONNECTION SPEED)

    df.to_csv('./file-history/finalTable.csv')
    print('finalTable.csv created')"""
    print(summarize(prompt,context))