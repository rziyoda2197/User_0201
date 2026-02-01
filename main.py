class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def ban_user(self, user):
        return f"{user} bloklandi"


class Customer(User):
    def buy(self, product):
        return f"{self.username} {product} sotib oldi"


admin = Admin("root")
customer = Customer("ali")

print(admin.ban_user("vali"))
print(customer.buy("Laptop"))
