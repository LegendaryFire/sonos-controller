from pynput import keyboard
from constants import Windows
from notifications import Notifications


class Worker:
    def __init__(self, config, player):
        """
        Initializes the worker.
        :param config: The configuration class.
        """
        self.__config = config
        self.__player = player
        self.__notifications = Notifications()
        self.__combo_pressed = False
        self.__volume_changed = False
        self.__listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release,
            win32_event_filter=self.__win32_event_filter,
            suppress=False
        )
        self.__notifications.notify_player_changed(self.__player.get_player())
        print(f"Connected to Sonos {self.__player.get_player().player_name}. Current volume set to {self.__player.get_player().volume}%.")

    def __on_press(self, key):
        if key == self.__config.get_combo():
            self.__combo_pressed = True
        elif self.__combo_pressed:
            match key:
                case keyboard.Key.media_volume_up:
                    self.__player.volume_up()
                    self.__volume_changed = True
                case keyboard.Key.media_volume_down:
                    self.__player.volume_down()
                    self.__volume_changed = True
                case keyboard.Key.media_volume_mute:
                    self.__player.volume_mute()
                    self.__volume_changed = True
                case keyboard.Key.left:
                    self.__player.previous_player()
                    self.__notifications.notify_player_changed(self.__player.get_player())
                case keyboard.Key.right:
                    self.__player.next_player()
                    self.__notifications.notify_player_changed(self.__player.get_player())

    def __on_release(self, key):
        # To quit the listener hold Escape, hold Shift then release Escape.
        if key == keyboard.Key.esc and self.__combo_pressed:
            return False  # This will quit the listener
        elif key == self.__config.get_combo():
            if self.__volume_changed:
                self.__volume_changed = False
                self.__notifications.notify_volume_changed(self.__player.get_player())
            self.__combo_pressed = False

    def __win32_event_filter(self, msg, data):
        # If there was a key down or up event, and the key was in the list of keys to suppress.
        if (msg == Windows.WM_KEYDOWN or msg == Windows.WM_KEYUP) and data.vkCode in Windows.VK_LIST:
            self.__listener._suppress = self.__combo_pressed  # Only suppress if combo key is pressed.
        # Any other event.
        else:
            self.__listener._suppress = False
        return True

    def start_listening(self):
        """
        Starts listening for key events to control Sonos speaker volume.
        :return: Returns none.
        """
        with self.__listener as worker:
            worker.join()
