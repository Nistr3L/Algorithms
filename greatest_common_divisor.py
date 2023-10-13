def gcd(a: int, b: int) -> int:    
    while b != 0:               
        t = b                   
        b = a % b               
        a = t                   
    return abs(a)


def main():
    print("The division-based implementation of Euclidean's algorithm\nfor calculating the Greatest Common Divisor.\n")
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(
            f"gcd({num_1}, {num_2}) = "
            f"{gcd(num_1, num_2)}"
        )
        
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")


if __name__ == "__main__":
    main()