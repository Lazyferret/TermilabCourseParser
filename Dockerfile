FROM selenium/standalone-chrome:latest
RUN sudo apt-get -y update -qy
RUN sudo apt-get -y upgrade -qy
RUN sudo apt-get install -qy python3
RUN sudo apt-get install -qy python3-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]