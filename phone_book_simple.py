
def add_record(phone_book, name, surname, phone=None, email=None):
    """
    Add a record to phone_book

    Args:
        phone_book: list holding the phone book
        name: name of the created contact
        surname: surname of the created contact
        phone: phone number of the created contact
        email: email address of the created contact
    """
    phone_book.append({
        'name': name,
        'surname': surname,
        'phone': phone,
        'email': email,
    })
    return phone_book


def change_record(phone_book, search_tag, tag, replaced_tag, new_value):
    """
    Change record from phone_book

    Args:
        phone_book: list holding the phone book
        search_tag: tag by which we look for the contact
        tag: value of the search tag
        replaced_tag: the tag name we wish to replace
        new_value: new value of the replaced tag
    """
    for i in range(0, len(phone_book)):
        if phone_book[i][search_tag] == tag:
            phone_book[i][replaced_tag] = new_value
    return phone_book


def delete_record(phone_book, search_tag, tag):
    """
    Deletes a record from the phone book

    Args:
        phone_book: list holding the phone book
        search_tag: tag by which we look for the contact
        tag: value of the search tag
    """
    for i in range(0, len(phone_book)):
        if phone_book[i][search_tag] == tag:
            del phone_book[i]
    return phone_book


def search_record(phone_book, search_tag, tag):
    """
    Lists records with search_tag matching a tag, from phone_book.

    Args:
        phone_book: list holding the phone book
        search_tag: tag by which we look for the contact
        tag: value of the search tag
    """
    returned_list = []
    for i in range(0, len(phone_book)):
        if phone_book[i][search_tag] is None:
            continue
        if tag in phone_book[i][search_tag]:
            returned_list.append(phone_book[i])
    return returned_list


def print_phone_book(phone_book):
    """
    Prints nicely the phone_book
    """
    for record in phone_book:
        print(f'Name: {record["name"]} {record["surname"]}', end='')
        if record["phone"] is not None:
            print(f', phone number: {record["phone"]}', end='')
        if record["email"] is not None:
            print(f', email: {record["email"]}', end='')
        print(';')


if __name__ == '__main__':

    mock_data = [
        {'name': '1', 'surname': '3', 'phone': '12', 'email': '@sth.sth'},
        {'name': '2', 'surname': '3', 'phone': '23', 'email': '@sth.sth'}]

    mock_data = add_record(mock_data, 'John', 'Doe', phone='123456789')
    mock_data = add_record(mock_data, 'Jane', 'Doe')

    print_phone_book(search_record(mock_data, 'surname', 'Doe'))

    mock_data = change_record(mock_data, 'name', 'Jane', 'surname', 'Dont')
    print()
    print_phone_book(search_record(mock_data, 'email', '@sth'))
