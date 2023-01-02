import streamlit as st
from PIL import Image
from pathlib import Path

c_dr = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = c_dr/"styles"/"main.css"
resume = c_dr/"assets"/"resume.pdf"
pp = c_dr/"assets"/"pic.png"

img = Image.open(pp)
st.set_page_config(
    page_title = "Resume | Jayanth Telu",
    page_icon = img,
    layout = 'wide',
)

links = {
    "Github": "https://github.com/jayanthtelu",
    "LinkedIn" : "https://www.linkedin.com/in/jayanth-telu-033067172/",
}

with open(css_file) as css_f:
    st.markdown("<style>{}</style>".format(css_f.read()), unsafe_allow_html=True)

with open(resume, "rb") as resume_pdf:
    pdf_resume = resume_pdf.read()

#--- Header Section ------

col1, mid, col2 = st.columns([1,1,5])
#left, right = st.columns(2, gap="small")
with col1:
    st.image(img, width = 300)

with col2: 
    st.title("Jayanth Telu")
    st.write("""
Graduate Student at UNC Charlotte with hands-on expertise in dealing with data leveraged via technical experience from different industries at major corporations and an Azure certified Data Engineer Associate
    """)
    st.download_button(
        label="📥 Download Resume",
        data=pdf_resume,
        file_name=resume.name,
        mime="application/octet-stream",
    )
    st.write("📧 jayanth.telu99@gmail.com")
