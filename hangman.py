import requests

def get_guess():
  dashes = "-" * len(secret_word)
  guesses_left = 10

  while guesses_left > 0 and not dashes == secret_word:
    print(dashes)
    print (str(guesses_left))

    guess = input("Guess:")

    if guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1

  if guesses_left == 0:
    print ("You lose. The word was: " + str(secret_word))
  else:
    print ("Congrats! You win. The word was: " + str(secret_word))

def update_dashes(secret, cur_dash, rec_guess):
  result = ""

  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess
    else:
      result = result + cur_dash[i]

  return result

word_site = "http://api.wordnik.com:80/v4/words.json/randomWord?hasDictionaryDef=false&minCorpusCount=0&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
response = requests.get(word_site)
secret_word = response.json()["word"]
get_guess()
