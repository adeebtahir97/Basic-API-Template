import mysql.connector
import pickle
import json
import pandas as pd

if __name__ == '__main__':
    try:
    	conn = mysql.connector.connect(host="localhost",user="root",passwd="root")
    	cursor = conn.cursor()
	except:
    	#return appropriate json response
    	return '{"response":"Can\'t establish connection to database"}'

	#set database you want to use
	conn.execute("use project")

	#get all records into a dataframe
	cursor.execute("select * from YourtableName")
	df = pd.DataFrame(cursor.fetchall())

	#Do your training below 








	#Let your models be in a list 'model_l'
	model_l = [clf1,clf,....]

	#Pickle the models
	pickle_out = open("testModels.pickle","wb")
	pickle.dump(model_l,pickle_out)
	pickle_out.close()
