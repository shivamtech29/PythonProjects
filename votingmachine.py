# Voting Machine in less than 60 lines of clean code

import pyautogui
import time

def voteloop(votedct,n):
    p=[]
    for i in range(n):
        p.append(0)
    c='y'
    while c=='y':

        u = 0
        for i in votedct:
            print("\t\t\t{} : {}".format(u+1, i))
            u += 1
        x = int(input("\tEnter your vote choice here : "))
        p[x-1] = p[x-1]+1

        print("\tYour vote has been recorded. Now press y to confirm...")
        c = input("\tConfirm ... ")
        print("\tThanks for Voting")
        time.sleep(2)
        pyautogui.hotkey('alt', 'g')

    pyautogui.hotkey('alt', 'g')
    print("\n\tProcessing the Results...")
    time.sleep(2)
    pyautogui.hotkey('alt', 'g')
    print("\n\tFinally the results are out...")
    d = max(p)
    for i in range(n):
        if d==p[i]:
            name=votedct[i]
    print("\n" * 2)
    print("\tAnd the WINNER of Elections 2020 is {} with votes".format(name,d))


def startvote():
    print("\n"*30)
    p=int(input("Enter the number of parties to compete : "))
    votedct = []
    for i in range(p):
        k=input("Enter Contestant name")
        votedct.append(k)
    print("\tInstructions: choose the given options then Press Enter and confirm your result by pressing 'y'\n")
    print("\tYOU HAVE {} CHOICES ".format(p))
    u=0
    for i in votedct:
        print("\t\t\t{} : {}".format(u,i))
        u+=1
    time.sleep(2)
    pyautogui.hotkey('alt', 'g')
    voteloop(votedct,p)

startvote()