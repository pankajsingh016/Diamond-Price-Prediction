from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirement=file_obj.readline()
        requirements=[ req.replace("\n","") for req in requirement]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Pankaj',
    author_email='pankajsinghkanyal016@gmail.com',
    installed_requires=get_requirements('requirements.txt'),
    packages=find_packages() 
)




