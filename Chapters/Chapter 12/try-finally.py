def main():
    try:
        a=int(input("Enter number 1:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:                       #This runs even if the try is sucessful or the exception is met or even if the function returns
        print("I am inside of finally block")

main()