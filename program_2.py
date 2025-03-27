def random_number_generator():
  while True:
      try:

        number_of_numbers=int(input("How many random numbers would you like to write to a new file? (1-1000, no negative numbers please):"))
        if number_of_numbers > 1000:
            print("Number must be between 1-1000")
        elif number_of_numbers < 1:
            print("Please enter a number greater than 0")
        else:
            break
      except ValueError:
          print("Invalid input. Please enter a number between 1 and 1000")

  with open("random_numbers.txt",'w') as file:
    for num in range(number_of_numbers):
        file.write(f"{random.randint(1,500)}\n")

  print(f"{number_of_numbers} number(s) were written to a new file named 'random_numbers.txt'.")

if __name__=="__main__":
      random_number_generator()
