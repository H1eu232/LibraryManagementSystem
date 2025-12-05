import datetime

class Loan:
    def __init__(self, member_id, book_isbn, due_date):
        self.member_id = member_id
        self.book_isbn = book_isbn
        self.due_date = due_date

    def display_loan_details(self):
        # Định dạng ngày cho dễ đọc
        due_date_str = self.due_date.strftime("%Y-%m-%d")
        print(f"Loan Details: [MemberID: {self.member_id} borrowed Book ISBN: {self.book_isbn}, Due on: {due_date_str}]")

    def is_overdue(self):
        return datetime.datetime.now() > self.due_date