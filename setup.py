from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirments(file_path:str) -> List[str]:
    '''this function will return the list of requirmrnt '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readline()
        requirments=[req.replace('\n','') for req in requirments]
        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)


setup(
name = 'mlproject',
version='0.0.1',
author='Dr. Stark',
author_email='thakurds03763@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirement.txt')



)