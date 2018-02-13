from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.jinja2")

@app.route("/hva")
def what():
    return render_template("what.jinja2")

@app.route("/bivirkninger")
def side_effects():
    return render_template("side_effects.jinja2")

@app.route("/praktisk")
def practical():
    return render_template("practical.jinja2")

@app.route("/nar")
def when():
    return render_template("when.jinja2")

@app.route("/effekt")
def effect():
    return render_template("effect.jinja2")

if __name__ == '__main__':
    app.run(debug=True)
