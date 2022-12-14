from database import *
# Define a function to find a book by ID
def find_book_by_id(book_id):
  for book in read_book_records():
    if book[0] == str(book_id):
      return book
  return "This book does not exist"

# Define a function to find books by title
def find_books_by_title(title):
  matching_books = []
  for book in read_book_records():
    if book[1] == str(title):
      matching_books.append(book)
  return matching_books

# Define a function to find books by author
def find_books_by_author(author):
  matching_books = []
  for book in read_book_records():
    if book[2] == author:
      matching_books.append(book)
  return matching_books







