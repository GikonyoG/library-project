from main import available_books, all_members


def popular_books():
    books = available_books()
    book_titles = []
    highest_count = 0
    popular_book = None

    for book in books:
        book_titles.append(book[1])

    for title in book_titles:
        if book_titles.count(title) > highest_count:
            highest_count = book_titles.count(title)
            popular_book = title

    return popular_book


def calculate_budget(budget, popular_book):
    books = available_books()
    sum = 0

    for book in books:
        if book[1] == popular_book:
            x = budget / int(book[-2])
            print(f'you can buy {str(int(x))} of {book[1]}')
            break

popular_book = popular_books()
calculate_budget(100, popular_book)