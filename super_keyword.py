class employee:
    def __init__(self ,name, id):
        self.name = name
        self.id = id


class programmer(employee):
    def __init__(self , name,id, lang):
        super().__init__(name,id)
        self.lang = lang


faizan = employee("faizan buddawa",550)
daniyal = programmer("snake coder", 5555001,"java kotlin")

print(faizan.name)
print(faizan.id)
print(daniyal.lang)






           