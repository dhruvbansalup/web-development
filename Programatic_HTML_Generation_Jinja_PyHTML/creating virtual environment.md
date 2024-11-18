# Creating Virtual Environment
python -m venv .virtualPy-env 

# Activate Virtual Environment
<!-- For Linux -->
source .virtualPy-env/bin/activate
<!-- For Windows -->
.virtualPy-env\Scripts\activate

# installing packages
pip install -r requirements.txt

# Creating requirements.txt
pip freeze > requirements.txt