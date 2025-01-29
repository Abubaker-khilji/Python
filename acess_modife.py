#what is access modifiers 
# by default python given every modifiets public
# wesay python mein kuch public private nhi hota hai


class employee:
    def __init__(self):
        self.__name =  "abubaker"
# double undertaker sey yeh baat note hojati k yeh private hojati

a = employee()
print(a.__name)
print(a._employee__name)        # yeh name mangling hai es k zeriye access kr sktay
print(a.__dir__())
 