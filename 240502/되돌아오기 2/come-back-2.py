def return_to_origin(commands):
    directions = ['N', 'E', 'S', 'W'] 
    dx = [0, 1, 0, -1]  
    dy = [1, 0, -1, 0]  
    
    x, y = 0, 0  
    direction_idx = 0  
    visited = set([(0, 0)])  
    time = 0 
    
    for command in commands:
        if command == 'F': 
            x += dx[direction_idx]
            y += dy[direction_idx]
        elif command == 'L':  
            direction_idx = (direction_idx - 1) % 4
        elif command == 'R':  
            direction_idx = (direction_idx + 1) % 4
        
        time += 1 
        
        if (x, y) == (0, 0):
            return time
        

        visited.add((x, y))
    
    return -1


commands = input()

print(return_to_origin(commands))