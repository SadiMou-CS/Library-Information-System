from db import connect

conn=connect()
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Loan;")
cur.execute("DROP TABLE IF EXISTS Writes;")
cur.execute("DROP TABLE IF EXISTS Author;")
cur.execute("DROP TABLE IF EXISTS Book;")
cur.execute("DROP TABLE IF EXISTS Librarian;")
cur.execute("DROP TABLE IF EXISTS LibraryMember;")

cur.execute(""" CREATE TABLE LibraryMember (UserID INT PRIMARY KEY, PhoneNumber VARCHAR(20), Address VARCHAR(200));""")
cur.execute(""" CREATE TABLE Librarian (UserID INT PRIMARY KEY, LibrarianType VARCHAR(50), HireDate DATE);""")
cur.execute(""" CREATE TABLE Book (BookID VARCHAR(20) PRIMARY KEY, Title VARCHAR(200), BookType VARCHAR(20), Genre VARCHAR(50), YearPublished INT, Publisher VARCHAR(100), TotalCopies INT CHECK (TotalCopies>=0), AvailableCopies INT CHECK (AvailableCopies>=0), Location VARCHAR(100), CHECK (AvailableCopies<=TotalCopies));""")
cur.execute(""" CREATE TABLE Author (AuthorID INT PRIMARY KEY, Name VARCHAR(100));""")
cur.execute(""" CREATE TABLE Writes (AuthorID INT, BookID VARCHAR(20), PRIMARY KEY (AuthorID, BookID), FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID), FOREIGN KEY (BookID) REFERENCES Book(BookID));""")
cur.execute(""" CREATE TABLE Loan (LoanID INTEGER PRIMARY KEY AUTOINCREMENT, UserID INT, BookID VARCHAR(20), StaffID INT, CheckoutDate DATE, CheckinDate DATE, DueDate DATE, LoanStatus VARCHAR(10), CHECK (LoanStatus IN ('active', 'returned', 'overdue')), CHECK (CheckinDate IS NULL OR CheckinDate >= CheckoutDate), CHECK (DueDate >= CheckoutDate), FOREIGN KEY (UserID) REFERENCES LibraryMember(UserID), FOREIGN KEY (BookID) REFERENCES Book(BookID), FOREIGN KEY (StaffID) REFERENCES Librarian(UserID));""")

#sample data
#LibraryMember
cur.execute("INSERT INTO LibraryMember VALUES (101, '571-555-0101', '123 Maple St, Arlington, VA')")
cur.execute("INSERT INTO LibraryMember VALUES (102, '703-555-0202', '456 Oak Rd, Alexandria, VA')")
cur.execute("INSERT INTO LibraryMember VALUES (103, '202-555-0303', '789 Pine Ln, Fairfax, VA')")

#Librarian
cur.execute("INSERT INTO Librarian VALUES (501, 'Head Librarian', '2015-05-20')")
cur.execute("INSERT INTO Librarian VALUES (502, 'Assistant', '2019-11-10')")

# Author
cur.execute("INSERT INTO Author VALUES (1, 'Homer')")
cur.execute("INSERT INTO Author VALUES (2, 'George Orwell')")
cur.execute("INSERT INTO Author VALUES (3, 'Lara Hoby')")
cur.execute("INSERT INTO Author VALUES (4, 'Paulo Coelho')")
cur.execute("INSERT INTO Author VALUES (5, 'F. Scott Fitzgerald')")
cur.execute("INSERT INTO Author VALUES (6, 'J.D. Salinger')")
cur.execute("INSERT INTO Author VALUES (7, 'Jane Austen')")
cur.execute("INSERT INTO Author VALUES (8, 'Yuval Noah Harari')")
cur.execute("INSERT INTO Author VALUES (9, 'Michelle Obama')")
cur.execute("INSERT INTO Author VALUES (10, 'Alex Michaelides')")
cur.execute("INSERT INTO Author VALUES (11, 'Aldous Huxley')")
cur.execute("INSERT INTO Author VALUES (12, 'Stephen King')")
cur.execute("INSERT INTO Author VALUES (13, 'J.R.R. Tolkien')")

