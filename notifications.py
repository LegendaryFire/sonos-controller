from notifypy import Notify


class Notifications:
    def __init__(self):
        self.__notification = Notify(default_notification_title="Sonos Controller",
                              default_notification_application_name="Sonos Controller",
                              default_notification_audio="./silent.wav",
                                     default_notification_icon="./sonos.png")
        self.__notification.title = "Sonos Controller by Tristan Balon"
        self.__notification.message = "Welcome to the Sonos Controller. To begin, use your combo key and change the " \
                                      "volume."
        self.__notification.send()

    def notify_volume_changed(self, player):
        self.__notification.message = f"Volume set to {player.volume}%."
        self.__notification.title = f"Sonos {player.player_name}"
        self.__notification.send(block=False)

    def notify_player_changed(self, player):
        self.__notification.message = f"Connected to Sonos {player.player_name}. Current volume is {player.volume}%."
        self.__notification.title = f"Sonos {player.player_name}"
        self.__notification.send(block=False)