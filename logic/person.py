import json


class Person(object):
    """
    Class used to represent an Person
    """

    def __init__(self, id_person: int, name: str = 'Name', last_name: str = "LastName"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    def __str__(self):
        """ Returns str of person.
          :returns: string person
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_person, self.name, self.last_name)

    @classmethod
    def get_all(cls):
        """ Returns list of people
        :returns: list of people
        :rtype: list
        """
        result = list()

        with open('logic/db.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for p in data:
                person = Person(p['id'], p['name']
                                ['first_name'], p['name']['last_name'])
                result.append(person)
        return result

    @classmethod
    def person_insert(cls, new_data):
        with open('logic/db.json', 'r+', encoding='utf-8') as json_file:
            file_data = json.load(json_file)
            file_data.append(new_data)

            json_file.seek(0)

            json.dump(file_data, json_file, indent=4)

    @classmethod
    def verify_id(cls, idper):
        """ Returns if a person exists in the list
        :returns: boolean whether true or false if the person exists
        :rtype: boolean
        """
        person_found = True
        with open('logic/db.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for p in data:
                if (p['id'] == int(idper)):
                    person_found = True
                    break
                else:
                    person_found = False

        return person_found

    @classmethod
    def delete_person(cls, idper):
        with open('logic/db.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            newData = []
            for p in data:
                if (p['id'] != int(idper)):
                    newData.append(p)

        with open('logic/db.json', 'w', encoding='utf-8') as json_file:
            json.dump(newData, json_file, indent=4)

    @classmethod
    def person_update_form(cls, idper):
        """ Returns the person data
        :returns: the person obeject to update
        :rtype: Object
        """
        with open('logic/db.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for p in data:
                if (p['id'] == int(idper)):
                    return [(p['id'], p['name']['first_name'], p['name']['last_name'])]

    @classmethod
    def person_update(cls, idper, name, last_name):
        """ Returns the person data
        :returns the person object to update
        :rtype: Object
        """
        with open('logic/db.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for p in data:
                if (p['id'] == int(idper)):
                    p['name']['first_name'] = name
                    p['name']['last_name'] = last_name
                    data_sent = [
                        (p['id'], p['name']['first_name'], p['name']['last_name'])]

        with open('logic/db.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return data_sent


if __name__ == '__main__':

    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    edwin.name = "Edwin. A"
    print(edwin)
