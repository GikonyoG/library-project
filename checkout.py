from datetime import date
from main import available_books, all_members

today = date.today().strftime("%d/%m/%Y")


def update_book_data(book_id: int):  # TODO
    books = available_books()
    books[book_id - 1][-1] = today

    for book in books:
        with open('Book_info.txt', 'w') as f:
            f.writelines('') 

        for data in book:
            with open('Book_info.txt', 'a') as f:
                f.writelines(str(data) + '\n')


def checkout_book(member_id, book_id):
    order = []

    for index, book in enumerate(available_books()):
        if book_id == int(book[0]):
            order.append(available_books()[index])

    for index, member in enumerate(all_members()):
        if str(member_id) == member:
            order.append(all_members()[index])

    # Check is book is available
    if order[0][-1] != "":
        return "Book is not available"

    # Update the date loaned
    update_book_data(book_id)
        
    return order


print(checkout_book(2344, 3))
