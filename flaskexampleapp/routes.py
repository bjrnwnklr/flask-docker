from flaskexampleapp import app
from flaskexampleapp.forms import ExampleForm
from flask import render_template, jsonify


@app.route('/heartbeat')
def heartbeat():
    return jsonify({
        'status': 'healthy'
    })


@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = ExampleForm()
    if form.validate_on_submit():
        # Form was submitted as a POST request.
        content = title = f'POST: selected {form.select.data}'
    else:
        # Form was not submitted, GET request.
        content = title = 'Hello!'

    return render_template('index.html', title=title, content=content, form=form)
