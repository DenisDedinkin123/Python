from user import User

my_user = User('Денис', 'Петров')

print(my_user.first_name)
print(my_user.last_name)


def print_first_name(self):
    print(self.first_name)


def print_last_name(self):
    print(self.last_name)


def print_full_name(self):
    print(self.first_name, self.last_name)