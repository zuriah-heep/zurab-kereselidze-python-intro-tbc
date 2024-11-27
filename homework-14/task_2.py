def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2 ,  (y1 + y2) / 2

def main():
    print(midpoint(1, -5, 3, 5))
    print(midpoint(0, 15, 10, 20))
    print(type(midpoint(0, 15, 10, 20)))

if __name__ == "__main__":
    main()