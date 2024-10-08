from random import choice
import nltk
from nltk.corpus import words 
from PIL import Image, ImageDraw

class Hangman: 
    
    #define variables
    random_word = None
    game_on = True
    guess_count = 0 
    incorrect_guesses = 0
    display_word = []
    
    ##keep track of guessed letters
    guessed_letters = set()
    
    ##generate a random word to try to match to 
    @classmethod
    def word_generator(cls):
        nltk.download("words")
        word_list = words.words()
        
        difficulty_choice = input("Do you want to do Hard, Medium or Easy? Type out which mode: ").lower()
        
        if difficulty_choice == "hard": 
            print("Hard difficulty selected")
            cls.random_word = choice([word for word in word_list if 9 > len(word) > 5]).lower()
        elif difficulty_choice == "medium": 
            print("Medium difficulty selected")
            cls.random_word = choice([word for word in word_list if 7 > len(word) > 3]).lower()
        elif difficulty_choice == "easy": 
            print("Easy difficulty selected")
            cls.random_word = choice([word for word in word_list if 5 > len(word) > 2]).lower()
        else:
            print("Input not recognized, defaulting to Medium difficulty")
            cls.random_word = choice([word for word in word_list if 7 > len(word) > 3]).lower()
        
        
        cls.display_word = ["_"] * len(cls.random_word)
        return cls.random_word
    
    
    ##get player input
    ##match player input to word, record right or wrong
    @classmethod
    def player_input(cls):
        
        while True:
            player_guess = input("type in a letter: ").lower()
            if player_guess in cls.guessed_letters:
                print(f'You have already guessed {player_guess}, try again!')
            elif len(player_guess) != 1 or not player_guess.isalpha():
                print("Please enter a single letter.")
            else: 
                print(f'Here is your guess {player_guess}')
                cls.guessed_letters.add(player_guess)
                break
            
            
        if player_guess in cls.random_word:
            for i, char in enumerate(cls.random_word):
                if player_guess == char:
                        cls.display_word[i] = player_guess
        else:
                cls.incorrect_guesses += 1
            
        print(f'Current word: {" ".join(cls.display_word)}')
        print(f'Incorrect guesses: {cls.incorrect_guesses}')



    ##function to display word and guess results 
    @classmethod
    def display(cls):
        print("Current word: "+" ".join(cls.display_word))
    
    ##create actual hangman to replicate game
    @classmethod
    def display_2(cls):
        # Create a new image with a white background
        width, height = 200, 200
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)

        # Draw the base structure (gallows)
        draw.line((50, 150, 150, 150), fill='black', width=3)  # Base
        draw.line((100, 150, 100, 50), fill='black', width=3)  # Vertical pole
        draw.line((100, 50, 150, 50), fill='black', width=3)   # Horizontal pole
        draw.line((150, 50, 150, 70), fill='black', width=3)   # Rope

        # Draw hangman parts based on incorrect guesses
        if cls.incorrect_guesses >= 1:
            ##draw.line(xy, fill=None, width=0, joint=None)
            draw.ellipse((140, 70, 160, 90), outline='black', width=3)  # Head
        if cls.incorrect_guesses >= 2:
            draw.line((150, 90, 150, 120), fill='black', width=3)       # Body
        if cls.incorrect_guesses >= 3:
            draw.line((150, 100, 130, 110), fill='black', width=3)      # Left arm
        if cls.incorrect_guesses >= 4:
            draw.line((150, 100, 170, 110), fill='black', width=3)      # Right arm
        if cls.incorrect_guesses >= 5:
            draw.line((150, 120, 140, 140), fill='black', width=3)      # Left leg
        if cls.incorrect_guesses >= 6:
            draw.line((150, 120, 160, 140), fill='black', width=3)      # Right leg

        # Save the image
        image_filename = f'hangman_{cls.incorrect_guesses}.png'
        image.save(image_filename)
        print(f"Saved {image_filename}")
        
        # Display the image (optional)
        input_choice = input("Do you want to see your hanged man? Y/N?")
        
        if input_choice == 'y' or "Y":
            image.show()
        else:
            print("Image not printed")
        
    
    
    ## main function
    @classmethod
    def main(cls):
        
        
        
        print("Howdy, welcome to Hangman!")
        print("================================")
        print("Guess the word, one letter at a time.")
        print("You have 6 attempts to save the hangman!")
        print("Good luck and have fun!")
        print("================================\n")
        
        cls.word_generator()
        
        ##check
        ##print(cls.random_word)
        
        while cls.game_on == True:
            cls.display()
            cls.player_input()
            cls.display_2()
            
            if cls.incorrect_guesses >=6:
                print("Game over, you have hanged a man :(")
                print(cls.random_word)
                cls.game_on = False
            elif "_" not in cls.display_word:
                print("Congratulations! You've guessed the word correctly!")
                cls.game_on = False
            else:
                pass
            
# Run the game
Hangman.main()
            
            
            