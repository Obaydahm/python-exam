from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def showchart(): 
    return render_template('temp.html')

if __name__ == '__main__':
    app.run()