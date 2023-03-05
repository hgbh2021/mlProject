from setuptools import find_packages, setup
from typing import List

cst= "-e ."
def get_requirements(file_path:str)->List[str]:

    requiremets=[]
    with open( file_path) as file_obj:
        requiremets= file_obj.readlines()
        requiremets= [req.replace("\n", "") for req in requiremets ]
        if cst in requiremets:
            requiremets.remove( cst)
    return requiremets

setup(
    name='mlProject',
    version='0.0.1',
    author= 'Hemant Gaur',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt'),

)