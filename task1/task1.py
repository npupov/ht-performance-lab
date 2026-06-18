import sys

def get_path(n, m):
    path = []
    current = 1
    while True:
        path.append(str(current))
        current = ((current + m - 2) % n) + 1
        if current == 1:
            break
    return ''.join(path)

def main():
    args = sys.argv[1:]
    if len(args) < 3:
        return
    
    n1 = int(args[0])
    m1 = int(args[1])
    n2 = int(args[2])
    
    path1 = get_path(n1, m1)
    path2 = get_path(n2, m1)
    
    print(path1 + path2)

if __name__ == "__main__":
    main()
