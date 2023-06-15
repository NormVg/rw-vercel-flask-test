from flask import Flask ,request,jsonify,send_file,url_for,render_template
from plugs.fury_carter import ask_fury
from plugs.tts import gen
from plugs.listen import reco
import requests


aud_file  = []
app = Flask(__name__)


@app.route("/")
def index():
    return "<-- fury app development server -->"

@app.route("/fury-audio")
def send_audio():
    file_ = aud_file[0]
    return send_file(file_)

@app.route("/fury-res",methods=["GET","POST"])
def fury_res():
    command = request.args.get("command")
    user = request.args.get("user")
    key = request.args.get("key")
    if not user : user = "Norm"
    if not key : key = None
    print(command,user)
    response,forse = ask_fury(command, user=user, key=None)

    aud = gen(response)
    aud_file.clear()
    aud_file.append(aud)
    
    data = {
        "command":command,
        "reply":response,
        "audio": f'{request.host_url}fury-audio'
        }
    return jsonify(data)

@app.route("/audiostt",methods=["GET","POST"])
def helllomy():
    if request.method == 'POST':
        # return ""
        file = request.files['file']
        file.save("main.wav")

        text_data = reco("main.wav")
        
        data = {
            "text":text_data
            }
        print(data)
        return jsonify(data)
    return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
      </form>
      '''


@app.route("/fury",methods=["GET","POST"])
def fury():
    
    if request.method == "POST":
        file = request.files['file']
        # user = request.json.get("user")

        user = "Boss"
        file.save("main.wav")
        text_data = reco("main.wav")
        
        reply = requests.get(request.host_url+"fury-res?command="+text_data+"&user="+user).json()
        
        # reply = {"hh":"hhsd"}
        return jsonify(reply)
    
    else : return "200"

@app.route("/workspace")
def work_space():
    return render_template("index.html")

if __name__ == '__main__':

    app.run(debug=True)