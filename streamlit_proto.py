import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## Dummy Data
model_skill_scores = {"C++":9.5,
"React":9.0,
"Python":9.5,
"Java":3.0,
"JavaScript":5.0,
"Django":1.0}

skills_ls = list(model_skill_scores.keys())
skill_scores = list(model_skill_scores.values())
fake_summary = "Meet Chad Giga, the epitome of a Google Developer. Chad is a highly skilled and experienced software engineer with a passion for innovation and a knack for solving complex problems. He possesses a deep understanding of computer science fundamentals and is proficient in a variety of programming languages and technologies. Chad is also an excellent communicator and collaborator, making him an invaluable asset to any team."
## End of Dummy Data

#Column Formatting
col1, col2 = st.columns(2,gap="medium")

with col1:
    uploaded_resume = st.file_uploader('Choose your Resume file',type="pdf")

with col2:
    ###Write error message if non-valid github format
    git_user = st.text_input('Git Username','')
    st.write('Repository url: ', "github.com/" + git_user)

    submit_btn = st.button("Submit Git")
    if submit_btn and git_user:
        st.write('test successful')
    elif submit_btn and not git_user:
        st.write(':red[Enter Git Username to Continue]')

st.markdown("##")
# Send pdf info to Vertex AI here
     #Convert to bytes or StringIO below
    #bytes_data = uploaded_resume.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_resume.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)
 
if submit_btn and git_user:
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
        ax.set_xlabel('Score')
        ax.set_title('Skill Scoreboard')
        st.pyplot(fig)

    st.markdown("##")

    ## Candidate Summary
    st.write('Candidate Summary \n')
    # Generated summary string passed below
    st.write(fake_summary)

    st.markdown("##")
    
    ## Expander for Question-Answer BOT
    expander = st.expander("Click to ask questions about Resume and Github")
    with expander:
        st.write('blank')


