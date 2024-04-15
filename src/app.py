from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/', methods=['GET'])
def compute():
    name = request.args.get('name')
    var_first = request.args.get('var_first')
    var_second = request.args.get('var_second')

    if not name or not var_first or not var_second:
        return jsonify({'Error': 'Missing parameters'}), 400

    try:
        var_first = float(var_first)
        var_second = float(var_second)
    except ValueError:
        return jsonify({'Error': 'Invalid number format'}), 400

    response = {
        'name': name,
        'addition': var_first + var_second,
        'subtraction': var_first - var_second,
        'multiplication': var_first * var_second,
        'division': var_first / var_second if var_second != 0 else 'undefined'
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
