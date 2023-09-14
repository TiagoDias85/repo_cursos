class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

my_list = range(1, 11)

for n in my_list:
    an.party()
    #print(n)

print(an.x)
