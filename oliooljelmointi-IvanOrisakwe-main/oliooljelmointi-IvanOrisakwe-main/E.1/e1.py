while True:
        numbers = int(input("Enter a number 1- 100 (or type 0 to exit): "))
        if numbers == 0:
            print("Exiting the program.")
            break
        if 1 <= numbers <= 100:
            if numbers % 3 == 0 and numbers % 5 == 0:
                print("Hui Hai")
            elif numbers % 5 == 0:
                print("Hai is printed")
            elif numbers % 3 == 0:
                print("Hui")
            else:
                print(f"{numbers} is not divisible by 3 or 5")
        else:
            print("Please enter a number between 1 and 100")