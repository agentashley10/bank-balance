# PIN authentication
correct_pin = "1234"
pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Incorrect PIN. Access denied.")
    exit()

print("PIN correct. Welcome to your bank account!")
balance = 0 # Starting balance is 0

while True:
  print("\n--- Simple Bank Menu ---")
  print("1. Check balance")
  print("2. Deposit money")
  print("3. Withdraw money")
  print("4. Exit")

  choice = input("Choose an option (1-4): ")

  if choice == "1":
    print("Your current balance is £" + "{:.2f}".format(balance))

  elif choice == "2":
    deposit = float(input("Enter amount to deposit: £"))
    if deposit > 0:
      balance += deposit
      print("Deposit successful!")
    else:
      print("Enter a positive amount.")
    print("Updated balance: £" + "{:.2f}".format(balance))

  elif choice == "3":
    withdraw = float(input("Enter amount to withdraw: £"))
    if withdraw > balance:
      print("Insufficient funds.")
    elif withdraw <= 0:
      print("Enter a positive amount.")
    else:
      balance -= withdraw
      print("Withdrawal successful!")
    print("Updated balance: £" + "{:.2f}".format(balance))

  elif choice == "4":
    print("Goodbye!")
    restart = input("Would you like to restart the bank menu? (y/n): ").lower()
    if restart != 'y' and restart != 'yes':
      print("Thank you for using our banking system!")
      break

  else:
    print("Invalid option. Please choose 1-4.")