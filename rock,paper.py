import random

user_score = 0
computer_score = 0

user_input_dict = {'r': 1, 'p': 2, 's': 3}
opposite_user_input_dict = {1: 'rock', 2: 'paper', 3: 'scissors'}
winning_cases = [(1, 3), (2, 1), (3, 2)]  # (you, computer)

for round in range(1, 4):
    print(f"\n--- Round {round} ---")
    computer = random.choice([1, 2, 3])

    user_input = input('Enter (r=rock, p=paper, s=scissors): ').lower()

    if user_input not in user_input_dict:
        print("Invalid input! Try again.")
        continue

    you = user_input_dict[user_input]

    print(f'Your choice: {opposite_user_input_dict[you]}')
    print(f'Computer choice: {opposite_user_input_dict[computer]}')

    if you == computer:
        print("Result: Draw")
    elif (you, computer) in winning_cases:
        print("Result: You Win this round!")
        user_score += 1
    else:
        print("Result: You Lose this round!")
        computer_score += 1

print("\n=== Final Results ===")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("You win the game!")
elif user_score < computer_score:
    print("Computer wins the game!")
else:
    print("It's a draw!")
