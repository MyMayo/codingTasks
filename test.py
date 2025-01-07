
class Email:

    def __init__(self, email_address, Subject_line, email_content):
        self.email_address = email_address
        self.Subject_line = Subject_line
        self.email_content = email_content
        self.has_been_read = False
        
    def mark_as_read(self):
        self.has_been_read = True


inbox = []


def populate_inbox(self):
    email_list = [
            ("boldman@dmail.com", "Fish dont fart", "U sure?"),
            ("rabies@dmail.com", "The end is near", "Hi there"),
            ("unicorn@dmail.com", "Life is beautiful", "I believe so")
        
        ]
    inbox.append(email_list)


def list_emails(self):
    for index, email in enumerate(inbox):
        print(index)


x = print(int(input("Please insert email no. you wanna open:")))

def read_email(inbox):
    if x == 0:
        return inbox(0)
        print(mark_as_read)
    elif x == 1:
        return inbox(1)
        print(mark_as_read)
    elif x == 2:
        return inbox(2)
        print(mark_as_read)
    else:
        print("Wrong choise")


