from flask import Flask, render_template, request
import run_google_search as gs
import openai_summary as ai
import os

app = Flask(__name__, template_folder=os.path.abspath("./templates"))

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
# @app.route("/", methods=['GET', 'POST'])
# def index():
#     summary = ""
#     if request.method == 'POST':
#         question = request.form['question']
#         summary = ai.summary(question)

#     return render_template('index.html', summary=summary)

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     return """
#     <h1>Test</h1>
#     <form action="/" method="post">
#         <label for="test">Test Textarea:</label>
#         <textarea id="test" name="test" rows="4" cols="50"></textarea>
#         <br>
#         <input type="submit" value="Submit">
#     </form>
#     """

if __name__ == '__main__':
    app.run(debug=True)