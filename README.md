# color-flask

A simple Flask Color API

## Running locally
Run the following commands to run a local Flask Application for testing purposes:
```
virtualenv venv -p python3.8
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then, you can
```
POST http://127.0.0.1:5000/
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