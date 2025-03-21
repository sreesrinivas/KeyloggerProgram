Keylogger Project:-
A simple keylogger implementation using Python and the pynput library. This project is intended for educational purposes and demonstrates how keystrokes can be logged and saved to a file.

Overview:-
This keylogger script captures keystrokes and logs them to a file (keylog.txt). It uses the pynput library to monitor keyboard events and stops logging when the Esc key is pressed.

The project is designed to help users understand how keyloggers work and to demonstrate the importance of cybersecurity awareness. It is not intended for malicious use.

Features:-
Logs regular keystrokes (e.g., letters, numbers, symbols).

Logs special keys (e.g., Shift, Ctrl, Alt) in a readable format.

Stops logging when the Esc key is pressed.

Simple and easy-to-understand code structure.

Installation:-
Prerequisites:

Python 3.x installed on your system.

The pynput library.

Install the pynput library:-
Run the following command to install the required library:

bash
pip install pynput

Download the Script:-
Clone this repository or download the keylogger.py file to your local machine.

Usage:-
Run the Script:
Navigate to the directory containing the script and run it using Python:

bash
python keylogger.py

Start Logging:
The script will start logging keystrokes to a file named keylog.txt in the same directory. A message will be printed to the console:

Keylogger started. Press 'Esc' to stop.

Stop Logging:
Press the Esc key to stop the keylogger. The script will terminate, and the log file will be saved.

View Logs:
Open the keylog.txt file to view the logged keystrokes.

License
This project is licensed under the MIT License.