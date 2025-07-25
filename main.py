from flask import Flask, render_template, request
from Model import SpellcheckerModule
app = Flask(__name__)

spell_checker_module = SpellcheckerModule()

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/spell', methods=['GET', 'POST'])
def spell():
     if request.method == 'POST':
         text=request.form['text']
         corrected_text=spell_checker_module.correct_spell(text)
         corrected_grammer=spell_checker_module.correct_grammer(text)
         return render_template('index.html',corrected_text=corrected_text,corrected_grammer=corrected_grammer)


@app.route('/grammer', methods=['GET', 'POST'])
def grammer():
    if request.method == 'POST':
        file=request.files['file']
        readable_file=file.read().decode('utf8',errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        corrected_file_grammer = spell_checker_module.correct_grammer(readable_file)
    return render_template('index.html', corrected_file_text=corrected_file_text, corrected_file_grammer=corrected_file_grammer)


if __name__ == '__main__':
    app.run(debug=True)