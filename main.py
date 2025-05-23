print("Test")

# inputs for number of wolves and sheep
n = int(input("Wolves: ")) # number of wolves
m = int(input("Sheep: ")) # number of sheep

# make two lists for each side of the river
starting_side = []
ending_side = []

# add wolves and sheep to the starting side
for i in range(n):
    starting_side.append("wolf")
for i in range(m):
    starting_side.append("sheep")

# function for counting the number of wolves and sheep
def count_animals(side):
    wolves = 0
    sheep = 0
    for animal in side:
        if animal == "wolf":
            wolves += 1
        elif animal == "sheep":
            sheep += 1
    return wolves, sheep

def is_safe(side):
    wolves, sheep = count_animals(side)
    # if there are more wolves than sheep, the sheep will be eaten
    if wolves > sheep and sheep > 0:
        return False
    return True

boat_location = "start"
boat = []

steps = 0
while True:
    print("Steps: ", steps)
    print("Starting side: ", starting_side)
    print("Ending side: ", ending_side)
    print("Boat location: ", boat_location)

    if len(starting_side) == 0:
        print("Success")
        break

    if not is_safe(starting_side) or not is_safe(ending_side):
        print("Failure")
        break

    boat.clear()
    boat = starting_side[:2]
    del starting_side[:2]
        
    boat_location = "end"

    ending_side.extend(boat)
    boat.clear()

    if starting_side and ending_side:
        return_animal = ending_side.pop()
        starting_side.append(return_animal)
        boat_location = "start"
    
    steps += 1