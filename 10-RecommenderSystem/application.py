from flask import Flask
from recomm import user_movie_ratings
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("main.html",
    title="MOVIE RECOMMENDER")

@app.route("/recommendations")
def recommender_page():

    html_form_data = dict(request.args)

    ratings = user_movie_ratings(html_form_data)

    print(html_form_data)

    return render_template ('recommendations.html',
                                movies = ratings)

if __name__ == "__main__":
    app.run(debug=True, port=5000)