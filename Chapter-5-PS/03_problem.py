"""Can we have a set with 18 (int) and '18' (str) as a value in it?"""
'''YES'''

s=set()
s.add(18)
s.add("18")
print(s)