#(len(links), gap="small")
st.write("#")
cols = st.columns(2)
for index, (platform, link) in enumerate(links.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("👨‍🎓 Education")

# ---- Master's ------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("<h style='text-align: justify; font-weight: bold; color: white;'>Master of Science in Computer Science</h>", unsafe_allow_html=True)
with col2:
     st.markdown("<h style='text-align: justify; color: white;'>Expected May 2023</h>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("<h style='text-align: justify; color: white;'>🏫 University of North Carolina at Charlotte</h>", unsafe_allow_html=True)
with col2:
     st.markdown("<h style='text-align: justify; color: white;'>GPA 4.0/4.0</h>", unsafe_allow_html=True)

st.write("**Relevant Coursework**: Big Data Analytics, Visual Analytics, Algorithms and Data structures, Database Systems, Software System Design and Implementation, Intelligent Systems")

# ---- Bachelor's ---- 
col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("<h style='text-align: justify; font-weight: bold; color: white;'>Bachelor's in Computer Science</h>", unsafe_allow_html=True)
with col2:
     st.markdown("<h style='text-align: justify; color: white;'>June 2020</h>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("<h style='text-align: justify; color: white;'>🏫 Gitam Deemed to be University, India</h>", unsafe_allow_html=True)
with col2:
     st.markdown("<h style='text-align: justify; color: white;'>GPA 3.5/4.0</h>", unsafe_allow_html=True)

st.write("**Relevant Coursework**: Programming Concepts using C, C++ and Java, Web Development using HTML, CSS and JavaScript, Design and Analysis of Algorithms, Data mining, Machine Learning. ")

#st.write("#")
st.subheader("🔧 Techincal Skills")
st.write("""
- 🖥️ Programming Languages: C, Python, Java
- 📃 Web Technologies : HTML, CSS
- 💾 Databases : MySQL, NoSQL
- 📊 BI Tools : Power BI, Tableau, Amazon Quicksight
- 📚 Packages : Pandas, Numpy , matplotlib, seaborn, beautifulsoup. 
- 🧑‍💻 Framework : Streamlit. 
- ☁️ Cloud Technologies : Azure, AWS. 
""")

#---- Work Experience ----- 
st.subheader("💼 Work Experience")
st.write(" 🚧**Teaching Assistant | UNC at Charlotte** ")
st.write("Aug 2022 - Present")
st.write(""" 
- Teaching Assistant for Database Design and Implementation (ITCS 3160) and Database Systems (ITCS6160)
- Mentored 90 undergraduate and 75 graduate students with coursework, assignments, grading and projects. """)

st.write(" 🚧**Associate Data Engineer | PriceWaterhouseCoopers, India**")
st.write(" May 2021 - Dec 2021")
st.write("""
- Ingested, explored, and cleaned data using Azure Synapse Analytics workspace.
- Built ETL pipelines using Azure data factory. 
- Used Azure data lake storage services to store the transformed data. 
- Applied transformations on data using Azure data bricks. 
- Used Power-BI to generate reports and dashboards for weekly meetings. 
"""
)

st.write(" 🚧**Data Analyst Intern | Mu Sigma, India** ")
st.write(" Sep 2020 - Dec 2020")
st.write("""
- Performed data analysis to identify the trends on customer purchase patterns. 
- Designed dashboards and reports using Tableau.
- Performed Data cleaning and transformations using various packages in python on large datasets. 
- Designed few hypotheses and provided the insights on customer behaviors that helped to reduce the customer churn rate.  
""")

st.write("🚧**Software Developer Intern | Tata Consultancy Services**")
st.write(" May 2019 - July 2019")
st.write("""
- Worked as full stack developer in developing an application for patient registration and scheduling appointment. 
- Gained hands-on experience in Java, SQL, HTML and CSS3. 
- For developing the front end, we used angular. For the backend of the application, we used spring boot. The database used is H2DB.
""")

#---- Acedmaic Projects ----
st.subheader("👨‍💻 Academic Projects")
st.write("🚧**Netflix Demographics**")
st.write("""
In this project, I’ve gathered the Netflix datasets from ‘kaggle.com’ and cleaned the data. The data is transformed according to the requirements for exploratory data analysis. Using the transformed datasets, I’ve developed visualizations using Tableau. These visualizations give a clear understanding on the complete datasets. These visualizations are integrated into a webpage using streamlit framework and hosted the webpage on this page. (https://rb.gy/cdhqtl)
""")

st.write("🚧**EDA on COVID-19**")
st.write("In this project we’ve chosen the centralized repository of up-to-date and curated datasets related to the spread and characteristics of the novel corona virus (SARS-CoV-2) and its associated illness, COVID-19. The COVID-19 data lake consists of data from different around the globe from various organizations. From all the available data such as testing data, vaccinations data, hospitals data and about many more events regarding COVID-19 we have chosen the testing data which has up to November 2021. Using this dataset, our main goal is to identify the trends of positive cases of the covid-19 around the country and track the deaths polls of covid-19 in various regions. Also try to forecast the cases of a week ahead using various packages.")

st.write("🚧**Identifying and Predicting Customer Churn**")
st.write(" In this project, I've gathered data sets of a home improvement company and cleaned all the data that is required for exploratory data analysis. After cleaning, I've made some hypothesis that are related to customer churn and their behavior. Then I've did some analysis on the data and got some insights of the data, then converted those insights in visualizations which help to identify the root causes of the problem.")

st.subheader("👨‍🎓 Student Involvements")
st.write("🚧**Computer Society of India (CSI) – GITAM student club**")
st.write("""
***Mentor & Logistics and Sponsorships Team Lead | Nov 2018 - Jan 2020***
- After my tenure in a Leadership role, I mentored my subordinates, helped them to organize and trouble-free conduct of the events 
- Identified sponsor leads and generated funds to the student branch. Coordinated with various verticals and hosted one state level and few district levels events.
""")
st.write("""
***Event Organizer | Dec 2017 - Nov 2018*** 
- Organized various technical events such as AI and IOT, Cyber security and Robotics workshops as part of Hello.MarTin, Ethereal 2.0 and Ethereal. Student Volunteer Aug 2017 - Dec 2017 
- Worked as volunteer for the CSI Andhra Pradesh State Student Convention - APSSC 2017 and organized a technical event named Code-Bounty
""")
