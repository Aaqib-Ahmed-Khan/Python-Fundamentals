names={"aaqib","ahmed","khan","karachi"}
# print(names)
# for x in names:
#     print(x)
# if "ahmed" in names:
#    print("ahmed is in set")
names2={"ahmed","khan","khan2"}
names4=names.union(names2)
print(names4)

# for only duplicates 
names.intersection_update(names2)
print(names)

# keep all values except duplicates
names2.symmetric_difference_update(names)
print(names2)