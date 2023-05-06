from flask import Flask, render_template, request, redirect,session,flash
import pyshorteners

app = Flask(__name__)
app.secret_key = 'my-secret-key'

        
        
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        s = pyshorteners.Shortener()
        x = s.dagd.short(request.form["link"])
        return render_template('index.html',flag = 1,link=x)
    return render_template('index.html',flag = 0)

if __name__ == '__main__':
    app.run(debug=True)