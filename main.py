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


@app.route('/mentors-by-country')
def mentors_by_country():
    mentors_by_country_data = data_manager.get_mentors_by_country()

    return render_template('mentors_by_country.html', mentors_by_country_data=mentors_by_country_data)


@app.route('/contacts')
def contacts():
    contacts_data = data_manager.get_contacts()

    return render_template('contacts.html', contacts_data=contacts_data)


@app.route('/applicants')
def applicants():
    applicants_data = data_manager.get_applicants()

    return render_template('applicants.html', applicants_data=applicants_data)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    applicants_and_mentors_data = data_manager.get_applicants_and_mentors()

    return render_template('applicants_and_mentors.html', applicants_and_mentors_data=applicants_and_mentors_data)


if __name__ == '__main__':
    app.run(debug=True)
