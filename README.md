# AI-assistant

## Discord Bot 

### Docker setup 
If you want a quick and easy start, this is the guide with docker:
- What you need to have installed:
    - [Docker](www.docker.com)  
    - [NPM](www.npm.com) 
- Step by step guide:
    1. `$ git clone git@github.com:United-AI/AI-assistant.git`
    2. `$ git checkout DiscordDev` 
    3. `$ cd DiscordBot` 
    4. `$ npm install` 
    5. `$ docker run -dp 3000:3000 -w /DiscordBot -v "$(pwd):/DiscordBot" --name discord-bot maximilianvh/unitedaibot:discordbot-prod`

### Normal setup 
If you don't want to learn or install docker, this is how it is done without:
- What you need to have installed:
    - [NPM](www.npm.com) 
- Step by step guide:
    1. `$ git clone git@github.com:United-AI/AI-assistant.git`
    2. `$ git checkout DiscordDev` 
    3. `$ cd DiscordBot` 
    4. `$ npm install` 
    5. `$ node src/main.js`

### How to contribute 
If you decide to contribute to the discord bot, then please make either a pull request or create a separate branch and inform your project leader.
