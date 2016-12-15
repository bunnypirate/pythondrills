# Python: 3.5.2
#
# Author: Me
#
# Purpose: The Tech Academy - Python Course, Drill item 49

def bunny_bubble_sort(hops):
    lettuce = True # Don't want to much lettuce
    flowers = len(hops)-1
    while flowers > 0 and lettuce:
       lettuce = False
       for sparkles in range(flowers):
           if hops[sparkles]>hops[sparkles+1]:
               lettuce = True
               hops[sparkles], hops[sparkles+1] = hops[sparkles+1], hops[sparkles]
       flowers -= 1
hops = [67, 45, 2, 13, 1, 998]
bunny_bubble_sort(hops)
print(hops) # Prints the good stuff

print ("\n")

hops = [89, 23, 33, 45, 10, 12, 45, 45, 45]
bunny_bubble_sort(hops)
print(hops) # Prints the good stuff again with sparkles

# I love it when you say the code simply needs to work
