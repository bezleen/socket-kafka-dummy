# Run the server 
OPTION 1: run with docker
```
docker-compose up -d --build
```
OPTION2: run 1 thread with python (first time)
```
virtualenv .venv -p python3.8
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py run
```
in the second time you just need to run it with 
```
python3 manage.py run
```
The server will run on port 5000 or 7012
# SETTING
1. Set up the topic that you want this server to listen from kafka in src/constants.py -> TOPIC_DUMMY
2. Set up your kafka URL in .env
3. Put your code in src/events/dummy.py and src/controllers/dummy.py (optional)
# Listen event
Listen event "message" from the frontend