from flask import Flask , render_template
app=Flask(__name__)

@app.route("/index")
def index ():
    return render_template('index.html')
@app.route("/port")
def port() :
    return render_template('portfolio-details.html')
app.run(debug=True)
