print('How many cats do you have')
numCats=input()
try:
    if int(numCats)>=4:
        print('That is a lot of cats.')
    elif int(numCats)>=0:
        print('That is not to many cats.')
    elif int(numCats)<=0:
        print('Use a real number.')
    
except ValueError:
    print('You did not enter a number.')

    
