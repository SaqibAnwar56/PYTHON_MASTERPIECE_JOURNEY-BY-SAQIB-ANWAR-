'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

s = set()
s.add(20)
s.add(20.0) 
s.add('20')
print(s) # 20==20.0 there fore lenth becomes 2
print(len(s),type(s))