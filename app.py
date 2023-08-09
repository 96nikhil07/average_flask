from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/success/<int:score>')
def success(score):
    return "Student is passed with" +str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Student is failed with " +str(score)

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        results=""
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        
        
        return render_template('calculate.html',average_marks=average_marks)
        
        #return render_template('result.html',average_marks=average_marks)
    

if __name__=='__main__':
    app.run(debug=True)