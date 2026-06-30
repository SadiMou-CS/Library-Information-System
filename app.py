from db import connect
def search(): #search books
  title=input("Enter book title: ")
  conn = connect()
  cur=conn.cursor()
  cur.execute(""" SELECT b.Title, b.AvailableCopies, a.Name, b.BookID, b.BookType FROM Book b JOIN Writes w ON b.BookID=w.BookID JOIN Author a ON w.AuthorID =a.AuthorID WHERE LOWER(b.Title) LIKE LOWER(?) """, ('%'+title+'%',))
  results=cur.fetchall()
  if results:
    for row in results:
      print(f"Title: {row[0]}, Book Type: {row[4]}, Available: {row[1]}, Author: {row[2]}, BookID: {row[3]}")
  else:
    print("No books found. .·°՞(っ-ᯅ-ς)՞°·.")
  cur.close()
  conn.close()

def checkout():
  userID=int(input("Enter your UserID: "))
  bookID = input("Enter BookID: ")
  conn=connect()
  cur = conn.cursor()
  cur.execute(""" SELECT COUNT(*) FROM Loan WHERE UserID = ? AND LoanStatus = 'active' """, (userID,))
  count = cur.fetchone()[0]
  if count >= 50:
    print("You cannot borrow more than 50 books.")
    conn.close()
    return
  
  cur.execute("SELECT AvailableCopies FROM Book WHERE BookID = ?", (bookID,))
  result=cur.fetchone()
  if result and result[0]>0:
    cur.execute(""" INSERT INTO Loan (UserID, BookID, StaffID, CheckoutDate, CheckinDate, DueDate, LoanStatus) VALUES (?, ?, ?, DATE('now'), NULL, DATE('now', '+14 days'), 'active')""",(userID, bookID, 501))
    cur.execute(""" UPDATE Book SET AvailableCopies=AvailableCopies-1 WHERE BookID=?""",(bookID,))
    conn.commit()
    print("Book checkout successful! ( ˶ˆᗜˆ˵ )")
  else:
    print("Book not available (｡ᵕ ◞ _◟)")
  cur.close()
  conn.close()
  
def returnBook():
  loanID=int(input("Enter LoanID: "))
  conn=connect()
  cur=conn.cursor()
  cur.execute("SELECT BookID FROM Loan WHERE LoanID = ?", (loanID,))
  result=cur.fetchone()
  if result:
    bookID=result[0]
    cur.execute(""" UPDATE Loan SET CheckinDate=DATE('now'), LoanStatus='returned' WHERE LoanID=?""",(loanID,))
    cur.execute("""UPDATE Book SET AvailableCopies=AvailableCopies+1 WHERE BookID=?""", (bookID,))
    conn.commit()
    print("Book returned successfully! ( ⸝⸝´ ᵕ `⸝⸝)")
  else:
    print("Invalid LoanID (⇀‸↼‶)")
  cur.close()
  conn.close()

def viewLoans():
    userID = int(input("Enter your UserID: "))
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT LoanID, BookID, DueDate, LoanStatus
        FROM Loan
        WHERE UserID = ?
    """, (userID,))

    results = cur.fetchall()

    if results:
        for row in results:
            print(f"LoanID: {row[0]}, Book: {row[1]}, Due: {row[2]}, Status: {row[3]}")
    else:
        print("No loans found.")

    conn.close()

def menu():
  while True:
    print("\n 𓂃˖˳·˖ ִֶָ ⋆ Bookbuggies Library System ⋆ ִֶָ˖·˳˖𓂃 ִֶָ ")
    print("1. Search Books 🔍📚")
    print("2. Checkout Book 𓂃🖊")
    print("3. Return Book 𐔌՞. .՞𐦯づ📖") 
    print("4. View My Loans")
    print("5. Exit")
    choice=input("Select option number: ")
    if choice == '1':
      search()
    elif choice == '2':
      checkout()
    elif choice == '3':
      returnBook()
    elif choice == '4':
      viewLoans()
    elif choice == '5':
      break
    else:
      print("Invalid option!")

if __name__=="__main__":
  menu()

