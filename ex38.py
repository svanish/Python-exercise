ten_things = "Apples oranges crows telephone light sugar"

print "\nWait there is not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "\nAdding: ", next_one
    stuff.append(next_one)
    print "\nThere is %d items now." % len(stuff)
	
print "\nThere we go: ",stuff

print "\nLet's do some things with stuff."

print stuff[0]
print stuff[-1]
print stuff.pop()
print ' ' .join(stuff)
print '#'.join(stuff[3:5])