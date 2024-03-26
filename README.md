# flask-base64encode

Simple Flask Web App: base64 Encoding

## Screenshot Sample
<p align="center">
<img src="./static/demo-image.png" width="400" />


## Prerequisites
```
git

pipenv
```


## How-To with Pipenv 

```
$ pipenv install

$ pipenv shell


$ flask run                                                                
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## How-To with Docker

```
## view/edit Dockerfile

## build image
docker build -t flask_base64encode .

# run container
docker container run --name flask_base64encode --detach --publish 5000:5000 flask_base64encode:latest
```

```
## access container
curl http://127.0.0.1:5000

```

```
## teardown container
docker container rm -f $(docker container ls -aq -f name=flask_base64encode) 

## teardown image
docker image rm -f $(docker image ls -aq -f reference='flask_base64encode*')

```
 

