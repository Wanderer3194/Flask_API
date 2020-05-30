from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/add',methods=["POST"])
def add_num():
    #get x,y from the posted data
    dataDict=request.get_json()

    if "y" not in dataDict:
        return "error",305
    x=dataDict["x"]
    y=dataDict["y"]

    z=x+y
    retJson = {
        "z":z

    }
    return jsonify(retJson),200


@app.route('/bye')
def bye():
    #prepare a response for the request that came to /bye
    c=2*23
    s=str(c)

    retJson ={
        'Name':'Elfarouk',
        'Age': 22,
        "phones":[
            {
                "phoneName":"Iphone8",
                "phoneNumber": 12134
            },
            {
                "phoneName":"oneplus",
                "phoneNumber": 987654
            }
        ]

    }

    return jsonify(retJson)

if __name__== "__main__":
    app.run(debug=True)
