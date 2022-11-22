def main():
    width: int = int(input("Enter Width: "))
    hight: int = int(input("Enter Hight: "))
    area: int = width * hight
    print(f"Area: {area}")


if __name__ == "__main__":
    print("This program takes hight and width off a rectangle and calculates its area")
    main()
