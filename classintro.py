
class Apple:  # class, concept
    type = "fruit"
    def __init__(self, loc = "tree", clr = "red"):
        self.__location = loc
        self.__color = clr

    def get_location(self):
        return self.__location
    
    def get_color(self): 
        return self.__color

    def _set_location(self, loc):
        self.__location = loc

    def drop(self):
        if self.__location == "tree":
            self._set_location("ground")
            print ("I dropped")
        else:
            print ("I connot be dropped")


x = Apple("tree", "red") # object, tangible, implicitely calls __init__
y = Apple()
z = Apple(clr="yellow")

z.drop() # if I designate drop function as public then ok. otherwise should not be allowed.

x.drop() # Actually calls Apple.drop(x)

print (x.type)


