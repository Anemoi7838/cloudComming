from flask import Flask,render_template,request
import numpy as np
import app.modules.get as get
import app.modules.calc as calc
import app.modules.judge as judge
import app.modules.conposite as conposite

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")
@app.route("/result",methods=["GET","POST"])
def result():
    if (request.method == "POST"):
        lon = float(request.form.get('lon'))
        lat = float(request.form.get('lat'))
        if(lon == '' or lat == ''):
            return render_template("index.html")
        print(lon,lat)
        plon,plat,ulon,ulat=calc.imagePosition(lon,lat)
        get.images(ulon,ulat)
        x,y=calc.xy(lon,lat,plon,plat)
        print(x,y)
        judgelist=judge.rain(x,y)
        text=0
        for jd in judgelist:
            if jd == "降水なし":
                continue
            else:
                text=1
                break
        #conposite.gsi()
        #conposite.border()
        conposite.surf()
        time = get.date("display")
        conposite.cnpst(lon,lat,plon,plat,time)
        return render_template("result.html",lon=lon,lat=lat,times=time,judges=judgelist,text=text)  


if __name__ == "__main__":
    app.run(debug=True)