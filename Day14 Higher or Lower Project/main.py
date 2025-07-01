from game_data import data
import art, random

def compare(a, b, current_score):
    print("\n"*20)
    print(art.logo)

    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a['follower_count'] > b['follower_count']:
        result = "a"
    else:
        result = "b"

    if user_choice == result:
        failure = False
        current_score += 1
    else:
        failure = True
        print(f"Sorry, that's wrong. Final score: {current_score}.")

    return current_score, failure


lose = False
score = 0
compare_B = random.choice(data)

while not lose:
    compare_A = compare_B
    compare_B = random.choice(data)
    while compare_A == compare_B:
        compare_B = random.choice(data)
    score, lose = compare(compare_A, compare_B, score)
