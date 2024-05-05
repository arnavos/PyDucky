from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "idk"

@app.route('/script.txt')
def serve_script():
    with open('script.txt', 'r') as file:
        script = file.read()
    return script

@app.route('/script.exe')
def serve_exe():
    filename = 'script.exe'
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
