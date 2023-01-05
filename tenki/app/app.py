from flask import Flask,render_template,request
import app.modules.get as get

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")
@app.route("/result",methods=["GET"])
def result():
    get.images()
    lat,lon = get.gps()
    return render_template("result.html",lat=lat,lon=lon)

if __name__ == "__main__":
    app.run(debug=True)