from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/flyers')
def flyers():
    # return 'Hi'
    print(request.args)
    # multi_dict = request.args
    # for key in multi_dict:
    #     print multi_dict.get(key)
    #     print multi_dict.getlist(key)
    start = request.args['start']
    end = request.args['end']
    location_id = request.args['location_id']
    return "Start: %s, End: %s, location_id: %s" % (start, end, location_id)


@app.route('/locations', defaults={'location_id': None})
@app.route('/locations/<location_id>')
def locations(location_id):
    if not location_id:
        return 'all'

    return "location_id: %s" % (location_id)
