from flask import Flask,render_template,request,url_for
import numpy as np
import pickle
app = Flask(__name__)

model=pickle.load(open('Model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/#',methods=['POST','GET'])
def predict():
    preg=request.form['preg']
    glucose=request.form['glucose']
    bp=request.form['bp']
    st=request.form['st']
    insulin=request.form['insulin']
    bmi=request.form['bmi']
    dbd=request.form['dbd']
    age=request.form['age']
    ppa=int(preg)/int(age)
    stbmi=float(st)/float(bmi)
    gpa=float(glucose)/float(age)
    gwi=float(glucose)/float(insulin)
    output=model.predict(np.array([[preg,glucose,bp,st,insulin,bmi,dbd,age,ppa,stbmi,gpa,gwi]]))
    if output[0]==0:
        return render_template("no.html")
    else:
        return render_template("yes.html")




if __name__ == '__main__':
    app.run()