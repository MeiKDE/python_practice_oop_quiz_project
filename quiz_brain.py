class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_input = ""
        self.current_question = ""
        self.score = 0
    
    def still_has_questions(self):
        """if self.question_number < len(self.question_list):
                return True
        else:
            return False 
        """
        # or simplify above code to below statement
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_input = input(f"Q.{self.question_number}: {self.current_question.question} (True/False)?: ")

    
    def check_answer(self):
        if self.user_input.lower() == self.current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            
        print(f"The correct answer was: {self.current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    def final_score(self):
        print(f"You've completed the quiz!")
        print(f"Your final score is: {self.score}/{self.question_number}.")
        
        
        
        
    
        
        
        
        