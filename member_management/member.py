class Member:
    def __init__(self, member_id, name, card_status="Active"):
        self.member_id = member_id
        self.name = name
        self.card_status = card_status # Ví dụ: "Active", "Suspended"

    def display_info(self):
        print(f"Member: [ID: {self.member_id}, Name: {self.name}, Status: {self.card_status}]")