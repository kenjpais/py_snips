from typing import List

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

directions = [
    (0, 1), 
    (0, -1), 
    (-1, 0), 
    (1, 0),
]

def solve(maze: List[str], wall: str, start: Point, end: Point):
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []
    
    def walk(curr: Point, path: List[Point]) -> bool:
        ## Pre
        
        # Map out of bounds check
        if (curr.x < 0 or curr.x >= len(maze[0])) or (curr.y < 0 or curr.y >= len(maze)):
            return False
        
        # Wall check
        if maze[curr.y][curr.x] == wall:
            return False
        
        # Check if point has been seen before
        if seen[curr.y][curr.x]:
            return False
        
        # Success case
        if curr.x == end.x and curr.y == end.y:
            path.append(Point(curr.x, curr.y))
            return True
        
        # Mark current position as seen
        seen[curr.y][curr.x] = True
        
        path.append(Point(curr.x, curr.y))
        
        ## Recurse
        # Explore in all directions
        for dx, dy in directions:
            if walk(Point(curr.x + dx, curr.y + dy), path):
                return True
        
        ## Post
        path.pop() # Pop the invalid points ie. after popping invalid points, invalid path is popped effectively
        
        return False

    if walk(start, path):
        print("Path found!")
        print("Path:", path)
    else:
        print("No path exists.")

# Mock mazes and test cases
mock_mazes = [
    # Maze 1: Simple path
    {
        "maze": [
            "##########",
            "#        #",
            "# ####### ",
            "#        #",
            "##########"
        ],
        "start": Point(1, 1),
        "end": Point(8, 3)
    },
    # Maze 2: No path
    {
        "maze": [
            "##########",
            "# ####### ",
            "# ####### ",
            "# ####### ",
            "##########"
        ],
        "start": Point(1, 1),
        "end": Point(8, 3)
    },
    # Maze 3: Complex path
    {
        "maze": [
            "##########",
            "#        #",
            "######   #",
            "#     ####",
            "#        #",
            "##########"
        ],
        "start": Point(1, 1),
        "end": Point(8, 4)
    },
]

# Run tests
for i, test_case in enumerate(mock_mazes, 1):
    print(f"Testing Maze {i}")
    solve(test_case["maze"], wall="#", start=test_case["start"], end=test_case["end"])
    print()
