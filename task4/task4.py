import sys

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves

def main():
    if len(sys.argv) < 2:
        return
    
    file_path = sys.argv[1]
    
    with open(file_path, 'r') as f:
        nums = [int(line.strip()) for line in f.readlines() if line.strip()]
    
    moves = min_moves_to_equal(nums)
    
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()
