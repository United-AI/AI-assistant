# AI-assistant

## Discord Bot 

### Docker setup 
If you want a quick and easy start, this is the guide with docker:
- What you need to have installed:
    - [Docker](https://www.docker.com)  
    - [NPM](https://www.npm.com) 
- Step by step guide:
    1. `$ git clone git@github.com:United-AI/AI-assistant.git`
    2. `$ git checkout DiscordDev` 
    3. `$ cd DiscordBot` 
    4. `$ npm install` 
    5. `$ docker run -dp 3000:3000 -w /DiscordBot -v "$(pwd):/DiscordBot" --name discord-bot maximilianvh/unitedaibot:discordbot-prod`

### Normal setup 
If you don't want to learn or install docker, this is how it is done without:
- What you need to have installed:
    - [NPM](https://www.npm.com) 
- Step by step guide:
    1. `$ git clone git@github.com:United-AI/AI-assistant.git`
    2. `$ git checkout DiscordDev` 
    3. `$ cd DiscordBot` 
    4. `$ npm install` 
    5. `$ node src/main.js`

### How to contribute 
If you cloned this repository and followed the setup, you will most likely get an error message similar to this:
`Error: Cannot find module './config.json'`
This is caused by the fact that this file contains the access kays to the discord bot and with it anyone could use our bot.
To avoid someone stealing our bot or abusing it we have decided on following solution:
- If you are part of our club "United AI" you can ask your team leader and he will hand you the correct `config.json` file.
- If you are not a member you won't receive the file and have to create your own bot.
