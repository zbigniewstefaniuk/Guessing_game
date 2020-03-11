import sys
from time import sleep
import random


class GuessingEngine:

    def __init__(self):
        self.choices = {
            "1": self.animal_game,
            "2": self.capital_game,
            "3": self.leave
        }
        self.run()

    def display_menu(self):
        print("""
    GAME MENU
1: Guessing Animal game
2: Scoreboard
3: Exit
                """)

    def run(self):
        flag_menu = True
        while flag_menu:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
                flag_menu = False
            else:
                print("You have to select either 1, 2 or 3")
                print(f'{choice} Please try again')

    def animal_game(self):
        animals = {
            'Lion': 'He\'s King of the JUNGLE!',
            'Monkey': 'Eats bananas and dances for you',
            'Giraffe': 'Has a hella long neck',
            'Elephant': 'Big grey boy in africa and making: Toooth!',
            'Tiger': 'That\'s how MJ called Peter Parker ',
            'Rabbit': 'In 8 mile, Eminem was called white...',
            'Owl': 'Hooo, hoo!(also got big eyes O.O)',
            'Horse': 'Universal symbol of freedom without restraint',
            'Fish': 'Swimming in the ocean...',
            'Worm': 'Bear Grylls often ate it!',
            'Wolf': 'Howling at the midnight to the moon! Auu',
            'Snake': 'Ssssss...',
            'Bear': 'Big Brown and fluffy living in the forest',
            'Fox': 'Has a big fluffy red tail',
            'Shark': 'Surfers are often bitten by...',
            'Zebra': 'Black and white, living on savvanah',
            'Dog': 'He\'s the best friend of human',
            'Cat': 'Meow :3',
            'Alligator': 'Mostly large, predatory, semiaquatic reptiles',
            'Camel': 'You travel on him at sahara',
            'Bat': 'He\'s using echolocation to travel',
            'Chicken': 'Part of "KFC"',
            'Bird': 'Flying animal',
            'Cow': 'Giving milk and making: "Moooo"',
            'Duck': 'Duffy, Donald...',
            'Donkey': 'Shrek friend',
            'Goat': 'He\'s only animal, that have square eyes',
            'Mouse': 'Disney iconic character Mickey!',
            'Ocelot': 'Small kind of leopard with cents, and it\'s beautiful',
            'Parrot': 'Always repeating words after you...',
            'Pig': 'They eating just everything!',
            'Spider': 'Living in the web'
        }
        print("Let's Play small game!\n ")
        sleep(1)
        print("In this game you need to guess an animal!\n")
        sleep(1)
        # print('These are the possible animals: ')
        # for animal, quote in animals.items(): # first wersion contains 4 animals so it was easier to show
        #     print(animal)

        random_animal = random.choice(list(animals.keys()))

        flag = True
        counter_tries = 1
        fail = 0
        while flag:
            guess = ''
            while not guess:
                guess = input('\nGuess which animial I\'m thinking of: \n')
                if not guess:
                    print('Type something...')
            guess = guess.title()
            if guess == random_animal:
                print(f'Great! {random_animal} is the right answer!\n'
                      f'You guess it after {counter_tries} tries.')
                flag = False
                sleep(2)
                self.run()
            elif fail >= 2:
                print(f'Nope, here is small tip: \n'
                      f'{animals.get(random_animal)}')
            else:
                print(f'Nope\n')
            fail += 1
            counter_tries += 1

    def capital_game(self):
        """
        Scoreboard
        """
        print('there will be scoreboard! shhh')
        sleep(2)
        self.run()

    def leave(self):
        print("Thank you, bye.")
        sys.exit(0)


if __name__ == '__main__':
    game = GuessingEngine()
