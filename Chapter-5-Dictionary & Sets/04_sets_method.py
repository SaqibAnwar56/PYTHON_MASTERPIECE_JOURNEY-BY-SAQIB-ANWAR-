e={1,2,3,4,4,5,6,6,"Suleman"}
print(e,type(e))
#sets can ccontain diff data types

e.add(50)
e.add("Saqib")
print(e)

e.copy()
print(e) #copy whole set

e.clear()
print(e) #make set empty


'''PROPERTIES OF SETS
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.'''

'''Operations of Sets'''

s={1,2,3,4}
print(len(s),type(s))

s.remove(1)
print(s)

print(s.pop())
