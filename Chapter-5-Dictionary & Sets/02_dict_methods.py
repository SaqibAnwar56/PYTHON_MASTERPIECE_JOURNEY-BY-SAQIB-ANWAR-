marks={
    "Saqib":50,
    "Aaqib":89,
    "Atif":87,
    0:"Saqib"
}
print(marks.items()) # return in item style
print(marks.keys())# return keys
print(marks.values())# return values
marks.update({"Saqib":30,"Babar":100}) # update or add kr skte he
print(marks)
print(marks.get("Babar"))# return particular matching
print(marks.get(0))
print(marks.copy()) #COPY WHOLE DICT
print(marks.clear()) # clear whole dict

# "IMP RULE"
# print(marks.get("Babar2"))# returns none if not find not showing any error
# print(marks["Babar2"])# it shows error there is any type of dict present