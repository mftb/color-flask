# color-flask

A simple Flask Color API

## Running locally
Run the following commands to run a local the Flask Color API:
```
virtualenv venv -p python3.8
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then, you can request it:
```
curl --location --request GET 'http://0.0.0.0:5000' \
--header 'Content-Type: application/json'
```

```
curl --location --request GET 'http://0.0.0.0:5000/red' \
--header 'Content-Type: application/json'
```

```
curl --location --request POST 'http://0.0.0.0:5000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "color": "fuchsia",
    "value": "#fab"
}'
```

## Running tests:
```
virtualenv venv -p python3.8
source venv/bin/activate
pip install -r requirements.txt
pytest
```

## Running test coverage report:
```
virtualenv venv -p python3.8
source venv/bin/activate
pip install -r requirements.txt
pytest --cov
```

# Running with podman

You can run the application with podman with the following commands:

```
podman build -t color-flask .
podman run -it -p 5000:5000 color-flask:latest
```

# Deploying with podman

You can deploy the application with podman pushing it to a container registry also using podman:

```
podman push color-flask:latest
```
