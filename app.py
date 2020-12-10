from flask import Flask, render_template, url_for, flash, redirect, request


app = Flask(__name__)
app.config['SECRET_KEY'] = '092487f8e26e1ddc22d41f919418e32a'

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    # introduction for our project have two buttons here
    return render_template('home.html', title='Home')

# page for Hinduism
@app.route('/rel1', methods=['GET'])
def rel1():
    return render_template('rel1.html', title='Hinduism')
# page for Judaism
@app.route('/rel2', methods=['GET'])
def rel2():
    return render_template('rel2.html', title='Judaism')

# page for definition of religion
@app.route('/def', methods=['GET'])
def defn():
    return render_template('def.html', title='Religion Definition')

if __name__ == '__main__':
    app.secret_key = app.config['SECRET_KEY']
    app.run(debug=True)
