def say_hello() -> str:
    return "Hello, world!"


def try_continue():
    a = 0
    b = 2
    while a < 4:
        
        a += 1
        b -= 1
        try:
            print(f"a: {a}, b: {b}")
            a/b
        except ZeroDivisionError:
            print(f"{a}/{b} Error: Division by zero!")
            continue
        finally:
            print("This will always be printed.")
    print(f"{a}, {b} Finished try_continue.")


if __name__ == "__main__":
    print(say_hello())
    try_continue()
