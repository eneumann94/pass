from flask import Flask, request, jsonify, render_template
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_hash', methods=['POST'])
def generate_hash():
    data = request.get_json()
    senha = data['senha']
    salt = data['salt']
    ctext = senha + salt

    h = hashlib.sha256()
    h.update(ctext.encode('utf8'))
    phash = h.hexdigest()
    phash = phash[:32]

    return jsonify({'phash': phash})

if __name__ == '__main__':
    app.run(debug=True)
