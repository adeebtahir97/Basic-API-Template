import pickle
import json
import flask
from flask import jsonify, Flask
from flask import request, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def testing():
    return render_template('inputPage.html')


@app.route('/predict', methods=["POST"])
def predict():

    #get the data in json sent as input to this API
    content = request.get_json()
    inputVal = int(content["InputVal"]) #Explicitly keep it as int(coz in your case the inputs are numeric...)    


    #Load the models
    with open("testModels.pickle","rb") as pickle_in:
        model_l = pickle.load(pickle_in)

    #Perform prediction
    prediction1 = model_l[0].predict(inputVal)
    prediction2 = model_l[1].predict(inputVal)

    #Do the aggregation of predictions
    pred = prediction1*0.3 + prediction2*0.4 #I've just put random weights..change them to your needs
    print(pred) #This is just to see the prediction on the terminal

    #Update the database with prediction
    try:
        conn = mysql.connector.connect(host="localhost",user="root",passwd="root")
        #set database you want to use
        conn.execute("use project")
        #update table
        conn.execute("(put your sql table update here).....")
    except:
        #return appropriate json response
        return '{"response":"Can\'t establish connection to database"}'


    #Return the prediction in JSON format
    return '{"response":"'+pred+'"}'   


if __name__ == '__main__':
    app.run(debug=True, port=4040)
