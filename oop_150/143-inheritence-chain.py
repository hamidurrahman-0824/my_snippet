#inheritance chain#amphibia,reptelia,aves,mamalia
#ability,compare,invent,belongs,update,
class Choradata:
    species = []
    def __init__(self,name):
        self.name = name
        Choradata.species.append(name)
        self.names = []
        self.chars = ['Chordet','developed','structered-heart...']
    def ability(self):
        print(self.name,"Can do that ____")
    def belongs_to(self,name):
        if name in Choradata.species:
            print('It belongs to chordata')
        elif name == ['Chordet','developed','structered-heart...']:
            print('Its is chorted for having fundamental characteristics of chordet.')
        else:
            print('Perhaps it belongs to other class')
    def addspcs(self,name):
        if name not in Choradata.species:
            Choradata.species.append(name)
            print("Congrats you discovered something new!")
        else:
            print("Already discovered")
    def update_chars(self,lst):
        if isinstance(lst,list):
            self.chars.extend(lst)
            print(f"Updated charecteristics", self.chars)
        else:
            self.chars.append(lst)
            print(f"Updated charecteristics", self.chars)
class Mamals(Choradata):
#char,update,
    def __init__(self, name):
        self.list = []
        self.list.append(name)
        self.chars = []
    def addchars(self,lst):
        self.chars+=lst
    def ability(self):
        self.ablty = ['swim','generate-milk']
    
class Human(Mamals):
    def __init__(self, name):
        self.name = name
        self.chars = []
    def addchars(self, lst):
        self.chars + list(lst)
#help
class Chordata:
    def __init__(self, name):
        self.name = name
        self.chars = [
            "notochord",
            "dorsal nerve cord",
            "developed heart"
        ]

    def show_characteristics(self):
        print(f"{self.name} has chordata characteristics:")
        for c in self.chars:
            print("-", c)


class Mammals(Chordata):
    def __init__(self, name):
        super().__init__(name)   # call parent constructor
        self.chars += [
            "warm blooded",
            "hair or fur",
            "produce milk"
        ]

    def mammal_ability(self):
        print(f"{self.name} can produce milk for its young.")


class Human(Mammals):
    def __init__(self, name):
        super().__init__(name)
        self.chars += [
            "high intelligence",
            "language communication"
        ]

    def speak(self):
        print(f"{self.name} can speak and think logically.")
class Animal:
    def __init__(self, name):
        self.name = name
        self.characteristics = ["living organism", "can move"]

    def show(self):
        print(f"\n{self.name}'s characteristics:")
        for c in self.characteristics:
            print("-", c)


class Chordata(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.characteristics += [
            "notochord",
            "dorsal nerve cord",
            "developed heart"
        ]

    def backbone(self):
        print(self.name, "has a backbone.")


class Mammal(Chordata):
    def __init__(self, name):
        super().__init__(name)
        self.characteristics += [
            "warm-blooded",
            "hair or fur",
            "produces milk"
        ]

    def feed_baby(self):
        print(self.name, "feeds babies with milk.")


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.characteristics += [
            "high intelligence",
            "language communication"
        ]

    def speak(self):
        print(self.name, "can speak and think logically.")