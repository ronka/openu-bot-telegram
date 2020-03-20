# OpenU-Bot

OpenU-Bot for getting group links. 

#### Setting up the project

- get bot api key from BotFather
- setup environment variables
- install required modules `pip install -r requirements.txt`
- run the bot `python openu-bot.py`

#### Push to heroku

`git push heroku master`

#### Running the environment

`. ./<env_name>/Scripts/activate` 


#### environment variables

- `TOKEN_API` - Telegram bot API key
- `API_LINK` - API URL to get group links
- `API_COURSE` - API URL to serve courses
- `ENV` - Set `local` to run locally
