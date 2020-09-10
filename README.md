# Docker and Kubernetes Hands-On Workshop for Beginners

This project is a Workshop presented to Women in Technology. **DETAILS TBD**

The Workshop will be presented in a virtual setting.

## Table of Contents  

[Getting Started](https://github.com/coder-lgtm/docker-k8s#getting-started)

[Prerequisites](https://github.com/coder-lgtm/docker-k8s#prerequisites)

[Installation](https://github.com/coder-lgtm/docker-k8s#installation)

[1. Clone this repo](https://github.com/coder-lgtm/docker-k8s#1-clone-this-repo)

[2. Install Homebrew](https://github.com/coder-lgtm/docker-k8s#2-install-homebrew)

[3. Install Python](https://github.com/coder-lgtm/docker-k8s#3-install-python)

[4. Install Pip](https://github.com/coder-lgtm/docker-k8s#4-install-pip)

[5. Install dependency packages Flask and Requests](https://github.com/coder-lgtm/docker-k8s#5-install-dependency-packages-flask-and-requests)

[Launch Your Web Applications!](https://github.com/coder-lgtm/docker-k8s#launch-your-web-applications)

[6. Launch your Hello World web application](https://github.com/coder-lgtm/docker-k8s#6-launch-your-hello-world-web-application)

[7. Launch your Weather API web application](https://github.com/coder-lgtm/docker-k8s#7-launch-your-weather-api-web-application)

[Docker](https://github.com/coder-lgtm/docker-k8s#docker)

[8. Install Docker](https://github.com/coder-lgtm/docker-k8s#8-install-docker)

[9. Install Virtualbox](https://github.com/coder-lgtm/docker-k8s#9-install-virtualbox)

[10. Validate the Docker installation](https://github.com/coder-lgtm/docker-k8s#10-validate-the-docker-installation)

[11. Connect to Docker](https://github.com/coder-lgtm/docker-k8s#11-connect-to-docker)

[12. Check Docker processes](https://github.com/coder-lgtm/docker-k8s#12-check-docker-processes)

[Built With](https://github.com/coder-lgtm/docker-k8s#built-with)

[Authors](https://github.com/coder-lgtm/docker-k8s#authors)



## Getting Started

This project includes sample Python Flask applications and instructions for installing Docker on your local environment.

It is advisable but not mandatory that you have performed these steps beforehand. That way, you can follow along during the workshop to launch your Docker Container locally and later to a public cloud (Google Cloud Platform free tier account).

### Prerequisites

The steps below were executed on Macbooks running MacOS Catalina.


### Installation

#### 1. Clone this repo
```
$ git clone git@github.com:coder-lgtm/docker-k8s.git
$ cd docker-k8s
```

#### 2. Install Homebrew
```
$ ./tools/brew_installation.sh
$ brew update
```

#### 3. Install Python
```
$ brew install python
```

#### 4. Install Pip
```
$ sudo easy_install pip
```

#### 5. Install dependency packages Flask and Requests
```
$ sudo pip install flask
$ pip install requests
```

### Launch Your Web Applications!

#### 6. Launch your Hello World web application
```
$ python ./app/helloworld/hello_world.py 
```

Point your browser to the below URL:
```
http://localhost:5000/
```

The expected response is:
```
Hello World!
```

#### 7. Launch your Weather API web application
```
$ python ./app/weathervane/weather_vane.py
```

Point your browser to the below URL, using the zip code of your choice (we are using the zip code for Redwood City, California):
```
http://localhost:5000/weather?zip=94065
```

The expected response is something like the below (it may be unformatted):
```
{
  "current": {
    "gust_kph": 11.5, 
    "last_updated": "2020-09-06 12:00", 
    "vis_miles": 9.0, 
    "pressure_in": 30.4, 
    "cloud": 0, 
    "precip_mm": 0.0, 
    "is_day": 1, 
    "feelslike_c": 30.0, 
    "condition": {
      "text": "Sunny", 
      "code": 1000, 
      "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png"
    }, 
    "feelslike_f": 85.9, 
    "wind_mph": 0.0, 
    "temp_f": 87.8, 
    "temp_c": 31.0, 
    "last_updated_epoch": 1599418805, 
    "pressure_mb": 1015.0, 
    "vis_km": 16.0, 
    "precip_in": 0.0, 
    "wind_dir": "N", 
    "wind_kph": 0.0, 
    "uv": 8.0, 
    "humidity": 46, 
    "gust_mph": 7.2, 
    "wind_degree": 0
  }, 
  "location": {
    "name": "Redwood City", 
    "country": "USA", 
    "region": "California", 
    "tz_id": "America/Los_Angeles", 
    "lon": -122.25, 
    "lat": 37.53, 
    "localtime_epoch": 1599419443, 
    "localtime": "2020-09-06 12:10"
  }
}
```

### Docker 

#### 8. Install Docker

```
$ brew install docker
$ brew install docker-machine
```

#### 9. Install Virtualbox
```
$ brew cask install virtualbox
```

If your Mac asks you for permission, go to System Preferences -> Security & Privacy -> General. You will see a message like `System software from developer "Oracle America, Inc." was blocked from loading`. Click on the lock in the lower left corner and click Allow, then run `brew cask install virtualbox` again.

#### 10. Validate the Docker installation
Launch the Docker machine named "default":
```
$ docker-machine create --driver virtualbox default
```

Confirm that the Docker machine is running:
```
$ docker-machine ls 
```

The expected output is shown below:
```
TBD
```

#### 11. Connect to Docker

Start the Docker machine if it is not running *TBD details*:
```
$ docker-machine start
```

Connect to the Docker machine *TBD what is docker-machine set to?*:
```
$ docker-machine env eval $(docker-machine env)
```

#### 12. Check Docker processes
```
$ docker ps
```

There should be no running processes and we will launch one during the workshop. The expected output is shown below:
```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```




## Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Docker Engine](https://docs.docker.com/engine/)

## Authors

* [Rutuja Joshi](https://www.linkedin.com/in/rutuja/)
* [Anita Carey](https://www.linkedin.com/in/anitacarey/)




