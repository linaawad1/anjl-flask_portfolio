from random import choice
from PyInquirer import prompt
import random

print("Wanna see what the future has in store for you in 2023? First see your horoscope based on your zodiac sign:")
while True: # The while loop lets the user input information after an invalid answer
    date = int(input("Enter the day you were born: \n"))
    if date > 31: # maxes out the dates at 31 days per month. Makes sure the input is valid
        print("Enter correct date, cannot exceed 31\n") # As the code runs it checks these conditions then goes to the next iteration of the loop.
        continue
    month = int(input("Enter your birthday month as a number: \n")) # This is the same idea as the day
    if month > 12: # But there are 12 months in the year
        print("Enter the correct month, should not exceed 12\n")
        continue
    break # If there are no issues or invalid answers, the while loop is broken and the code continues executing the following:

# Coders Packet zodiac sign analysis
if month == 12: # This code gives an if-else statement for each of the 12 zodiac signs to determine which zodiac sign the users birthday falls into
    if (date < 22):
        sign = 'Sagittarius' # For example: in the month of december(12) if the birthday you entered is less than 22, then the user is a sagittarius.
    else:
        sign = 'Capricorn' # if they are born in december but not on a day 1-22, then they are a capricorn
elif month == 1: 
    if (date < 20):
        sign = 'Capricorn'
    else:
        sign = 'Aquarius'
elif month == 2:
    if (date < 19):
        sign = 'Aquarius'
    else:
        sign = 'Pisces'
elif month == 3:
    if (date < 21):
        sign = 'Pisces'
    else:
        sign = 'Aries'
elif month == 4:
    if (date < 20):
        sign = 'Aries'
    else:
        sign = 'Taurus'
elif month == 5:
    if (date < 21):
        sign = 'Taurus'
    else:
        sign = 'Gemini'
elif month == 6:
    if (date < 21):
        sign = 'Gemini'
    else:
        sign = 'Cancer'
elif month == 7:
    if (date < 23):
        sign = 'Cancer'
    else:
        sign = 'Leo'
elif month == 8:
    if (date < 23):
        sign = 'Leo'
    else:
        sign = 'Virgo'
elif month == 9:
    if (date < 23):
        sign = 'Virgo'
    else:
        sign = 'Libra'
elif month == 10:
    if (date < 23):
        sign = 'Libra'
    else:
        sign = 'Scorpio'
elif month == 11:
    if (date < 22):
        sign = 'Scorpio'
    else:
        sign = 'Sagittarius'

print("\nYou are a:", sign) # Displays the zodiac sign that aligns with the birthday the user inputted.

user = input("\nNow, do you want to read your future for 2023 based on this discovery?\nEnter yes to read and no to leave\n") # Furthers the programs purpose to show the user their future and give them a self reflection.

