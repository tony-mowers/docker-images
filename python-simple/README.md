# Simple Python Website

This example illustrates how to build a web application within a Docker container. 
It was built using the python [flask](https://flask.palletsprojects.com/en/2.0.x/) 
package.  

## Run on Command Line

```bash
> pip3 install -r requirements.txt
> export FLASK_ENV=development && python3 -m flask run
```

Open your browser to http://localhost:5000

NOTE: ctrl-C will stop the process

## Run in Docker Container

```bash
> docker compose build
> docker compose up
```

Open your browser to http://localhost:5000

NOTE: ctrl-C will stop the process


[markdown guide](https://guides.github.com/features/mastering-markdown/)