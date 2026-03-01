class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    result_list = []

    for person_data in people:
        current_name = person_data["name"]
        current_person = Person.people[current_name]

        partner_key = "wife" if "wife" in person_data else "husband"
        partner_name = person_data.get(partner_key)

        if partner_name is not None:
            partner_instance = Person.people.get(partner_name)
            setattr(current_person, partner_key, partner_instance)
        else:
            setattr(current_person, partner_key, None)

        result_list.append(current_person)

    return result_list
