class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __repr__(self):
        return f'Category: {self.category}\nBalance: {str(self.get_balance())}\nEntries: {len(self.ledger)}'

    def __str__(self):
        return self.print_cat()

    def print_cat(self):
        line_width = 30
        output = ''

        output += f"{self.category:*^{line_width}}\n"
        for entry in self.ledger:
            amt_width = len(f"{entry['amount']:.2f}")
            output += f"{entry['description'][:line_width - amt_width - 1]:<{line_width - amt_width}}{entry['amount']:>{amt_width}.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        pass

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance
        
    def get_spending(self):
        spending = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                spending += entry['amount']
        return spending

    def transfer(self, amount, this_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {this_cat.category}')
            this_cat.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    total_spend = 0
    per_category_spending = []
    line_width = len(categories) * 3 + 1
    output = f'Percentage spent by category\n'

    for this_cat in categories:
        cat_spend = abs(this_cat.get_spending())
        total_spend += cat_spend
        per_category_spending.append({'category':this_cat.category, 'spending': cat_spend})

    for perc in range(100, -1, -10):
        if perc is not None:
            output += f'{perc:>3}|'
            for each_cat in per_category_spending:
                if (test := each_cat['spending'] / total_spend * 100) > perc:
                    # output += f" {test:.2f}"
                    output += f" o "
                else:
                    output += f"   "
            output += ' \n'
    output += f'{"":<4}{"":-^{line_width}}\n'
    
    for index in range(long_name := max([len(x['category']) for x in per_category_spending])):
        output += f'{"":<4}'
        for this_cat in categories:
            if index < len(this_cat.category):
                output += f' {this_cat.category[index]} '
            else:
                output += '   '
        if index < long_name - 1:
            output += ' \n'
        else:
        # if index == long_name - 1:
            output += ' '
            
    return output

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.withdraw(1, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(44.44, 'groceries')
auto = Category('Auto')
entertainment = Category('Entertainment')
auto.deposit(1500, 'restaurant and more food for dessert')
auto.withdraw(95.89, 'restaurant and more food for dessert')

print(create_spend_chart([food, auto, clothing, entertainment]))