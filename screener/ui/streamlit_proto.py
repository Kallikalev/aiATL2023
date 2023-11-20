import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PyPDF2 import PdfWriter
from pipeline import runPipeline

#from screener.document_scan.DocumentAI.py import 
#from screener.codey.evaluator.py import 

## Dummy Data

fake_summary = "Meet Chad Giga, the epitome of a Google Developer. Chad is a highly skilled and experienced software engineer with a passion for innovation and a knack for solving complex problems. He possesses a deep understanding of computer science fundamentals and is proficient in a variety of programming languages and technologies. Chad is also an excellent communicator and collaborator, making him an invaluable asset to any team."
## End of Dummy Data

candidate_evaluation = "No candidate summary could be generated."
candidate_scores = dict()

# create form
with st.form("master_form"):
    #Column Formatting
    col1, col2 = st.columns(2,gap="medium")
    submit_flag = False

    with col1:
        uploaded_resume = st.file_uploader('Choose your Resume file',type="pdf")
        ## transform PDF to bytes or StringIO to send to DocumentAI

    with col2:
    ###Write error message if non-valid github format
        git_user = st.text_input('Git Username','',key='git')
        st.write('Account url: ', "github.com/" + git_user)

        submit_btn = st.form_submit_button("Submit Git")
        if submit_btn and git_user:
            candidate_evaluation, candidate_scores = runPipeline(git_user, uploaded_resume)
            st.write(':green[Submission Successful]')
            submit_flag = True
        elif submit_btn and not git_user:
            st.write(':red[Enter Git Username to Continue]')

    st.markdown("##")

    if submit_flag:
        skills_ls = list(candidate_scores.keys())
        skill_scores = list(candidate_scores.values())
        col3, col4 = st.columns(2)
        with col3:
            st.write("List of Skills found in resume")
            for skill in skills_ls:
                st.markdown(f"- {skill}")

        st.markdown("##")

        with col4:
            y_pos = np.arange(len(skills_ls))
            fig, ax = plt.subplots(figsize=(5,5))
            hbars = ax.barh(y_pos,skill_scores, align='center')
            ax.set_yticks(y_pos, labels=skills_ls)
            ax.invert_yaxis()  # labels read top-to-bottom
            #ax.set_xlabel('Score')
            ax.set_title('Skill Scoreboard',fontsize=20)
            # Label with specially formatted floats
            ax.bar_label(hbars, fmt='%.1f',padding=5,fontsize=14)
            ax.set_xlim(right=12)  # adjust xlim to fit labels
            ax.set_xticks([])
            plt.yticks(fontsize = 15) 
            st.pyplot(fig)


        st.markdown("##")

        ## Candidate Summary
        st.write('Candidate Summary \n')
        # Generated summary string passed below
        st.write(candidate_evaluation)

        st.markdown("##")
    
        ## Expander for Question-Answer BOT
        expander = st.expander("Click to ask questions about Resume and Github")
        with expander:
            user_prompt = st.text_area("",placeholder="Ex. Does the candidate have experience in datacleaning?")
