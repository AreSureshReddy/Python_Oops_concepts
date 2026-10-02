class Notification:
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self,message):
        return f"Email Sent: {message}"
class SMSNotification(Notification):
    def send(self,message):
        return f"SMS Sent: {message}"
class WhatsAppNotification(Notification):
    def send(self,message):
        return f"WhatsApp Message Sent: {message}"

