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