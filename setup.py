from setuptools import find_packages, setup
from typing import List
## find_packages -> maps the application folder structure and makes package

HYPEN_E = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This funtion will return the list of requirements.   
    '''
    requirements=[]

    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[r.replace('\n','') for r in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)


    return requirements

setup(
    name='mlproject',
    version=0.0,
    author="zahid",
    author_email='zahidshuvobd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)