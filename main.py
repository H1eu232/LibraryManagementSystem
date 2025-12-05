import datetime

from book_management.book import Book
from member_management.member import Member
from borrow_return_management.loan import Loan
from fine_management.fine import Fine
from reporting.report import Report

def main():
    print("--- Library Management App Simulation (Python) ---")

    book1 = Book(isbn="978-0321765723", title="The C# Programming Language", author="Anders Hejlsberg")
    book2 = Book(isbn="978-0132350884", title="Clean Code", author="Robert C. Martin")

    book1.display_info()
    book2.display_info()
    print()

    member1 = Member(member_id="M001", name="Nguyen Van A")
    member2 = Member(member_id="M002", name="Tran Thi B")

    member1.display_info()
    member2.display_info()
    print()

    today = datetime.datetime.now()
    loan1 = Loan(member_id=member1.member_id, book_isbn=book1.isbn, due_date=today + datetime.timedelta(days=14))
    loan2 = Loan(member_id=member2.member_id, book_isbn=book2.isbn, due_date=today - datetime.timedelta(days=5)) # Trễ 5 ngày

    loan1.display_loan_details()
    print(f"Is loan1 overdue? {loan1.is_overdue()}")

    loan2.display_loan_details()
    print(f"Is loan2 overdue? {loan2.is_overdue()}")
    print()

    if loan2.is_overdue():
        fine_for_member2 = Fine(member_id=member2.member_id, amount=15000)
        fine_for_member2.display_fine_details()
        print()

    overdue_report = Report(report_name="Monthly Overdue Books Report", generated_date=today)
    overdue_report.generate_report()

    print("\n--- Simulation End ---")

if __name__ == "__main__":
    main()