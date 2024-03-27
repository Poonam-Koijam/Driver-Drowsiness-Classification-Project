import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "CNNClassifier"

list_of_files = [
    ".github/workflows/ .gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    #create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # then create file -->
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.inof(f"{filename} is already exists")


        