# Writes
cur.execute("INSERT INTO Writes VALUES (1, '9780140449136')")
cur.execute("INSERT INTO Writes VALUES (2, '9780451526342')")
cur.execute("INSERT INTO Writes VALUES (3, '9783791386287')") # Picasso
cur.execute("INSERT INTO Writes VALUES (4, '9780062315007')") # The Alchemist
cur.execute("INSERT INTO Writes VALUES (2, '9780451524935')") # 1984 (George Orwell)
cur.execute("INSERT INTO Writes VALUES (5, '9780743273565')") # The Great Gatsby
cur.execute("INSERT INTO Writes VALUES (6, '9780316769488')") # The Catcher in the Rye
cur.execute("INSERT INTO Writes VALUES (7, '9780141439518')") # Pride and Prejudice
cur.execute("INSERT INTO Writes VALUES (8, '9787236444994')") # Sapiens (Hardcover)
cur.execute("INSERT INTO Writes VALUES (8, '9786974967812')") # Sapiens (Paperback)
cur.execute("INSERT INTO Writes VALUES (8, '9784328406075')") # Sapiens (Hardcover 2014)
cur.execute("INSERT INTO Writes VALUES (9, '9789340292869')") # Becoming (E-book)
cur.execute("INSERT INTO Writes VALUES (9, '9784723696046')") # Becoming (Paperback)
cur.execute("INSERT INTO Writes VALUES (10, '9782402781984')") # The Silent Patient
cur.execute("INSERT INTO Writes VALUES (11, '9788949909550')") # Brave New World (1952)
cur.execute("INSERT INTO Writes VALUES (11, '9786794691822')") # Brave New World (2013)
cur.execute("INSERT INTO Writes VALUES (12, '9789181601206')") # The Shining
cur.execute("INSERT INTO Writes VALUES (13, '9787239881556')") # The Hobbit

#Book
cur.execute("INSERT INTO Book VALUES ('9780140449136', 'The Odyssey', 'Hardcover', 'Classic', 2003, 'Penguin', 4, 2, 'Arlington')")
cur.execute("INSERT INTO Book VALUES ('9780451526342', 'Animal Farm', 'Paperback', 'Satire', 1945, 'Signet', 10, 10, 'Alexandria')")
cur.execute("INSERT INTO Book VALUES ('9783791386287', 'Picasso: Masters of Art', 'Paperback', 'History', 2020, 'National Geographic Books', 5, 5, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9780062315007', 'The Alchemist', 'Hardcover', 'Fiction', 1988, 'HarperOne', 10, 8, 'Arlington')")
cur.execute("INSERT INTO Book VALUES ('9780451524935', '1984', 'Paperback', 'Dystopian', 1949, 'Signet Classic', 15, 12, 'Alexandria')")
cur.execute("INSERT INTO Book VALUES ('9780743273565', 'The Great Gatsby', 'Paperback', 'Classic', 1925, 'Scribner', 8, 3, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9780316769488', 'The Catcher in the Rye', 'Hardcover', 'Fiction', 1951, 'Little, Brown', 5, 5, 'Fairfax')")
cur.execute("INSERT INTO Book VALUES ('9780141439518', 'Pride and Prejudice', 'Paperback', 'Romance', 1813, 'Penguin Classics', 12, 10, 'Arlington')")
cur.execute("INSERT INTO Book VALUES ('9787236444994', 'Sapiens', 'Hardcover', 'History', 2005, 'Simon & Schuster', 14, 4, 'Fairfax')")
cur.execute("INSERT INTO Book VALUES ('9789340292869', 'Becoming', 'E-book', 'Biography', 1974, 'Random House', 11, 6, 'Falls Church')")
cur.execute("INSERT INTO Book VALUES ('9782402781984', 'The Silent Patient', 'Hardcover', 'Thriller', 2023, 'Random House', 9, 0, 'Alexandria')")
cur.execute("INSERT INTO Book VALUES ('9788949909550', 'Brave New World', 'Hardcover', 'Dystopian', 1952, 'Simon & Schuster', 8, 6, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9789181601206', 'The Shining', 'Hardcover', 'Horror', 2002, 'Hachette', 16, 10, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9786974967812', 'Sapiens', 'Paperback', 'History', 1961, 'Simon & Schuster', 12, 7, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9784328406075', 'Sapiens', 'Hardcover', 'History', 2014, 'Macmillan', 16, 0, 'Shirlington')")
cur.execute("INSERT INTO Book VALUES ('9787239881556', 'The Hobbit', 'Paperback', 'Fantasy', 1990, 'Penguin', 5, 0, 'Fairfax')")
cur.execute("INSERT INTO Book VALUES ('9784723696046', 'Becoming', 'Paperback', 'Biography', 2020, 'Random House', 10, 2, 'Falls Church')")
cur.execute("INSERT INTO Book VALUES ('9786794691822', 'Brave New World', 'Hardcover', 'Dystopian', 2013, 'Penguin', 5, 3, 'Shirlington')")

conn.commit()
conn.close()
