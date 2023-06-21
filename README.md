# sonos-controller
**sonos-controller** is a controller for your Sonos multiroom audio system using Python, for Windows. Using **sonos-controller** you'll be able to control the volume of your Sonos zones using the native media keys on your keyboard. Hold the combo key (default is left shift), and use your volume controls to adjust the volume of the selected zone. To switch a zone, hold the combo key and use the left & right arrows to navigate.

### Getting Started
To start off, we must add players to the configuration file. It's recommended you have static IP addresses set for your speakers. Opening _config.xml_, you'll see an example configuration that looks as such.
```
<WinSonos>
	<Configuration>
		<VolumeInterval>2</VolumeInterval>
		<ComboKey>SHIFT_L</ComboKey>
	</Configuration>
	<Players>
		<Player>192.168.1.123</Player>
		<Player>192.168.1.124</Player>
	</Players>
</WinSonos>
```
Simply add the IP addresses of each player. You can add or remove as many players as needed. **sonos-controller** will list the players in the navigation as they are ordered in the config. The combo key can be set as either _SHIFT_L_ (left shift), or _SHIFT_R_ (right shift). Lastly, the volume interval is the percentage change on the volume up and down events.

To start **sonos-controller**, run the file _run.bat_. If not already installed, install Python 3 from the Windows Store. Upon first startup, a Python virtual environment will be created and the required dependencies will be installed.

To exit **sonos-controller**, hold the escape key, then hold the shift key and release the escape key.
