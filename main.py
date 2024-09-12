from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Welcome to the website of Greg pedersen"

if __name__ == "__main__":
  app.run()


#Set up my heroku account with this function that points to my web domain 
#Set this up so that the output here points to the web domain that I currently own.
