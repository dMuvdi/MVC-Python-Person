from flask import Flask, render_template


def index():
    return render_template('index.html')


def insert_web(p):
    return render_template('person_detail.html', value=p)


def web_person_founded():
    return render_template('id_found.html')


def person_web_get():
    return render_template('person.html')


def people(data):
    return render_template('people.html', value=data)


def people_id(data, id):
    return render_template('people.html', value=data, id=id)


def person_update_form(data):
    return render_template('person_update_form.html', value=data)


def person_update(data):
    return render_template('person_update.html', value=data)
