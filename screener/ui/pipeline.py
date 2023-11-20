from github_api import get_repos_from_username
from DocumentAI import scan_resume
from get_skills_resume import get_skills
from github_api import get_repos_from_username
from RawFileToDesc import rawToDesc
from FileDescToRepoDesc import fileToRepoDesc
from final_profile_summary import RepoSumToEval
from final_score_summary import RepoSumToScores
import json

demoMode = True

def runPipeline(username, pdf):
    print(username)
    resume_raw_text = scan_resume(pdf.read())
    skills = get_skills(resume_raw_text)

    if not demoMode:
        repos = get_repos_from_username(username)
        for repo in repos:        
            print("Processing repository: " + repo["name"])
            print("\n")

            for file in repo["files"]:
                print("Processing file " + file["name"])
                file["description"] = rawToDesc(skills, repo["name"], repo["readme"], file["name"], file["contents"])
                # print(file["description"])
                print("\n")

            file_descriptions = [f["description"] for f in repo["files"]]
            repo["description"] = fileToRepoDesc(skills, repo["name"], file_descriptions, repo["stars"], repo["readme"], repo["primaryLanguage"])
            # print(repo["description"])
            print("\n")
        repo_descriptions = [r["description"] for r in repos]
    else:
        repo_descriptions = [" Repository Summary: \n        \n        The repository contains a 3D kinematic robot simulator written in C++. The simulator allows the user to control the motor angles of a robot's legs and to visualize the robot's movement. The code is well-written and demonstrates the developer's strong understanding of C++, 3D graphics, and robotics.\n\nSkill 1: C++ (Score: 8/10)\n* Strengths: The developer demonstrates a good understanding of C++ syntax and object-oriented programming principles. \n* Weaknesses: The code could be improved by using more descriptive variable names and by adding comments to explain what each function does. \n\nSkill 2: 3D Kinematic Robot Simulator (Score: 7/10)\n* Strengths: The developer demonstrates a good understanding of 3D kinematics and how to simulate the movement of a robot. \n* Weaknesses: The code could be improved by adding more features to the simulator, such as the ability to add obstacles and to simulate the effects of gravity. \n\nSkill 3: Linear Algebra (Score: 6/10)\n* Strengths: The developer demonstrates a good understanding of linear algebra concepts such as vectors and matrices. \n* Weaknesses: The code could be improved by using more efficient linear algebra algorithms. \n\nSkill 4: OpenGL (Score: 5/10)\n* Strengths: The developer demonstrates a basic understanding of OpenGL and how to use it to render 3D graphics. \n* Weaknesses: The code could be improved by using more advanced OpenGL features, such as shaders and textures. \n\nSkill 5: Robotics (Score: 4/10)\n* Strengths: The developer demonstrates a basic understanding of robotics concepts such as forward and inverse kinematics. \n* Weaknesses: The code could be improved by adding more features to the robot, such as the ability to walk and to interact with its environment. \n\nSkill 6: Multithreading (Score: 3/10)\n* Strengths: The developer demonstrates a basic understanding of multithreading and how to use it to improve the performance of a program. \n* Weaknesses: The code could be improved by using more advanced multithreading techniques, such as thread pools and mutexes.", ' Repository Summary: \nThe scratchNetwork repository contains a C++ implementation of a neural network framework, along with a Python script for visualizing data. The code is well-written and demonstrates a good understanding of linear algebra, C++, neural networks, and data visualization. However, the repository is small and does not contain any advanced techniques.\n\nSkill 1: C++ (Score: 8/10)\n* The code is well-written and uses idiomatic C++.\n* The code is efficient and uses C++-specific features such as templates and inline functions.\n\nSkill 2: Neural Networks (Score: 8/10)\n* The code demonstrates a good understanding of neural network concepts such as forward propagation, backpropagation, and weight updates.\n* The code implements a neural network framework that can be used to train and test neural networks.\n\nSkill 3: Data Visualization (Score: 7/10)\n* The Python script demonstrates the ability to visualize data in a 3D scatter plot using the Python matplotlib library.\n* The script is easy to use and can be used to visualize data from a variety of sources.\n\nSkill 4: Linear Algebra (Score: 8/10)\n* The code demonstrates a good understanding of linear algebra concepts such as matrix multiplication and vector addition.\n* The code uses efficient linear algebra operations to implement the neural network framework.', " Repository Summary: \n     The repository contains a virtual operating system project, which demonstrates the candidate's ability to design and implement a complex system. The code is well-written and organized, and the candidate has clearly put a lot of thought into the design of the system. \n\n     Skill 1: C++ (Score: 8/10) \n     Strengths: The candidate demonstrates a strong understanding of C++, with the use of templates, function overloading, and exception handling. \n     Weaknesses: None observed in this repository. \n\n     Skill 2: Operating Systems (Score: 8/10) \n     Strengths: The candidate demonstrates a strong understanding of operating system concepts, such as memory management, process control, scheduling, and context switching. \n     Weaknesses: None observed in this repository. \n\n     Skill 3: Multithreading (Score: 7/10) \n     Strengths: The candidate demonstrates an understanding of multithreading concepts, such as mutex management and thread synchronization. \n     Weaknesses: Could be improved by using more advanced multithreading techniques, such as thread pools. \n\n     Skill 4: Data Structures (Score: 7/10) \n     Strengths: The candidate demonstrates an understanding of data structures, such as vectors and strings. \n     Weaknesses: Could be improved by using more advanced data structures, such as hash tables and graphs. \n\n     Skill 5: Algorithms (Score: 6/10) \n     Strengths: The candidate demonstrates an understanding of algorithms, such as sorting and searching. \n     Weaknesses: Could be improved by using more advanced algorithms, such as dynamic programming and machine learning. \n\n     Skill 6: System Programming (Score: 7/10) \n     Strengths: The candidate demonstrates an understanding of system programming concepts, such as memory management and process control. \n     Weaknesses: Could be improved by using more advanced system programming techniques, such as kernel development and device drivers.", ' Repository Summary: \nThis repository contains a React application that allows users to interact with a map and view information about gardens. \nThe code is well-written and organized, and the application is functional and easy to use. \nThe applicant has demonstrated a strong understanding of React, JavaScript, HTML, and CSS.\n\nSkill 1: React (10/10)\nThe applicant has demonstrated a strong understanding of React, with the use of components, state, and event handling. \n\nSkill 2: JavaScript (9/10)\nThe applicant has demonstrated a strong understanding of JavaScript, with the use of variables, functions, and objects. \n\nSkill 3: HTML (8/10)\nThe applicant has demonstrated a good understanding of HTML, with the use of elements, attributes, and tags. \n\nSkill 4: CSS (7/10)\nThe applicant has demonstrated a good understanding of CSS, with the use of selectors, properties, and values. \n\nSkill 5: Git (6/10)\nThe applicant has demonstrated a basic understanding of Git, with the use of commands and branching.', " Repository summary: The repository contains code for a Minecraft Reinforcement Learning environment. The code is written in Python and uses libraries such as PyTorch, NumPy, and Mineflayer. The repository demonstrates the candidate's skills in Python programming, artificial intelligence, server development, and configuration management.\n\nSkill 1: Python (9/10)\n* Strengths: The candidate demonstrates proficiency in Python by writing clear and concise code. The code is well-structured and uses Pythonic idioms.\n* Weaknesses: None observed in this repository.\n\nSkill 2: Artificial Intelligence (8/10)\n* Strengths: The candidate demonstrates knowledge of AI concepts such as reinforcement learning, deep learning, and computer vision. The code implements a deep reinforcement learning algorithm to train a Minecraft agent to navigate a maze.\n* Weaknesses: The code could be improved by using more advanced AI techniques, such as hierarchical reinforcement learning or model-based reinforcement learning.\n\nSkill 3: Server Development (7/10)\n* Strengths: The candidate demonstrates the ability to set up and configure a Minecraft server. The code includes a script to start the server and a configuration file to specify the server settings.\n* Weaknesses: The code could be improved by adding more features to the server, such as support for multiple players or a web-based interface.\n\nSkill 4: Configuration Management (6/10)\n* Strengths: The candidate demonstrates the ability to manage configuration files. The code includes a configuration file to specify the server settings and a script to load the configuration file.\n* Weaknesses: The code could be improved by using a more robust configuration management system, such as Ansible or Puppet."]

    print(repo_descriptions)
    
    if demoMode:
        final_scores_json_string = """
            { "C++": 8.67,
            "Python": 8.5,
            "Data Structures": 7.5,
            "Algorithms": 7.33,
            "React": 8,
            "Software Design": 6
            }
        """
        final_eval = """
        - The candidate has a strong understanding of C++, with experience in 3D graphics, robotics, and neural networks. 
        - The candidate has experience in operating system design and implementation, as well as multithreading and data structures. 
        - The candidate has experience in web development with React, as well as AI and server development with Python. 

        **Strengths:**
        - Strong technical skills in C++, Python, Java, and JavaScript
        - Experience in a variety of domains, including 3D graphics, robotics, operating systems, and web development
        - Ability to learn new technologies quickly and apply them to real-world problems

        **Weaknesses:**
        - Some of the candidate's projects are small and lack advanced features
        - The candidate could improve their use of descriptive variable names and comments in their code
        - The candidate could improve their knowledge of advanced multithreading techniques

        **Recommendation:**
        I recommend hiring this candidate. They have a strong foundation in computer science and have demonstrated their ability to apply their skills to a variety of real-world problems. With more experience, they will likely become a valuable asset to any team.
        """
    else:
        final_scores_string = RepoSumToScores(repo_descriptions)
        final_scores_json_string = "{" + final_scores_string.split("}")[0] + "}"
        final_eval = RepoSumToEval(repo_descriptions, skills)
        print(final_eval)
        print(final_scores_json_string)
        

    print(final_scores_json_string)
    final_scores_json = json.loads(final_scores_json_string)
    return final_eval, final_scores_json
