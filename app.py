from flask import Flask,jsonify,request,render_template


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return jsonify({'message':'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)