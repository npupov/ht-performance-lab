import sys
import math

def main():
    if len(sys.argv) < 3:
        return
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    with open(ellipse_file, 'r') as f:
        cx, cy = map(float, f.readline().strip().split())
        rx, ry = map(float, f.readline().strip().split())
    
    with open(points_file, 'r') as f:
        points = [line.strip().split() for line in f.readlines()]
    
    for point in points:
        if not point:
            continue
        x, y = map(float, point)
        value = ((x - cx) ** 2) / (rx ** 2) + ((y - cy) ** 2) / (ry ** 2)
        if abs(value - 1.0) < 1e-10:
            print(0)
        elif value < 1.0:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()
