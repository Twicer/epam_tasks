def get_digits(num):
    if isinstance(num, int) is False:
        print("It's not an int")
        return None
    return [c for c in str(num)]


if __name__ == "__main__":
    print(get_digits(12454))
