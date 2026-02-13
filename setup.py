from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from file 
            lines=file.readlines()
            for line in lines:
                # remove leading and trailing whitespace characters
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst
print(get_requirements())

# setup function is used to specify the details of the package and its dependencies
setup(
    name='NetworkSecurity',
    version='0.1',
    author='Vaibhav',
    packages=find_packages(),
    install_requires=get_requirements()
)