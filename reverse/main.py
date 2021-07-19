

def reverse(x: int) -> int:
    test_num = 0
    while x > 0:
        remainder = x % 10
        test_num = (test_num * 10) + remainder
        x = x // 10
    return test_num



def main():
    x = reverse(-123)
    print(x)
if __name__ == "__main__":
    main()