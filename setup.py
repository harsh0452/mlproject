from setuptools import find_packages,setup
from typing import List
Hyphen_e_Dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] ##replace is done as \n gets added in reading everyline
        if Hyphen_e_Dot in requirements:
            requirements.remove(Hyphen_e_Dot)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Harsh',
    author_email='harsh0452@gmail.com',
    packages=find_packages(), ##  searches in how many folders we have __init__.py ,it considers that as package and builds it
    install_requires= get_requirements('requirements.txt')  ## creating a function to read as 100's of packages is not feasible to wite['pandas','numpy','seaborn']

)