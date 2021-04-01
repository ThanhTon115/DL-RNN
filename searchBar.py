from flask import Flask,render_template
app = Flask(__name__)
# @app.route('/printA')
def printA():
    print("a")
# import requests
# url = "http://127.0.0.1:5000/printA"
# requests.post(url)


@app.route('/change', methods=['GET'])
def change():
    if request.method == 'GET':
        print(1)
        message = {'greeting':'Hello from Flask!'}
        return printA()
        # return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print("request.get_json()")  # parse as JSON
        return 'Sucesss', 200


@app.route('/')
def main():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()