import xml.etree.ElementTree as ET
from pynput import keyboard


class Config:
    def __init__(self, file_path):
        """
        Loads the configuration file.
        :param file_path: The file path to the configuration.
        """
        with open(file_path, 'r') as file:
            self.__tree = ET.parse(file)

    def get_players(self):
        """
        Gets a list of the Sonos players from the configuration file.
        :return: Returns the Sonos player's IP address.
        """
        root = self.__tree.getroot()
        child = root.findall('.//Player')
        if len(child) == 0:
            raise AttributeError("Could not find any players in the configuration.")

        player_list = []
        for player in child:
            player_list.append(player.text)

        return player_list

    def get_combo(self):
        """
        Gets the combo key, to be used for volume controls.
        :return: Returns the combo key.
        """
        root = self.__tree.getroot()
        child = root.find('.//ComboKey')
        if child is None:
            return keyboard.Key.shift_l  # Default combo key.

        match child.text.upper():
            case "SHIFT_L":
                return keyboard.Key.shift_l
            case "SHIFT_R":
                return keyboard.Key.shift_r
            case _:
                return keyboard.Key.shift_l  # Default combo key.

    def get_interval(self):
        """
        Gets the volume interval in percentage.
        :return: Returns the volume interval.
        """
        root = self.__tree.getroot()
        child = root.find('.//VolumeInterval')
        if child is None:
            return 3  # Default volume interval.
        else:
            return int(child.text)
