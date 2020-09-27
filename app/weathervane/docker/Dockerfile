FROM python:3.6-alpine
RUN apk --no-cache add curl
WORKDIR /project
ADD . /project
RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ["python", "weather_vane.py"]
