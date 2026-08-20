"""Observers can be regular objects."""
class EmailSubscriber:
    def update(self, event): print("email:", event)
class Newsletter:
    def __init__(self): self.subscribers = []
    def publish(self, event):
        for subscriber in self.subscribers: subscriber.update(event)

news = Newsletter(); news.subscribers.append(EmailSubscriber()); news.publish("new post")
