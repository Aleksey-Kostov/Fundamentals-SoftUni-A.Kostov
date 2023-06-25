class Email:
    def __init__(self, senders, receivers, contents):
        self.senders = senders
        self.receivers = receivers
        self.contents = contents
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.senders} says to {self.receivers}: {self.contents}. Sent: {self.is_sent}"


emails = []
mail = input()
while mail != "Stop":
    tokens = mail.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    mail = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))
for i in send_emails:
    emails[i].send()
for email in emails:
    print(email.get_info())
