person = "Jose"
print(f"my name is {person}")

d = {'a': 1, 'b': 2, 'c': 3}
print(f"my number is {d['a']}")

mylist = [0,1,2]
print(f"my number is {mylist[1]}")

library = [('Author', 'Topic' ,'Pages'), ('Twain', 'Rafting', 506),('Feyman', 'Physics',214)]
print(library)

for author, topic, pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:>{10}}")
    

