import numpy as np

with open("data.txt", "r") as file:
    grid = [list(line.strip()) for line in file]
mymap = np.array(grid)
print(mymap)

# finding the starting position:
num_rows, num_cols = mymap.shape
start = np.where(mymap == "^")
row, col = start[0][0], start[1][0]
print(f"Guard's starting position: ({row}, {col})")
visited_positions = set()
visited_positions.add((row, col))
direction = "up"

# guard track:
while True:
    current_position = mymap[row, col]
    if current_position == "#":
        # changing direction
        if direction == "up":
            direction = "right"
            row += 1 # to stay below #
        elif direction == "right":
            direction = "down"
            col -=1
        elif direction == "down":
            direction = "left"
            row -= 1
        elif direction == "left":
            direction = "up"
            col += 1
        else:
            break
    try:   
        if direction == "up":
            row -= 1  # Move up
        elif direction == "right":
            col += 1  # Move right
        elif direction == "down":
            row +=1 # Move down
        elif direction == "left":
            col -= 1 # move left
        
        if mymap[row, col] != "#":
            visited_positions.add((row, col))
            
    except IndexError:
        print(f"Guard existed at ({row}, {col}).")
        break
    

print(f"Total moves: {len(visited_positions)}")

