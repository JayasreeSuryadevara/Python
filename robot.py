# A robot has been given a list of movement instructions. 
# Each instruction is either left, right, up or down, 
# followed by a distance to move. The robot starts at 0, 0. 
# You want to calculate where the robot will end up and 
# return its final position as a list. For example, 
# if the robot is given the instructions
# ["right 10", "up 50", "left 30", "down 10"], 
# it will end up 20 left and 40 up from where it started, 
# so you should return [-20, 40].

def robot(movements):
  end_position = [0,0]
  for move in movements:
    direction = move.split(" ")
    if direction[0] == "up":
      end_position[1] += int(direction[1])
    if direction[0] == "down":
      end_position[1] -= int(direction[1])
    if direction[0] == "right":
      end_position[0] += int(direction[1])
    if direction[0] == "left":
      end_position[0] -= int(direction[1])

  return end_position


print(robot(["right 10", "up 50", "left 30", "down 10"]))
