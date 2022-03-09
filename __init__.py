from flask import Flask
import bus_test

app = Flask(__name__)

@app.route("/")
def home():
    return bus_test.main()

if __name__ == "__main__":
  app.run()
