from notification import (
    EmailNotification,
    SMSNotification,
    WhatsAppNotification
)

notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

message = "Your order has been shipped."

for notification in notifications:
    print(notification.send(message))