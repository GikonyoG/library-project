book_records = []
log_records=[]

#function reads the book records from the "Book_Info.txt" file
def read_book_records():
  with open("Book_Info.txt", "r") as f:
    for line in f:
      record = line.strip().split(",")
      book_records.append(record)
  return book_records
#function reads the book records from the "logfile.txt" file
def read_log_records():
  with open("logfile.txt", "r") as f:

    for line in f:

      record = line.strip().split(",")
      log_records.append(record)
  return log_records






