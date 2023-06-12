from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        numbers = data['numbers']
        if isinstance(numbers, list) and all(isinstance(num, (int, float)) for num in numbers):
            result = sum(numbers)
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Invalid input. The "numbers" field should be a list of numbers.'}), 400
    except KeyError:
        return jsonify({'error': 'Invalid input. Missing "numbers" field.'}), 400


@app.route('/concatenate', methods=['POST'])
def concatenate_strings():
    try:
        data = request.get_json()
        string1 = data['string1']
        string2 = data['string2']
        if isinstance(string1, str) and isinstance(string2, str):
            result = string1 + string2
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Invalid input. The "string1" and "string2" fields should be strings.'}), 400
    except KeyError:
        return jsonify({'error': 'Invalid input. Missing "string1" or "string2" field.'}), 400


if __name__ == '__main__':
    app.run()
