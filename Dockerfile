FROM python:2.7.13

# Pull newest version of git repo
run git clone https://github.com/jackdoesdata/pipelineTutorial.git

# Make directory for Docker
run mkdir ca_docker

# Copy current directory and move to ca_docker
copy . /ca_docker/

# Define working directory
workdir /ca_docker

run pip install --upgrade pip --upgrade oauth2client pandas mysql client sqlalchemy gspread

CMD ["python", "./gSheetAPI.py"]
