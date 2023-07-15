from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def add_p():
    a=10
    b=20
    return str(a+b)

@app.route('/pars')
def add_get():
    a = request.args.get("a")
    b=request.args.get("b")
    return str(int(a)+ int(b))
# URL to run = http://127.0.0.1:5000/pars?a=10&b=20

# @app.route('/', methods=['POST'])
# def add():
#     a=request.form["a"]
#     b=request.form["b"]
#     c=request.form["c"]
#     return str(int(a)+int(b)+int(c))

if __name__ == '__main__':
    app.run(port=7000)

