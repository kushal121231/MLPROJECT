## used to package and distribute the project as a package.
from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
    ## this function will return the list of requirements
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements if req.strip()]
    return requirements
setup(
    name="MLPROJECT",
    version="0.1.0",
    author="KUSHAL NAGANABOINA",
    author_email="kushalnaganaboina3@gmail.com",
    description="A machine learning project package",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)