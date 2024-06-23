from flask import Flask, request, render_template, jsonify
import numpy as np

main = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/convolve', methods=['POST'])
def convolve():
    data = request.get_json()
    signal1 = np.array(data['signal1'])
    signal2 = np.array(data['signal2'])
    result = np.convolve(signal1, signal2).tolist()
    return jsonify(result=result)

if __name__ == '__main__':
    main.run(debug=True)