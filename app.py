from flask import Flask, request, redirect, url_for
import requests


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index(): 
    return 'Hello MailboxLayer API!'


@app.route('/result/<string:acc_key>/<string:email>/<string:format_valid>/<string:disposable>/<string:score>/<string'
           ':mx_found>')
def result(acc_key, email, format_valid, disposable, score, mx_found):
    return '<h3>Email: {};  <br>Is Format Valid: {}; <br>Is Disposable: {}; <br> Score: {}; <br> Mx_found: {};<br>Your ' \
           'Access Key:{} </h3>'.format(email, format_valid, disposable, score, mx_found, acc_key)


@app.route('/validate', methods=['GET', 'POST'])
def numverify():
    if request.method == 'GET':
        return '''<h1>Please fill out the parameters</h1>
                    <form method="POST" action="/validate">
                    <input type="text" name="acc_key">
                    <input type="text" name="email">
                    <input type="submit" value="Request">
                </form>'''
    else:
        acc_key = request.form['acc_key']
        email = request.form['email']

        req = requests.get('http://apilayer.net/api/check?access_key=' + acc_key + '&email=' + email)
        response = req.json()

        disposable = response["disposable"]
        format_valid = response["format_valid"]
        score = response["score"]
        mx_found = response["mx_found"]

        return redirect(url_for('result', acc_key=acc_key, email=email, format_valid=format_valid,
                                disposable=disposable, score=score, mx_found=mx_found))


if __name__ == '__main__':
    app.run()