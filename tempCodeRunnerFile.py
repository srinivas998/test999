def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("sum:", add(a, b))
    print("product:", multiply(a, b))

if __name__ == "__main__":
    main()
    