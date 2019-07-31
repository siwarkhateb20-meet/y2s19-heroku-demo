from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favo_food  = ["lobster", "spaghetti", "sushi"] 

	return render_template("index.html",
    	favo_food=favo_food,
		opposite_day=True)

if __name__ == '__main__':
	app.run(debug = True)
