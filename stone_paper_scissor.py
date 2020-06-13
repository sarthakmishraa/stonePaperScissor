#stone paper scissor by Sarthak Mishra
import random

print('____Stone Paper Scissor____')
print('It\'s a 5 point game whoever scores 5 points first, wins!')
print('s for stone')
print('p for paper')
print('x for scissor')

i=0
j=0
while i<5 and j<5:
        n = input('Input : ')

        r = random.randint(1,4)

        if r == 1:
                comp = 's'
                print('Computer\'s choice : ' , comp)
        elif r == 2:
                comp = 'p'
                print('Computer\'s choice : ' , comp)
        elif r == 3:
                comp = 'x'
                print('Computer\'s choice : ' , comp)

        if n == 's' and comp == 'p':
                print('You selected stone and computer selected paper')
                print('PC won!')
                i = i+1
        elif n == 's' and comp == 'x':
                print('You selected stone and computer selected scissor')
                print('You won!')
                j = j+1
        elif n == 'p' and comp == 's':
                print('You selected paper and computer selected stone')
                print('You won!')
                j = j+1
        elif n == 'p' and comp == 'x':
                print('You selected paper and computer selected scissor')
                print('PC won!')
                i = i+1
        elif n == 'x' and comp == 's':
                print('You selected scissor and computer selected stone')
                print('PC won!')
                i = i+1
        elif n == 'x' and comp == 'p':
                print('You selected scissor and computer selected paper')
                print('You won!')
                j = j+1
        elif n == comp:
                print('Both players chose same item')
        else:
                print('Invalid Input')
        print('PC : ',i , 'You : ',j)
print('Final Scores \n You : ',j ,'PC : ',i)