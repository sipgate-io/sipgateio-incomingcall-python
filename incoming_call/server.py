import flask
import json

app = flask.Flask(__name__)


@app.route('/', methods=["POST"])
def receive_new_call():

    request_data = flask.request.form.to_dict()
    json_data = json.dumps(request_data, indent=2)
    print(json_data)

    return '', 204
