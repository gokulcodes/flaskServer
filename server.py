from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:paths>')
def renderer(paths):
    return render_template(paths)


def writer(content):
    first_name = content['first_name']
    last_name = content['last_name']
    sub = content['subject']
    mail_id = content['mail']
    detail = content['content']
    with open('data.txt', 'w') as file:
        file.write(
            f'First Name: {first_name},  Last Name: {last_name}, Subject: {sub}, Email: {mail_id}, Description: {detail}')


@app.route('/form_endpoint', methods=['POST', 'GET'])
def form_end():
    if request.method == 'POST':
        data = request.form.to_dict()
        writer(data)
    return redirect('/thanks.html#contact-section')


@app.route('/mail_endpoint')
def mail_end():
    return render_template('index.html')
