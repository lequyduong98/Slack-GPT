# Slack-GPT

- Slack + Open AI chat GPT integration with flask

# Setup slack

- Create slack bot
- Seting for Event Subcription

# Setup Flask

- Install requirement.txt

    ``` pip install -r requirement.txt ```
- Run flask 
    ``` ./start.sh ```
- Flask will run at port 3000

# Slack for Event Subcription auth.

- Best way is put Flask to run in a VPS or any host that slack can sent direct Post request to (Public IP, URL)
- Another way is using Ngrok to get public url.
- Put that url to slack Event Subcription to complete slack config. 
