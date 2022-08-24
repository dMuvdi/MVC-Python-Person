from flask import Flask, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from logic.person import Person
import web_view
import console_view


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = "abc"


@app.route("/")
def start():
    print("hello welcome to people")
    return web_view.index()

# insertion process


@app.route('/choice_insert')
def insert_choice():
    flash("Choose if you want to do the insertion on web or console", "success")
    return redirect('people')


@app.route('/person_get', methods=['GET'])
def person_web_get():
    return web_view.person_web_get()


@app.route("/console_insert")
def insert_console():
    console_view.insert_view()

    person = {}

    id_p = input("\nType person id: ")

    if (len(id_p) == 0):
        console_view.empty_input()

    while (len(id_p) == 0):
        id_p = input("\nType person id: ")

        if (len(id_p) == 0):
            console_view.empty_input()

    if (Person.verify_id(id_p) == True):
        console_view.person_founded()

    while (Person.verify_id(id_p)):
        id_p = input("\nType person id: ")

        if (Person.verify_id(id_p) == True):
            console_view.person_founded()

    p_name = input("\nType person name: ")

    if (len(p_name) == 0):
        console_view.empty_input()

    while (len(p_name) == 0):
        p_name = input("\nType person name: ")

        if (len(p_name) == 0):
            console_view.empty_input()

    p_last_name = input("\nType person last name: ")

    if (len(p_last_name) == 0):
        console_view.empty_input()

    while (len(p_last_name) == 0):
        p_last_name = input("\nType person last name: ")
        if (len(p_last_name) == 0):
            console_view.empty_input()

    person["id"] = int(id_p)
    person['name'] = {}
    person['name']["first_name"] = str(p_name)
    person['name']["last_name"] = str(p_last_name)

    Person.person_insert(person)

    flash("The insertion was done on console", "info")
    return redirect('people')


@app.route('/person_detail', methods=['POST'])
def insert_web():

    person = {}

    id_p = request.form['id_person']

    if (Person.verify_id(id_p) == True):
        flash("The id already exists")
        return redirect('person_get')

    p_name = request.form['first_name']
    p_last_name = request.form['last_name']

    per = Person(id_person=id_p, name=p_name, last_name=p_last_name)

    person['id'] = int(per.id_person)
    person['name'] = {}
    person['name']["first_name"] = str(per.name)
    person['name']["last_name"] = str(per.last_name)

    Person.person_insert(person)

    console_view.inserted_on_web()

    return web_view.insert_web(per)

# show all people


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in Person.get_all()]
    print(data)
    return web_view.people(data)


@app.route('/people_id/<id>')
def people_id(id):
    data = [(i.id_person, i.name, i.last_name) for i in Person.get_all()]
    print(data)
    return web_view.people_id(data, id)


# update process

@app.route('/choice_update/<id>')
def update_choice(id):
    flash("Choose if you want to do the updation on web or console", "warning")
    return redirect(url_for('people_id', id=id))


@app.route('/console_update/<id>')
def console_update(id):
    data = Person.person_update_form(id)
    console_view.person_update(data[0][0], data[0][1], data[0][2])

    p_new_name = input("\nType the new name: ")

    if (len(p_new_name) == 0):
        console_view.empty_input()

    while (len(p_new_name) == 0):
        p_new_name = input("\nType person new name: ")
        if (len(p_new_name) == 0):
            console_view.empty_input()

    p_new_last_name = input("\nType the new last name: ")

    if (len(p_new_last_name) == 0):
        console_view.empty_input()

    while (len(p_new_last_name) == 0):
        p_new_last_name = input("\nType person last name: ")
        if (len(p_new_last_name) == 0):
            console_view.empty_input()

    data = Person.person_update(id, p_new_name, p_new_last_name)

    flash("The updation was done on console for value: " +
          str(data[0][0])+" "+data[0][1]+" "+data[0][2], "info")
    return redirect(url_for('people'))


@app.route('/person_update/<id>', methods=['GET'])
def person_update_form(id):
    data = Person.person_update_form(id)
    return web_view.person_update_form(data)


@app.route('/person_updated/<id>', methods=['POST'])
def person_update(id):
    p_name = request.form['first_name']
    p_last_name = request.form['last_name']
    data = Person.person_update(id, p_name, p_last_name)

    console_view.updated_on_web()

    return web_view.person_update(data)

# delete process


@app.route('/choice_delete/<id>', methods=['POST'])
def delete_choice(id):
    flash("Choose if you want to do the deletion on web or console", "danger")
    return redirect(url_for('people_id', id=id))


@app.route('/console_delete/<id>')
def console_delete(id):
    data = Person.person_update_form(id)
    console_view.person_delete(data[0][0], data[0][1], data[0][2])

    answer = input("\n\n Are you sure you want to delete this person? (y/n): ")

    while (answer != 'y'
            and answer != 'n'):
        console_view.wrong_answer()
        answer = input(
            "\n\n Are you sure you want to delete this person? (y/n): ")
        
    if (len(answer) == 0):
        console_view.empty_input()

    while (len(answer) == 0):
        p_new_last_name = input("\n\n Are you sure you want to delete this person? (y/n): ")
        if (len(answer) == 0):
            console_view.empty_input()


    if answer == 'y':
        flash("The deletion was done successfully on console! for value: " +
              str(data[0][0])+" "+data[0][1]+" "+data[0][2], "info")
        Person.delete_person(id)
        return redirect(url_for('people'))
    else:
        flash("The deletion process on console was canceled", "info")
        return redirect(url_for('people'))


@app.route('/person_delete/<id>', methods=['POST'])
def delete(id):
    data = Person.person_update_form(id)
    flash("Sucessfully deleted! value: " +
          str(data[0][0])+" "+data[0][1]+" "+data[0][2], "info")
    Person.delete_person(id)
    console_view.deleted_on_web()
    return redirect(url_for('people'))


if __name__ == '__main__':
    app.run(debug=True)
