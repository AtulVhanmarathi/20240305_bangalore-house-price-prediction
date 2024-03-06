# this file helps create the required folders and files as generic project template

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ML_LinearRegression"

list_files = [
    ".github/workflows/.gitkeep",
    f"source/{project_name}/__init__.py",
    f"source/{project_name}/components/__init__.py",
    f"source/{project_name}/utils/__init__.py",
    f"source/{project_name}/config/__init__.py",
    f"source/{project_name}/config/configuration.py",
    f"source/{project_name}/pipeline/__init__.py",
    f"source/{project_name}/entity/__init__.py",
    f"source/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/.gitkeep"

]

# we are using Path class from pathlib to convert normal path to windows path automatically
for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # split function is returing two variables

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # first I am checking whether the file exists, and I am also checking whether file contains some code / text
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f"File {filename} already exists")
