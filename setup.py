from setuptools import find_packages , setup

setup(
    name = "mcqgenrator",
    version = "0.0.1",
    author = "sai_kumar_aalla",
    author_email ="avsaikumar2000@gmail.com",
    install_requires = ["openai" , "langchain" , "streamlit" ,"python-dotenv" ,"pypdf2"] ,
    packages=find_packages()
)