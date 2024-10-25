import streamlit as st
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from Resume import temp1
from Portfolio import temp2
import base64

if 'resume1' not in st.session_state:
    st.session_state['resume1'] = True
if 'temp1' not in st.session_state:
    st.session_state['temp1'] = False
if 'temp2' not in st.session_state:
    st.session_state['temp2'] = False
if 'save_data' not in st.session_state:
    st.session_state['save_data'] = False
if 'load_data' not in st.session_state:
    st.session_state['load_data'] = False

st.sidebar.header("Select your Templates")

st.sidebar.image("Portfolio.png", caption="Portfolio", use_column_width=True)
temp_button2 = st.sidebar.button("Portfolio 💼", key='btn2')

st.write("\n\n")

st.sidebar.image("Resume.jpeg", caption="Resume", use_column_width=True)
temp_button1 = st.sidebar.button("Resume 📁", key="btn1")

save_data_button = st.sidebar.button("Save Data", key="btn_save_data")
load_data_button = st.sidebar.button("Load Data", key="btn_load_data")

if save_data_button:
    st.session_state['save_data'] = True
    st.session_state['load_data'] = False
elif load_data_button:
    st.session_state['load_data'] = True
    st.session_state['save_data'] = False

if st.session_state['save_data']:
    st.title("Save Data")
    user_data = {
        "Name": st.text_input("Name"),
        "Email": st.text_input("Email"),
        "Phone": st.text_input("Phone"),
        "Website": st.text_input("Website"),
        "Bio": st.text_area("Bio", height=200),
        "Companies": [],
        "Education": [],
        "Projects": [],
        "Skills": [],
        "Hobbies": [],
        "Achievements": [],
        "ProgrammingLanguages": [],
        "Tools": []
    }

    num_companies = st.number_input("Number of Companies to Add", min_value=0, step=1)
    for i in range(num_companies):
        st.write(f"Company {i + 1}")
        cols = st.columns(4)
        company_data = {
            "CompanyName": cols[0].text_input(f"Company Name", key=f"company_name_{i}"),
            "CompanyPeriod": cols[1].text_input(f"Company Period", key=f"company_period_{i}"),
            "CompanyRole": cols[2].text_input(f"Company Role", key=f"company_role_{i}"),
            "WorkDetails": cols[3].text_input(f"Work Details", key=f"work_details_{i}"),
        }
        user_data["Companies"].append(company_data)

    num_education = st.number_input("Number of Education Entries to Add", min_value=0, step=1)
    for i in range(num_education):
        st.write(f"Education {i + 1}")
        cols = st.columns(4)
        education_data = {
            "SchoolName": cols[0].text_input(f"School Name", key=f"school_name_{i}"),
            "StudyPeriod": cols[1].text_input(f"Study Period", key=f"study_period_{i}"),
            "CourseName": cols[2].text_input(f"Course Name", key=f"course_name_{i}"),
            "GPA": cols[3].text_input(f"GPA", key=f"gpa_{i}"),
        }
        user_data["Education"].append(education_data)

    num_projects = st.number_input("Number of Projects to Add", min_value=0, step=1)
    for i in range(num_projects):
        st.write(f"Project {i + 1}")
        cols = st.columns(2)
        project_data = {
            "ProjectName": cols[0].text_input(f"Project Name", key=f"project_name_{i}"),
            "TechStacks": cols[1].text_input(f"Tech Stacks", key=f"tech_stacks_{i}"),
            "ProjectDescription": st.text_area(f"Project Description", height=200, key=f"project_description_{i}"),
        }
        user_data["Projects"].append(project_data)

    num_skills = st.number_input("Number of Skills to Add", min_value=0, step=1)
    for i in range(num_skills):
        user_data["Skills"].append(st.text_input(f"Skill {i + 1}", key=f"skill_{i}"))

    num_hobbies = st.number_input("Number of Hobbies to Add", min_value=0, step=1)
    for i in range(num_hobbies):
        user_data["Hobbies"].append(st.text_input(f"Hobby {i + 1}", key=f"hobby_{i}"))

    num_achievements = st.number_input("Number of Achievements to Add", min_value=0, step=1)
    for i in range(num_achievements):
        user_data["Achievements"].append(st.text_input(f"Achievement {i + 1}", key=f"achievement_{i}"))

    num_programming_languages = st.number_input("Number of Programming Languages to Add", min_value=0, step=1)
    for i in range(num_programming_languages):
        user_data["ProgrammingLanguages"].append(st.text_input(f"Programming Language {i + 1}", key=f"programming_language_{i}"))

    num_tools = st.number_input("Number of Tools to Add", min_value=0, step=1)
    for i in range(num_tools):
        user_data["Tools"].append(st.text_input(f"Tool {i + 1}", key=f"tool_{i}"))

    if st.button("Save Data"):
        with open("user_data.json", "w") as json_file:
            json.dump(user_data, json_file)
        st.success("Data saved successfully!")

if st.session_state['load_data']:
    st.title("Load Data and Generate Templates")
    try:
        with open("user_data.json", "r") as json_file:
            user_data = json.load(json_file)
        st.success("Data loaded successfully!")
        st.write(user_data)
        if st.button("Generate Resume"):
            temp1(user_data)
        if st.button("Generate Portfolio"):
            temp2(user_data)
    except FileNotFoundError:
        st.error("No saved data found. Please save data first.")

if temp_button1 and not st.session_state['temp1']:
    st.session_state['temp1'] = True
    st.session_state['temp2'] = False
    temp1()
elif temp_button2 and not st.session_state['temp2']:
    st.session_state['temp2'] = True
    st.session_state['temp1'] = False
    temp2()
elif st.session_state['temp1']:
    temp1()
elif st.session_state['temp2']:
    temp2()
