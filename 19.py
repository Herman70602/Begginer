
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_gueses = False
while guess != secret_word and not (out_of_gueses):
    if guess_count < guess_limit:
         guess = input("enter guess: ")
         guess_count += 1
    else:
        out_of_gueses = True
if out_of_gueses:
    print("Out of guesses, you lose")
else:
    print("You win")
