## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x,guess=0.0):
    if average(x,a):
        return average 
    else:
        return improve_guess(guess,x)
    

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(x,a):
    return x+a/2.0

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess,x):
    x=x*1.0
    better_guess=average(guess+x/guess)
    return better_guess


#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)
