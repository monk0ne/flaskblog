from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '0961691511722547'

if __name__ == '__main__':
	app.run()
