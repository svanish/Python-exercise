def search(sorted_list, n):
        try:
            index_element = sorted_list.index(n)
            print index_element
        except:
            print -1
			
print "Enter the numbers to be added to the list"
			
sorted_list = [input("> "),
input("> "),
input("> "),
input("> ")]
print "The list is %r" % sorted_list
n = input(">Enter number to find position ")


index_element = search(sorted_list, n)




