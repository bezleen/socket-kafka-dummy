# Run the server 
```
docker-compose up -d --build
```
# SETTING
1. Set up the topic that you want this server to listen from kafka in src/constants.py -> TOPIC_DUMMY
2. Set up your kafka URL in .env
3. Put your code in src/events/dummy.py and src/controllers/dummy.py (optional)
# Listen event
Listen event "message" from the frontend