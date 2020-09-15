from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")
def index ():
    return render_template('index.html')
@app.route("/downloads")
def downloads() :
    return render_template('downloads.html')
app.run(port=100)
