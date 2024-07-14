#Create function for adding program
def adding_program(number_1, number_2):
    add_numbers = (number_1 + number_2)
    return add_numbers

def main():
    number_1 = int(input('First Number: '))
    number_2 = int(input('Second Number: '))
    total = adding_program(number_1, number_2)
    print(total)

#Run program
print('Start')
main()
print('Finish')