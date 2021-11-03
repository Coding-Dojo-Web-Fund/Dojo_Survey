from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def info():
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def user_info():
    print(request.form)
    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['favorite language'] = request.form.get('favorite languages')
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("info.html")

if __name__=="__main__":
    app.run(debug=True)
