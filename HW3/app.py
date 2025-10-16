from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/profile_form')
def profile_form():
    return render_template('profile_form.html')

@app.route('/profile_output', methods=['POST'])
def profile_output():
    # Get form data
    name = request.form['name']
    username = request.form['username']
    bio = request.form['bio']
    sex = request.form['sex']
    location = request.form['location']

    # Pass data to template
    return render_template(
        'profile_output.html',
        name=name,
        username=username,
        bio=bio,
        sex=sex,
        location=location
    )

if __name__ == '__main__':
    app.run(debug=True)
