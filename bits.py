#Name: Anton Durham
#Desc: This program is designed so that the user can input a number(n),
# and the output will show all the unique ways to organize n-bits
#Date: 2/07/2019

import itertools
def nbits(n):
    return [''.join(x) for x in itertools.product('01', repeat=n)]
    #This product function utilizes tuples and repetitions for its parameters, and is a standard function in the Python 2 library. Tuples are similar to
    #lists, but elements in a tuple are not changable.
    #Product(A, repeat=4) means the same as product(A, A, A, A).
    #
    #Tuples is used here to speed this function up, because iterating through tuples are is quicker than lists.
    #Please see product function explanation below my final print statement.


def main():
    n = input("Enter the number of bits to be shown: ")
    i = int(n)
    xpo = pow(2,i)
    print("There are ", xpo , " unique ways to arrange ", n , " bits")
    print("Possibilities")
    print("================")
    return i

print(nbits(main()))



#def product(*args, **kwds):

    #The product function accepts two arguments: an iterable list(tuple that is **args), and the amount of repititions to be carried out(repititions is **kwds).
    #This function works in my program by creating a lexicographic (basic ordered dictionary format - ant, bat, cat, cow, dog)
    #ordering so that if the input’s iterables are sorted, the product tuples are output in sorted order.

    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    #pools = map(tuple, args) * kwds.get('repeat', 1)

    #this map function returns a list of the results after applying the given function to each item of a given iterable
    
    #the repeat function makes an iterator that returns an object over and over again;
    #the object it is returning is the amount of orderings that the user inputs.
    #Repeat function repeats the object as many times as you want, which is why I used n. 
    #result = [[]]
    #for pool in pools:
        #result = [x+[y] for x in result for y in pool]
        
    #for prod in result:
        #yield tuple(prod)
    
    #Tuple function is used to create a tuple for the prod variable so we can return it.
    #Yield is used because we want to return a generator object: each new sorted list (Ax -->Ay -->Bx)
    #Generators are iterators, an iterable object you can only iterate over once.
    #Generators do not store all values in memory, they are not saved after each iteration
