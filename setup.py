import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    this function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
__version__ = "0.0.0"

REPO_NAME = "20240305_bangalore-house-price-prediction"
AUTHER_USER_NAME = "AtulVhanmarathi"
SOURCE_REPO = "ML_LinearRegression"
AUTHER_EMAIL = "atul.vhanmarathi@gmail.com"


setuptools.setup(
    name=SOURCE_REPO,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_EMAIL,
    description="This is a linear regression model",
    long_description=long_description,
    long_description_context="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"source"},
    # packages=setuptools.find_packages(where="source"),
    install_requires=get_requirements('requirements.txt'),
)
