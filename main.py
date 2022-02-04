"""
There are rules to help people distinguish dots from dashes in Morse code.
The length of a dot is 1 time unit.

A dash is 3 time units.
The space between symbols (dots and dashes) of the same letter is 1 time unit.
The space between letters is 3 time units.
The space between words is 7 time units.
"""
import time
import winsound

# T is the unit time, or dit duration in milliseconds, and W is the speed in wpm.

freq = 600  # Hz
dot = 150  # milliseconds
line = dot * 3

# for sleep
space_words = 0.7
space_letter = 0.03

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": " ",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    ":": "--..--",
    "!": "-.-.--",
    "@": ".--.-."
}
text = input("Enter your text: ").upper()
text_in_morse = []
morse_in_text = []


def morse_encr():
    for c in text:
        text_in_morse.append(morse_code[c])


def morse_decr():
    for valuex in text_in_morse:
        for key in morse_code:
            if valuex == morse_code[key]:
                morse_in_text.append(key)


# ----------------AUDIO---------------------------#
def play_sound_morse(len):
    winsound.Beep(freq, len)


def morse_to_sound():
    for x in text_in_morse:
        if x == " ":
            time.sleep(space_words)
        else:
            for c in x:
                if c == ".":
                    play_sound_morse(dot)
                else:
                    play_sound_morse(line)
                time.sleep(space_letter)


morse_encr()
morse_decr()
print(f"Your Message: ' {''.join(morse_in_text).title()} '\n")
print(f"is encrypted to Morse Code: ' {' '.join(text_in_morse)} '")
choise = input("Wanna hear it? y/n: ")

if choise == "y":
    morse_to_sound()
