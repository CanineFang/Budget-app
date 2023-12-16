class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [(cat.category, sum(item['amount'] for item in cat.ledger if item['amount'] < 0)) for cat in categories]
    total_spent = sum(spend for category, spend in spendings)

    # Calculate percentage spent for each category
    percentages = [(int((spend / total_spent) * 100 // 10) * 10) for category, spend in spendings]

    # Build the chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            chart += 'o' if percent >= i else ' '
            chart += '  '
        chart += '\n'

    # Add horizontal line and category names
    chart += "    -" + "---" * len(categories) + "\n"
    max_length = max(len(cat.category) for cat in categories)
    for i in range(max_length):
        chart += "     "
        for cat in categories:
            if i < len(cat.category):
                chart += cat.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip()
