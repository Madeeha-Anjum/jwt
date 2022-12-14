FROM python:3.10-slim-bullseye

WORKDIR /usr/app/

# Copy requirements.txt to app directory from current directory
COPY requirements.txt requirements.txt

# Install requirements from requirements.txt 

RUN pip3 install -r requirements.txt


# copy the files into the app directoey 
COPY ./app .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 