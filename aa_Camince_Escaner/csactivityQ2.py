class Plant:
    def __init__ (self, name, health, damage):
        self.name = name 
        self.health = health
        self.damage = damage

    def attack(self, DmgZom):
          DmgZom.take_dmg(self.damage)
          print(f"{self.name} attacks {DmgZom.name}")

    def take_dmg(self, Dmgtake):
         self.health = self.health - Dmgtake
         print(f"{self.name} took {Dmgtake} damage.")



class Zombie:
    def __init__ (self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def attack(self, DmgPlt):
         DmgPlt.take_dmg(self.damage)
         print(f"{self.name} attacks {DmgPlt.name}")

    def take_dmg(self, DmgTakeZ):
         self.health = self.health - DmgTakeZ
         print(f"{self.name} took {DmgTakeZ} damage.")

    def move(self, moveZ):
          self.distance = max(0, self.distance - moveZ)
          print(f"King Julian made the Zombie move it move it by {moveZ}")

#create Plant object
plant1 = Plant("Cattail", 300, 50)
plant2 = Plant("Electric Blueberry", 300, 100)

#create Zombie object
zombie1 = Zombie("Flag Zombie", 300, 100, 10)


#game loop
turn = 1

print("⊹₊ ˚‧︵‿₊୨ 𝓟𝓵𝓪𝓷𝓽𝓼 𝓥𝓼 𝓩𝓸𝓶𝓫𝓲𝓮𝓼 ୧₊‿︵‧ ˚ ₊⊹")

while True:
     print(f"turn {turn}")

     # plant1 attacks if alive
     if plant1.health > 0:
          plant1.attack(zombie1)

     if zombie1.health <= 0:
          print(f"{zombie1.name} has been unalived! You Win!!")
          break

     # plant2 attacks if alive
     if plant2.health > 0 and zombie1.health > 0:
          plant2.attack(zombie1)


#zombie moves if not already at plant
     if zombie1.distance > 0:
          zombie1.move(1)

#zombie attacks nearest alive plant
     if zombie1.distance == 0 and plant1.health > 0:
          zombie1.attack(plant1)
     elif zombie1.distance == 0 and plant2.health > 0:
          zombie1.attack(plant2)


#display health
     print(f"Cattail health is {plant1.health}")
     print(f"Electric Blueberry health is {plant2.health}")
     print(f"Flag zombie health is {zombie1.health}")


#check if both plants are defeated
     if plant1.health <= 0 and plant2.health <= 0:
          print("Both plants defeated! You lose! Zombie eat ur brein now!")
          break

     turn += 1


