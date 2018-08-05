from flask import Flask, request, jsonify

app = Flask(__name__)


models = [{'name': 'LFD'}, {'name': 'hoteltv'}, {'name': 'LED'}]
@app.route('/', methods =['GET'])
def test():
    return jsonify({'message': 'B2B Works'})


@app.route('/mode',methods=['GET'])
def mode():
    return jsonify({'B2B Busniess': models})

@app.route('/mode/<string:name>',methods=['GET'])
def ret(name):
    if ( name == 'LFD'):
        return jsonify({'name': 'LFD'})
    else:
        return jsonify({'NO Information': 'No value'})

#PUT Method ro add lauguage i dictionary's

@app.route('/mode',methods=['POST'])
def updatevalue():
    modelupdate = {'name': request.json['name']}
    models.append(modelupdate)
    return jsonify({'Models Info': models})


if __name__ == '__main__':
    app.run(debug=True, port=8080) #debug mode