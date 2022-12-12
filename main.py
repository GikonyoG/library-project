import time

def available_books() -> list:
    books = []
    with open('Book_info.txt', 'r') as f:
        for book in f:
            books.append(book.strip().replace(' ', '').split(','))
    return books


def all_members():
    with open('Student_info.txt', 'r') as f:
        lists = f.readlines()
        ids =[]

        for i in range(len(lists)):
            ids.append(lists[i].rstrip('\n'))
        # TODO: Validate ids

        return ids


def search_book(title: str):
    book_list = []
    with open('Book_info.txt', 'r') as f:
        for book in f:
            book_list.append(book.strip().split(','))
    
    for index, book in enumerate(book_list):
        if title == book[1]:
            return book_list[index]
