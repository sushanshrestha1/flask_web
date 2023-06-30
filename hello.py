from flask import Flask,render_template




#Create a flask instance
app=Flask(__name__)

#Create a route decorator

@app.route('/')


def index():
    first_name="joshn"
    stuff="tih is <strong>bold</strong> text"
    box=['me','she',14]
    return render_template("index.html",first_name=first_name,stuff=stuff,bigbox=box)

#localhost:5000/user/John 

@app.route('/user')

def user():
    name="sushan"
    return render_template("user.html",user_name=name)


#crete custom error pages

# invalid url
@app.errorhandler(404)


def page_not_found(e):
    return render_template("404.html"),404


#internal error
@app.errorhandler(500)


def page_not_found(e):
    return render_template("404.html"),500

