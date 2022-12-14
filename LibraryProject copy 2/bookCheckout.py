from database import *


def is_book_available(book_id, member_id):
    if int(member_id) < 1000 or int(member_id) > 9999:
        print("Member ID is invalid")
    else:
      for loan in read_log_records():
        if loan[0] == book_id and loan[-1] == '':
            print("Sorry, this book is not available. It has been loaned out")



is_book_available('5', '1111')


def member_check(member_id):
    try:
        int(member_id)
    except:
        print('Invalid')
    else:
        member_id = str(member_id)
        if len(member_id) == 4:
            print('Member id is Valid')
        else:
            print('Invalid')
