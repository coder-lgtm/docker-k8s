FROM python:3.6-alpine
WORKDIR /project
ADD . /project
RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ["python", "weather_cock.py"]
