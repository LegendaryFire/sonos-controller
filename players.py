from soco import SoCo


class Players:
    def __init__(self, config):
        self.__config = config
        self.__players = config.get_players()
        self.__cursor = 0

        # Initial setup of the player.
        self.__update_player()

    def get_player(self):
        """
        Gets the currently selected player IP address.
        :return: Returns the IP address of the selected player.
        """
        return self.__current_player

    def next_player(self):
        """
        Sets the current player to the next player in the list.
        :return: Returns None.
        """
        if self.__cursor == len(self.__players) - 1:
            self.__cursor = 0
        else:
            self.__cursor += 1

        self.__update_player()

    def previous_player(self):
        """
        Sets the current player to the previous player in the list.
        :return: Returns none.
        """
        if self.__cursor == 0:
            self.__cursor = len(self.__players) - 1
        else:
            self.__cursor -= 1
        self.__update_player()

    def volume_up(self):
        """
        Raises the volume by the interval set in the configuration.
        :return: Returns none.
        """
        player = self.__current_player
        volume_interval = self.__config.get_interval()
        player.set_relative_volume(volume_interval)

    def volume_down(self):
        """
        Lowers the volume by the interval set in the configuration.
        :return: Returns none.
        """
        player = self.__current_player
        volume_interval = self.__config.get_interval() - (self.__config.get_interval() * 2)
        player.set_relative_volume(volume_interval)
        print(f"Sonos {player.player_name}: Volume lowered to {player.volume}%.")

    def volume_mute(self):
        """
        Toggles muting the volume.
        :return: Returns none.
        """
        player = self.__current_player
        if player.mute is False:
            player.mute = True
            print(f"Sonos {player.player_name}: Volume muted.")
        else:
            player.mute = False
            print(f"Sonos {player.player_name}: Volume unmuted. Current volume is {player.volume}%.")

    def __update_player(self):
        self.__current_player = SoCo(self.__players[self.__cursor])