import flask
from time import sleep

app = flask.Flask("app")

def something_very_slow():
    print("about to do very slow thing")
    sleep(1)
    print("completed very slow thing")


def something_a_bit_slow():
    print("about to do something a bit slow")
    sleep(0.01)
    print("completed something that was a bit slow")


@app.route("/")
def hello():
    something_a_bit_slow()
    something_very_slow()
    return "Hello"
