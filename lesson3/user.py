class User:
    def __init__(self, first_name, last_name):
        self.userFirstName = first_name
        self.userLastName = last_name

    def print_first_name(self):
        print(self.userFirstName)

    def print_last_name(self):
        print(self.userLastName)

    def print_full_name(self):
        print(self.userFirstName, self.userLastName)
