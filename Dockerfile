FROM python:3.9
WORKDIR /usr/src/app
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy
COPY .env src/ageroller.py ./
CMD [ "pipenv", "run", "python", "./ageroller.py" ]
