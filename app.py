from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'welcome to my watchlist'