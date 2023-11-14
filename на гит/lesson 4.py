person = {"name": "John", "age": 30}
new_data = {"age": 31, "country": "Rus"}
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
git = {}
for got in (person, new_data, my_dict):
    git.update(got)
print(git)