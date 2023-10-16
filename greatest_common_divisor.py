def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return abs(gcd(b, a % b))

def main():
    print("The recursive-based implementation of Euclidean's algorithm\nfor calculating the Greatest Common Divisor.\n")
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
