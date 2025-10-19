from flask import Flask, render_template, request
from autocorrect import correct_spelling

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_text = ''
    original_text = ''
    if request.method == 'POST':
        original_text = request.form['text']
        corrected_text = correct_spelling(original_text)
    return render_template('index.html', corrected=corrected_text, original=original_text)

if __name__ == '__main__':
    app.run(debug=True)
