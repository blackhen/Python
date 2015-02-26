'''
Challenge : Lab_FindLetter
Program : FindLetter
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
        Karn Niamchan
Date : 1/9/2557 12:37
'''
def findletter(letter, character):
    '''
    Function name : findletter
    input string  -> integer
    '''
    letter = letter.lower()
    character = character.lower()
    print letter.count(character)
findletter(raw_input(), raw_input())
