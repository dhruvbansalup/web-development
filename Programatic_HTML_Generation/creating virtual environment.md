# Creating Virtual Environment
python -m venv .virtualPy-env 

# Activate Virtual Environment
source .virtualPy-env/bin/activate

# installing packages
pip install -r requirements.txt

# Creating requirements.txt
pip freeze > requirements.txt