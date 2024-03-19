def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd

def main():
    odd_values = [odd for odd in odds(3, 45)]
    odds2 = list(odds(21, 45))
    print(odd_values)
    print(odds2)

if __name__ == "__main__":
    main()
