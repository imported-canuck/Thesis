# Virtual Environments (Windows)

## What is a Virtual Environment
A virtual environment is a self-contained directory that provides an isolated environment for Python projects. You can set the Python version to be a different one from the global/main Python, and install different libraries (and their versions) within it. Functionally, it's like a mini-Python with potentially different libraries that can be called upon instead of the main Python. 

## How to create a Virtual Environment
First, choose a Python interpreter (must be downloaded on your machine, can check with ```py -0p```), ie. Python 3.11  
cd into the directory where you want to build the virtual environment  
In PowerShell (or any terminal), call (where "name" is the name of the venv):  
```
py -3.11 -m venv name
```
The virtual environment has now been created. You can then install dependencies (libraries) manually, or by reading off a requirements text file as such:
```
pip install --upgrade pip
pip install -r requirements.txt
```
Make sure that you're in the virtual environment before installing dependencies. 

## How to enter a Virtual environment
Make sure that you're in the same working directory as the virtual environment. Enter the virtual environment "name" with:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\name\Scripts\Activate.ps1
```
To exit the virtual environment:
```
deactivate
```

## How to delete a virtual environment
Deleting a virtual environment eliminates it for good. You can exit it instead. To delete it:
```
Remove-Item -Recurse -Force .\name
```
