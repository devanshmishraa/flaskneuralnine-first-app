from flask import Flask, request, make_response

app = Flask(__name__)

#Dynamic URLS
@app.route("/")
def index():   #custom response
    response = make_response("Hello World\n")
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


@app.route("/hello", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return "You have made a GET request\n"
    elif request.method == 'POST':
        return "You have made a POST request\n"
    else:
        return "You will never see this message\n"

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