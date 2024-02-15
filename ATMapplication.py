class User:
    def __init__(self, user_id, password, balance=5000, login_attempts=0):
        self.user_id = user_id
        self.password = password
        self.balance = balance
        self.login_attempts = login_attempts

    def authenticate(self, entered_password):
        if self.login_attempts >= 3:
            print("Account is locked. Please contact support.")
            return False
        if entered_password == self.password:
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            print("Incorrect password. Attempts remaining:", 3 - self.login_attempts)
            return False

    def deposit(self, amount, denominations):
        if self.authenticate(input("Enter your password: ")):
            # Deposit logic with denominations
            print("Deposit successful.")
            # Update balance and other necessary calculations

    def withdraw(self, amount, denominations):
        if self.authenticate(input("Enter your password: ")):
            # Withdrawal logic with denominations
            print("Withdrawal successful.")
            # Update balance and other necessary calculations

    def check_balance(self):
        if self.authenticate(input("Enter your password: ")):
            # Display balance
            print("Your balance is:", self.balance)

    def change_credentials(self):
        current_password = input("Enter current password: ")
        if self.authenticate(current_password):
            new_password = input("Enter new password: ")
            self.password = new_password
            print("Password changed successfully.")

class Admin:
    def __init__(self, admin_id, admin_password, balance=0):
        self.admin_id = admin_id
        self.admin_password = admin_password
        self.balance = balance

    def authenticate(self, entered_password):
        # Admin authentication logic
        pass

    def total_balance(self):
        # Display total balance
        print("Total balance in admin account:", self.balance)

    def cash_deposit(self, amount, denominations):
        # Admin deposit logic
        pass

    def notification(self):
        if self.balance < 75000:
            print("Notification: Balance is less than 75k. Please take necessary actions.")

# Example Usage:
users = [User("user1", "password1"), User("user2", "password2"), User("user3", "password3")]
admin = Admin("admin", "admin_password")

# Perform user operations
users[0].deposit(20000, {100: 2, 2000: 5})
users[1].withdraw(10000, {100: 1, 200: 1, 500: 1})
users[2].check_balance()
users[0].change_credentials()

# Perform admin operations
admin.total_balance()
admin.cash_deposit(50000, {100: 2, 2000: 5})
admin.notification()