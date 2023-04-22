import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

'''
This script will create the required structure for the project
'''


PROJECT_NAME : str = "dogBreed"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
]


for file_path in list_of_files:
    file_path = Path(file_path)

    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating dir : {file_dir} for file : {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        logging.info(f"Creating an empty file named : {file_name} in the dir named : {file_dir}")
        with open(file_path, "w") as f:
            pass    # To create an empty file

    else:
        logging.info("An non-empty file {file_path} already exists.")