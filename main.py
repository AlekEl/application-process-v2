import data_manager
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_and_schools():
    # We get back dictionaries here (for details check 'database_common.py')
    mentors_and_school = data_manager.get_mentors_and_school()

    return render_template('mentors_and_school.html', mentors_and_school=mentors_and_school)


@app.route('/all-school')
def mentors_all_school():
    mentors_all_schools = data_manager.get_mentors_all_schools()

    return render_template('mentors_all_school.html', mentors_all_schools=mentors_all_schools)


@app.route('/find-carol')
def find_carol():
    carol_data = data_manager.get_carol()

    return render_template('find_carol.html', carol_data=carol_data)


@app.route('/find-hat-girl')
def find_hat_girl():
    hat_girl = data_manager.get_hat_girl()

    return render_template('find_hat_girl.html', hat_girl=hat_girl)


@app.route('/add-and-find-marcus')
def add_and_find_marcus():
    data_manager.add_marcus()
    marcus = data_manager.get_marcus()

    return render_template('find_marcus.html', marcus=marcus)


@app.route('/update-and-find-jemima')
def update_and_find_jemima():
    data_manager.update_jemima()
    jemima = data_manager.get_jemima_number()

    return render_template('find_jemima_number.html', jemima=jemima)


@app.route('/delete-mauriseu.net')
def delete_mauriseu():
    data_manager.delete_mauriseu()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
