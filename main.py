import random
#beginning of the loop
play_again = True
while play_again:
# My words as shown in the word bank
  WORD = ('drake', 'madonna', 'rihanna', 'beyonce', 'cameron', 'eminem', 'ludacris', 'mario', 'prince', 'usher' ,'cher', 'sade', 'halsey', 'future', 'aaliyah', 'queen', 'nirvana', 'paramore', 'weezer', 'tupac')
  word = random.choice(WORD)
  correct = word
  clue = word[0] + word[(len(word)-1):(len(word))]
  letter_guess = ''
  word_guess = ''
  store_letter = ''
  count = 0
  limit = 7
  name = input("\nWelcome! What is your name?\n")
  print('Welcome' , name , 'to the Game!')
  print('You have 7 attempts at guessing letters in a word!')
  print('After the 7 tries, you have to guess the artist. Good luck' , name + '!')
  print('Here is your artist word bank: drake, madonna, rihanna, beyonce, cameron, eminem, ludacris, mario, prince, usher ,cher, sade, halsey, future, aaliyah, queen, nirvana, paramore, weezer, tupac')
  print('\n')
  while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

    if count == 3:
        print('\n')
        clue_request = input('Would you like a clue?')
        if clue_request == 'yes':
            print('\n')
            print('CLUE: The first and last letter of the name is: ', clue)
        if clue_request == 'no':
            print('You\'re very brave!')

  print('\n')
  print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
  print('These letters are: ', store_letter)

  word_guess = input('Guess the whole name: ')
  while word_guess:
    if word_guess.lower() == correct:
        print('You got it! Your prize....Nothing')
        break

    elif word_guess.lower() != correct:
        print('Almost had it! The answer was,', word)
        break 
  print("\nWould you like to play again? Type y or yes to play again.")
  response = input("> ").lower()
  if response not in ("yes", "y"):
      play_again = False
#loop end
if __name__ == "__main__":
  main()