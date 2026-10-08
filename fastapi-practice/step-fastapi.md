Install the FastAPI Package

# create an isolated virtual environment just for this subfolder
python -m venv venv

# activate it
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# install fastapi + uvicorn only in this venv
pip install fastapi uvicorn

pip install -r requirements.txt 



Entry Point main.py