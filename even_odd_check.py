while True:
    def even_odd_check(num4):
        if num % 2 == 0:
            print("Even Number!")
        else:
            print("Odd Number!")
            
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting the program.")
        break
    
    num = int(user_input)
    even_odd_check(num)
