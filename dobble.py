# Interesting dobble game with quick result for improving concentration

from string import *
import random
import time
import pyautogui

def win():
    print("\n\t HURRAY !!! YOU HAVE WON")
    x=input("Press y to continue playing and n to exit")
    if x == 'y':
        dobble()

def lose():
    print(" \n\t OOPS !! YOU LOST")
    x = input("Press y to continue playing and n to exit")
    if x == 'y':
        dobble()
    else :
        pyautogui.hotkey('alt', 'g')

def play(l1,l2,e):
    pyautogui.hotkey('alt', 'g')
    print("\n\t Following are two sets of combinations. \n \t Your job is to find the common element and enter it to win the game")
    print("\n\n\t\t",end=" ")
    for i in l1:
        print(i,end=" ")
    print("\n\n\t\t",end=" ")
    for i in l2:
        print(i,end=" ")
    print("\n")
    a = input("\tEnter the common element here : ")
    if a == e:
        win()
    else:
        lose()

def dobble():
    pyautogui.hotkey('alt', 'g')
    print("\tHELLO This is a toggle Game .\n\n\t\t  Loading...")
    time.sleep(2)
    lst1 = []
    lst2 = []
    symbols = list(ascii_letters)
    u = random.choice(symbols)
    symbols.remove(u)
    u1 = random.randint(0 , 5)
    u2 = random.randint(0 , 5)
    for i in range(6):
        a=random.choice(symbols)
        lst1.append(a)
        symbols.remove(a)
        b = random.choice(symbols)
        lst2.append(b)
        symbols.remove(b)
    lst1.insert(u1,u)
    lst2.insert(u2,u)
    play(lst1,lst2,u)

dobble()