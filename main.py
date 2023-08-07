from data import data
from art import logo,vs
import random
print(logo)



def get_account(account):
    name=account["name"]
    description=account['description']
    country=account['country']
    return f"{name}, a {description}, from {country}"

def check_big(guess,followers_a,followers_b):
    if followers_a>followers_b and guess=='a':
        return True
    elif followers_a>followers_b and guess=='b':
        return False
    elif followers_a<followers_b and guess=='a':
        return False
    elif followers_a<followers_b and guess=='b':
        return True
continue_game=True
score=0
account_b = random.choice(data)
while continue_game:

    account_a = account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A:{get_account(account_a)}")
    print(vs)
    print(f"Againist B:{get_account(account_b)}")
    guess=input("Who has more Followers? Type A or B: ").lower()
    followers_a=account_a["follower_count"]
    followers_b=account_b['follower_count']
    print(followers_a)
    print(followers_b)
    correct_guess=check_big(guess,followers_a,followers_b)

    if correct_guess:
        score+=1
        print(f"You are right, your current score is {score}")
    else:
        continue_game=False
        print(f"you lose, your total score is {score}")





