from abc import ABC, abstractmethod

# Interfaces are designed to define the rules of which classes tha implement this interface should follow

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None:
    pass


class EmailNotificationSender(NotificationSender):
  def send_notification(self, message):
    print(f'Email message - {message}')

class SMSNotificationSender(NotificationSender):
  def send_notification(self, message):
    print(f'SMS message - {message}')


class Notificator:
  def __init__(self, notification_sender: NotificationSender):
    self.__notification_sender = notification_sender

  def send(self, message: str) -> None:
    self.__notification_sender.send_notification(message)


obj = Notificator(SMSNotificationSender())
obj.send('Hello World')