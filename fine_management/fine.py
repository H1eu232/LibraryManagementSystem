class Fine:
    def __init__(self, member_id, amount, is_paid=False):
        self.member_id = member_id
        self.amount = amount
        self.is_paid = is_paid

    def display_fine_details(self):
        status = "Paid" if self.is_paid else "Unpaid"
        print(f"Fine Details: [MemberID: {self.member_id}, Amount: {self.amount:,.0f} VND, Status: {status}]")