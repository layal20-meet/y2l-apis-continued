import requests, json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
 	image_url = request.form['url-input']
	headers = {'Authorization': 'Key 1054d6f8bd544e648c9f291b49e30885'}
	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
	data ={"inputs": [
			{
				"data": {
				"image": {
				"url": image_url
				}
			}
		}
		]}

	# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))
	parsed= json.loads(response.content)
	return render_template('home.html', results=parsed["outputs"][0]["data"]["concepts"])

if __name__ == '__main__':
    app.run(debug=True)