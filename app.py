from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to UAV Controller'


@app.route('/date')
def date():
    output = subprocess.check_output(["date"], universal_newlines=True)
    return output


@app.route('/call')
def call():
    with open('out.txt', 'w+') as output:
        subprocess.call(["chmod", "755", "example.sh"])
        subprocess.call(["/bin/bash", "example.sh"], stdout=output)
    return 'Executed successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
