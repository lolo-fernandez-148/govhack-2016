from flask import Flask
from flask import jsonify
from flaskext.mysql import MySQL
from flask.json import JSONEncoder
from decimal import Decimal
from flask import request


class CustomJSONEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return super(CustomJSONEncoder, self).default(obj)


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pinnacle'
app.config['MYSQL_DATABASE_DB'] = 'pinnacle'
app.config['MYSQL_DATABASE_HOST'] = '0.0.0.0'
mysql.init_app(app)


app.json_encoder = CustomJSONEncoder

@app.route("/")
def hello():
    return "Welcome To Education Hub!"

@app.route("/api/courses")
def fetchAllCourses():
	searchIds = request.args.get('ids')
	print(searchIds)
 	return "All"

@app.route("/api/courses/<courseId>")
def fetchCourse(courseId):
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM pinnacle.cricos_courses where CRICOS_COURSE_ID = '" + courseId + "'")
	data = cursor.fetchone()
	if data is None:
 		return jsonify({})
	else:
 		return jsonify(data)


if __name__ == "__main__":
    port = 5000
    app.run(host='0.0.0.0', port=port)
