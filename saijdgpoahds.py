def list_sum(List):
    if List == []:
        return 0
    return List[0] + list_sum(List[1:])

List = [int(x) for x in input("Enter 4 numbers to be separated by spaces: ")]
guess = int(input(f"What is the sum of {List}?: ")) 
print(f"sum of list: {list_sum(List)}, your guess: {guess}")

if guess == list_sum(List):
    print("Your guess was correct")
else:
    print("Your guess was wrong")