if user == 'yes': # Simple if and elif commands that give each zodiac sign a glimpse into their 2023.
    print("Get ready! Your 2023 horoscope based on your zodiac sign:")
    if sign == "Sagittarius":
        print("\nKnow that all significant change you will face this year will take time \n"
              "Time and patience is the most important thing for you! \n"
              "your birthday wishes and dreams may come true this year\n")
    elif sign == 'Capricorn':
        print("\nKnowing your worth is exceptionally important as you will learn this year\n"
              "It will help you reach the fulfillment you need to feel \n")
    elif sign == "Aquarius":
        print("\nYou will have a fresh start this year where you will experience wonderful things!\n")
    elif sign == "Pisces":
        print("\nYou'll experience a sense of being a cosmic hero who confronts their traumas,\n"
              "transforms them into cosmic power,\n"
              "and realizes all of their ambitions.\n")
    elif sign == "Aries":
        print("\nConsider yourself a magnet this year, Aries, whether you're looking for a serious and fulfilling relationship, a more reliable group of friends, a promotion at your dream career, or the materialization of your ideal home.  \n"
              "Believe that the universe is on your side and that you are on the right track to fulfilling your deepest desires.  \n"
              "You are the star of the universe this year, guided by Jupiter and the North Node in your sign.\n")
    elif sign == "Taurus":
        print("\nYour healing process is being asked of you; \n"
              "embrace it and see it as a spiritual adventure rather than a burden.\n"
              "You can decide to make the healing process enjoyable this year!\n")
    elif sign == "Gemini":
        print("\nYou will reinvent yourself into someone special \n"
              "This will need some very precarious care and control \n"
              "Have fun this year don't be too serious.\n")
    elif sign == "Cancer":
        print("\nYou will be redone by the end of the year as an improved version of yourself \n"
              "Your self love will also grow a bunch this coming year. \n"
              "Congrats!!!.\n")
    elif sign == "Leo":
        print("\nThe year in which you completely unveil who you are to yourself.\n"
              "listen to others and don't let your ego get in the way. Remember that teamwork makes the\n"
              "dream work in 2023.\n")
    elif sign == "Virgo":
        print("\nYou'll be in a self-reflective and somewhat introverted mood. \n"
              "You will focus on progress rather than \n"
              "perfection.\n")
    elif sign == "Libra":
        print("\nBe prepared to be noticed and praised Libra. \n"
              "Although 2023 may have started off quiet \n"
              ", the last three months will feel explosive.\n")
    elif sign == "Scorpio":
        print("\nYScorpios might find themselves making an important connection—one they've put a lot of thought and work into—official  \n"
              "or, alternately, saying goodbye to relationships they don't want to continue investing in.  \n"
              "2023 will be the year you finally feel complete since you persisted in making investments in your wellbeing and fostering your prosperity.\n")
    else:
        print("Invalid input. Please try again with correct input.\n")

else:
    print("Goodbye!")

# @bsoyka fortune-teller code inspired. I was inspired by the categories of 3 separate fortune teller games to make the choices more random.
def represents_int(string: str):
    """Checks if a `string can be turned into an integer
    Args:
        string (str): String to test
    Returns:
        bool
    """

    try:
        int(string)
        return True
    except ValueError:
        return False
    
    # This is necessary to provide checks if given string could be converted to an integer. It uses a try and except block to convert the string to an integer using the built-in int() function. True means it is a successful conversion, False is not .
    # We are writing a program that requires the user to input an integer, so this code can validate the input.
   

print("Now that we know our horoscopes based on the moon phases, lets pick a random fortune to determine our luck and prosperity!")
print("Pick a card shape and, once again, welcome to:")

fortunes = [ # These following lists are examples of nested lists. And each has nested dictionaries.
    [ # The outer list represents different categories
        ['Heart', 'Spade', 'Diamond', 'Club'], # This list represents the different cards in a normal card deck
        {
            '1': 'You will learn a lot from your friendships.', # Each number represents another key value that will lead to the final fortune or advice given
            '2': 'A path of death lies in your wake.', # The inner dictionaries hold these numbers and hold the fortunes or advice that are chosen randomly.
            '5': 'You are very special in everyway.',
            '6': "A beautiful, smart, and loving person will be coming into your life.",
        },
        {
            '3': 'A new perspective will come with the new year.',
            '4': 'A pleasant surprise is waiting for you.',
            '7': 'A truly rich life contains love and art in abundance.',
            '8': 'All your hard work will soon pay off.',
        },
    ],
    [
        ['Heart', 'Spade', 'Diamond', 'Club'],
        {
            '1': "Any day above ground is a good day.",
            '2': 'Don’t be discouraged, because every wrong attempt discarded is another step forward.',
            '5': 'Embrace this love relationship you have!',
            '6': 'Every flower blooms in its own sweet time.',
        },
        {
            '3': 'Go take a rest; you deserve it.',
            '4': 'Good news will come to you by mail.',
            '7': "Happiness begins with facing life with a smile and a wink.",
            '8': "He who knows he has enough is rich.",
        },
    ],
    [
        ['Heart', 'Spade', 'Diamond', 'Club'],
        {
            '1': 'If you wish to see the best in others, show the best of yourself.',
            '2': 'Like the river flow into the sea. Something are just meant to be.',
            '5': 'You will become a great philanthropist in your later years.',
            '6': "You will always have good luck in your personal affairs.",
        },
        {
            '3': 'You will be traveling and coming into a fortune.',
            '4': "You will always be surrounded by true friends.",
            '7': 'There is no wisdom greater than kindness.',
            '8': 'You will inherit a large sum of money.',
        },
    ],
]

