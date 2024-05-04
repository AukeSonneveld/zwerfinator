from flask import Flask

app = Flask(__name__)

@app.route("/")
def classify_image():
    # Do something 
    return "Hello, World!"



# To run the server, run $ flask run
# Will open on port 5000
if __name__ == "__main__":
    app.run(debug=True)