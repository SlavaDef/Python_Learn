from flask import Flask
import datetime
app = Flask(__name__)
@app.route("/")
def hello() -> str:
    return  str(datetime.datetime.now())

app.run()

#"Hello World! from Flask_22!",