fortune_num = choice(range(len(fortunes))) # This code generates a random number between 0 and the length of the fortunes list minus 1, # and assigns it to the variable fortune_num using a choice() function from the random we imported earlier.
print('Fortune Teller #{}'.format(fortune_num + 1)) # There are 3 fortunes for the 3 different categories above.
fortune = fortunes[fortune_num] # any of the fortune numbers could be chosen
lol_0 = fortune[0]
lol_1 = fortune[1]
lol_2 = fortune[2]
lol = 0
print()

user_input = prompt(
    [
        { # another dictionary that holds the different steps in order to showcase the fortune
            'type': 'list',
            'name': 'answer',
            'message': 'Pick a card, any card:',
            'choices': lol_0,
        }
    ]
)['answer']

if represents_int(user_input):
    movement = int(user_input) # these are helpful controls that let the program run the way it does with arrows and all.
else:
    movement = len(user_input)

for _ in range(movement):
    lol += 1
    if lol == 3:
        lol = 1
print()

if lol == 1:
    user_input = prompt(
        [
            { # dictionary
                'type': 'list',
                'name': 'answer',
                'message': 'Pick a card, any card:',
                'choices': lol_1,
            }
        ]
    )['answer']
elif lol == 2:
    user_input = prompt( # this user input is very important and their choices dictate the fortune they get
        [
            { # dictionary
                'type': 'list',
                'name': 'answer',
                'message': 'Pick a card, any card:',
                'choices': lol_2,
            }
        ]
    )['answer']

if represents_int(user_input):
    movement = int(user_input)
else:
    movement = len(user_input)

for _ in range(movement):
    lol += 1
    if lol == 3:
        lol = 1

print()

if lol == 1:
    user_input = prompt(
        [
            { # dictionary
                'type': 'list',
                'name': 'answer',
                'message': 'Pick a card, any card:',
                'choices': lol_1,
            }
        ]
    )['answer']
    print()
    print('One thing the future wants you to know is:')
    print(lol_1[user_input])

elif lol == 2:
    user_input = prompt(
        [
            { # dictionary
                'type': 'list',
                'name': 'answer',
                'message': 'Pick a card, any card:',
                'choices': lol_2,
            }
        ]
    )['answer']
    print()
    print('One thing the future wants you to know is:')
    print(lol_2[user_input])


def spin_wheel_of_fortune(user): # Imitates spinning a wheel of fortune for a year of 365 days.
    # The returns are: bad_luck (int): The number of days with bad luck in the year and good_luck (int): The number of days with good luck in the year.
    if user == 'spin':
        print("Spin the wheel of 'fortune'!")
        print("----------------------------------")

        n = 365
        bad_luck = 0
        good_luck = 0

        for i in range(n):
            spin = random.randint(1,2)
            if spin == 1:
                bad_luck += 1
            else:
                good_luck += 1

        return bad_luck, good_luck

user_input = input("If you want to see your lucky days for the next year type 'spin'. If you want to skip type 'pass':")
if user_input == "spin":
    bad_luck, good_luck = spin_wheel_of_fortune(user_input)
    print("Days with bad luck:", bad_luck)
    print("Days with good luck:", good_luck)

user_input = input("What's your luck today? type 'spin' or 'pass'")
if user_input == "spin":
    good_luck = spin_wheel_of_fortune(user_input)
    if good_luck == 183:
        print("Yay! Today is a lucky day")
    else:
        print("Aww not great, try again tomorrow")


print("Thanks for playing my fortune game, hope you enjoyed!!")

