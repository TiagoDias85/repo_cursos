class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for entry in self.ledger:
            items += f"{entry['description'][:23]:23}{entry['amount']:>7.2f}\n"
            total += entry['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    total_withdrawals = 0
    category_withdrawals = {}

    for category in categories:
        withdrawals = sum(entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        category_withdrawals[category.name] = withdrawals
        total_withdrawals += withdrawals

    # Calculate the percentage spent in each category and create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for category in categories:
            percentage = category_withdrawals[category.name] * 100 // total_withdrawals if total_withdrawals != 0 else 0
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add the horizontal line and category names
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart
