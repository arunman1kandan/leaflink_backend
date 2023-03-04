from flask import Flask,request
from prediction import *
app = Flask(__name__)

@app.route("/getPlantDisease",methods=["POST"])
def getPlantDiseaseData():
	if(request.method=="POST"):
		imageUrl = request.get_json()["imageURL"]
		print(fetchResponse(imageUrl))
		return fetchResponse(imageUrl)
	else:
		return f"{request.method} will not work";

if __name__ == '__main__':
	app.run(debug=True)

