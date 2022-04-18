FROM python:3.6.12-stretch

RUN pip install --upgrade pip

WORKDIR /main

COPY requirements.txt requirements.txt

RUN apt-get update \
  &&  apt-get install -y apt-transport-https \
  && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && ACCEPT_EULA=Y apt-get install -y msodbcsql17

COPY . .

RUN apt-get update && apt-get install -y unixodbc-dev

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]