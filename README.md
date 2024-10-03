# Quiz Game

This is a simple terminal-based quiz game implemented in Python. It takes a set of questions and their answers, asks the user for input, and then checks whether the user's answer is correct. The game continues until all questions have been answered, and a final score is displayed at the end.

## Features

- **Question Bank**: The game loads a series of questions and answers from the `question_data` list.
- **Interactive Gameplay**: The user is prompted to answer questions one by one.
- **Answer Checking**: After each question, the user’s answer is checked, and feedback is given.
- **Final Score**: Once all the questions are answered, the user’s final score is displayed.

## How it Works

1. **Load Questions**: The program reads questions and their correct answers from a `question_data` list and creates a `Question` object for each one.
2. **Ask Questions**: The `QuizBrain` class handles asking questions to the user and checking their answers.
3. **Track Progress**: The game keeps track of how many questions the user has answered correctly.
4. **Display Final Score**: After the quiz is complete, the final score is displayed.

## Code Overview

The main script does the following:

1. Loops through the `question_data` list and creates `Question` objects for each question-answer pair.
2. Stores these `Question` objects in a `question_bank` list.
3. Initializes the `QuizBrain` object with the list of `Question` objects.
4. The game loop keeps asking questions until there are no more questions left.
5. After the game finishes, it prints the user’s final score.

### Code Example

Here’s an outline of how the code works:

```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank with Question objects
question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text=text, answer_text=answer)
    question_bank.append(new_question)

# Initialize QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Main quiz loop
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()

# Display the final score
quiz.final_score()
