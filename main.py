# TODO: Ask the questions
# TODO: Check the answers
# TODO: Check if at end of game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# look through the question_data and create a list of Question objects
question_bank = []
for q in question_data:
    question = q["question"]  # access the question
    correct_answer = q["correct_answer"]  # access the answer of the question
    # print(f"Question: {question}, Answer: {answer}") #print the question and answer
    # parse data and initialize a new Question object
    new_question = Question(question_text=question, answer_text=correct_answer)
    # now add the new Question object to the question_bank list
    question_bank.append(new_question)

# Test
# print(question_bank[0].question) #print the first question in the question_bank list
# print(question_bank[0].answer) #print the answer of the first question in the question_bank list

# Bring up the question_bank list and ask the user to answer the questions one by one.

quiz = QuizBrain(question_bank)
quiz.next_question()  # print the first question in the question_bank list
# User type answer
quiz.check_answer()

while quiz.still_has_questions():
    # Keep asking questions
    quiz.next_question()  # print the next question in the question_bank list
    quiz.check_answer()

quiz.final_score()
