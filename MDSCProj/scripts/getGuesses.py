from MDSCApp.models import Guess

def run(*args):
    try:
        x = Guess.objects.filter(puzzle=int(args[0]))
        if args[1] == "0":
            for i in x:
                print(f'{i.studentId} {i.name}: {i.guess}')
        else:
            rawGuesses = [i.guess for i in x]
            uniqueGuesses = list(set(rawGuesses))
            z = [(i, rawGuesses.count(i)) for i in uniqueGuesses]
            z = sorted(z, key=lambda i:i[0])
            z = sorted(z, key=lambda i:i[1])
            for i in z:
                print(f'{i[1]} {i[0]}')
    except:
        print("Error")
        print(args)
    

