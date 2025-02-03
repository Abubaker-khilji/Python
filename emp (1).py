class employee:
    def __init__(self, name):
     self.name = name
    def __len__(self):
        for c in self.name:
         i =  0   
         i = i + 1
         return i
        
    def __str__(self):
        return f"employee {self.name}"
    def __repr__(self):
        return f"employee {self.name}"    