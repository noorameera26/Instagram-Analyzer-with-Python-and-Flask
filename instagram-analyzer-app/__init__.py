from flask import Flask, render_template, request, redirect, url_for, render_template
from forms import ValidateHashtag

app = Flask(__name__)
app.config.update(
        WTF_CSRF_ENABLED = True, #Disable Cross-site request forgery protection
        SECRET_KEY = 'nanana'
)
#app.secret_key = 'nanana'

#routes
#telling our @app to execute home() whenever a user visits domain at the given route()
@app.route('/', methods = ['GET', 'POST'])
def main():
    #this should return the homepage
    form = ValidateHashtag(request.form)
    if form.validate_on_submit():
        #if hashtag data is validated, return it to be analyzed
        text = form.input_hashtag.data
        return redirect(url_for('instagram_analyze'))
    return render_template('homepage.html', form = form)

#telling our @app to analyze the searched hashtag
@app.route('/instagram_analyze/<user_input>')
def instagram_analyze(user_input):
    return render_template(
        'instagram_analyzer.html',
        input = user_input,
        file_name = user_input + ".png" #??????
    )

#unsure what this is still
@app.route('/instagram_analyze/<image_name>.png')
def image(image_name):
    pass

#display the about app
@app.route('/about')
def home():
    return render_template('about.html')