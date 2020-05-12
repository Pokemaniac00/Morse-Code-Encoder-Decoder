#!/bin/env python

def main():
    print("Welcome to Pokemaniac00's Morse Code Encoder & Decoder.")
    prompt = input("Would you like to encode a message? (respond 'n' to decode a message) (y/n)")
    result = ""
    if(prompt == "y"):
        message = input("Input a message you would like to encode: ")
        result = encode(message.lower())
    else:
        message = input("Input a message you would like to decode: ")
        result = decode(message.lower())
    print(result)

def encode(message):
    result = ""
    switch_cases = {
        'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--..",
        '1': ".----",
        '2': "..---",
        '3': "...--",
        '4': "....-",
        '5': ".....",
        '6': "-....",
        '7': "--...",
        '8': "---..",
        '9': "----.",
        '0': "-----",
        ' ': " "
    }
    for char in message:
        result += switch_cases.get(char, "`")
        result += " "
    
    if '`' in result:
        return "The message contained characters that could not be encoded."
    else:
        return result

def decode(message):
    strings = message.split(None)
    result = ""
    switch_cases = {
        ".-": 'a',
        "-...": 'b',
        "-.-.": 'c',
        "-..": 'd',
        ".": 'e',
        "..-.": 'f',
        "--.": 'g',
        "....": 'h',
        "..": 'i',
        ".---": 'j',
        "-.-": 'k',
        ".-..": 'l',
        "--": 'm',
        "-.": 'n',
        "---": 'o',
        ".--.": 'p',
        "--.-": 'q',
        ".-.": 'r',
        "...": 's',
        "-": 't',
        "..-": 'u',
        "...-": 'v',
        ".--": 'w',
        "-..-": 'x',
        "-.--": 'y',
        "--..": 'z',
        ".----": '1',
        "..---": '2',
        "...--": '3',
        "....-": '4',
        ".....": '5',
        "-....": '6',
        "--...": '7',
        "---..": '8',
        "----.": '9',
        "-----": '0'
    }
    for s in strings:
        result += switch_cases.get(s, "`")
        result += " "
    
    if '`' in result:
        return "The message contained characters that could not be decoded."
    else:
        return result.upper()

main()