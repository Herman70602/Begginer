from Question import Question

question_prompts = [
    "What color are orange?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Green\n\n",
    "What color is Pineapple?\n(a) Yellow\n(b) Blue\n(c) Magenta\n(d) Orange\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" = str(score) + "/" + str(len(questions)) + "correct")