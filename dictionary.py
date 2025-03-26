phones= {
    "aaqib": 1234,
    "ahmed": 2345,
    "khan": 3456 
}
# print(phones)
# print(type(phones))
# print(len(phones))
# print(phones["aaqib"])
# print(phones.get("ahmed"))
# print(phones.keys())

phones["aaqib"]=4321
print(phones)
phones["aaqib"]=5432
print(phones)

more_phones={
    "kia":2345
}
phones.update(more_phones)
print(phones)
phones.pop("ahmed")
print(phones)
phones.popitem()
print(phones)
 
# phones.clear()
# print(phones)

for x in phones:
 print(x)

for x in phones.items():
 print(x) 
  
  