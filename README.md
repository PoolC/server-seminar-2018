# Flask Seed Application
## Prerequisites
* Python 3.6+
* virutalenv


## Development
### Setup
```bash
# Set virtual environment.
virtualenv env
source ./env/bin/activate

# Install requirements.
pip install -r requirements.txt
```

### Run
```bash
FLASK_APP=app.py flask run -h 0.0.0.0 --with-threads
```
