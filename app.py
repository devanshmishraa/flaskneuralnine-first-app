from flask import Flask, request

app = Flask(__name__)

#Dynamic URLS
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/hello")
def hello():
    return "hello world"

#URL processors
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/add/<int:number1>/<int:number2>") #now this route is only for the integers as we have givent the type to the input
def add(number1,number2):
    
    return f"{number1} + {number2} = {number1 + number2}"


# @app.route("/handle_url_params")   #This Flask route:Listens at /handle_url_params, Returns any query parameters passed in the URL, as a string.
# def handle_params():
#     return str(request.args)         #http://localhost:5000/handle_url_params?name=Alice&age=30
#                                     #ImmutableMultiDict([('name', 'Alice'), ('age', '30')])
#                                     #request.args is a MultiDict that contains the query string parameters (i.e. the part after ? in a URL).
#                                     #It’s called "immutable" because Flask won’t let you change it directly.


@app.route("/handle_url_params")
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return "Some parametrs missing"



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5555, debug=True)