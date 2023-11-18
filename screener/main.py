# General Control flow:
#   Run UI, wait for user input
#   Once we get a github username and resume:
#       - Scan resume
#       - Pull relevant github files
#   Loop through skills, and evaluate code
#   Pass output from granular evaluations to higher level evaluation
#
# Imports
#from ui.streamlit_proto.py import generate_ui
from document_scan.DocumentAI.py import scan_resume

def main():
    scan_resume

if __name__ == "__main__":
    main()
