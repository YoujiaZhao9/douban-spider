from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    keyword = request.args.get("q")

    df = pd.read_csv("movies.csv")

    if keyword:
        df = df[df["title"].str.contains(keyword, na=False)]

    movies = df.to_dict(orient="records")

    return render_template("index.html", movies=movies, keyword=keyword)

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))