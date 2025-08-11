#Not supporting Gambling
#Just implementing the logic behin Slot Machine
#It is for 3X3 slot machine

import random

MAX_LINE = 3 #Global variable
MAX_BET = 100 #Global variable
MIN_BET = 1 #Global variable

ROWS = 3 #rows of slot machine
COLS = 3 #Columns of slot machine

#symbols in Slot Machine

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

#reward multiplier
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    #print(get_slot_machine_spin(ROWS, COLS, symbol_count))     
    #['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
    
    #with next segment we are making columns of symbol. So first we make a loop for column and the in that a loop for rows.
    #in one column iteration a row is created. A row is consisted of 3 symbols.
    #in 3 column iterations 3 rows and 3 columns are created
    columns = [] 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    ##print(get_slot_machine_spin(ROWS, COLS, symbol_count)) 
    #[['D', 'C', 'A'], ['B', 'D', 'C'], ['D', 'D', 'D']]
    
    return columns

def print_slot_machine(columns):
    #here we are looping through every single row
    for row in range(len(columns[0])):
        #here for every single row ,we are looping through every single column and printing the current row
        for i, column in enumerate(columns): #enumerate will give you index
            if i != len(columns) -1:
                print(column[row], end=" | ") #putting end to create new line 
            else :
                print(column[row], end="")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines=[]
    #with this loop we are checking each row of the column
    #the we check the first element of the 1st column in that row with the next loop.
    #if the 1st columns element matches with the 2nd columns element then the loop will go on to check the 3rd columns elemnet of that row
    #it will go on like this.
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit():
    while True:
        amount = input("Please enter your deposit amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount has to be greater than 0")
        else:
            print("Please enter a valid number.")

    return amount
    #print(amount)




def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines you want to bet on: (1-" + str(MAX_LINE) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of Lines")
        else:
            print("Please enter a number.")

    return lines
    
def get_bet():
    while True:
        amount = input("What amount you would like to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount has to be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough balance. Be in your ${balance} limit")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on line", *winnning_lines) # * it passes every line that you have won
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to Quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"you left with ${balance}")

main()