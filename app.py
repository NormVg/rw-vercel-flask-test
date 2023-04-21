from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
  return "200"


@app.route("/show")
def show_data():
  r = open("log.txt", "r")
  return str(r.read())


@app.route("/write")
def write_data():
  t = request.args.get("text")
  r = open("log.txt", "w")
  r.write(t)
  r.close()
  return "201"


@app.route("/dump")
def delete_data():
  r = open("log.txt", "w")
  r.write("")
  r.close()
  return "205 all data dumped"



if __name__ == '__main__':

    app.run()
