FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /inegi_graphql_api
WORKDIR /inegi_graphql_api
COPY /requeriments.txt /inegi_graphql_api/
RUN pip install -r requeriments.txt
COPY . /inegi_graphql_api/