class QuizBrain:

  def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_li = q_list

  def next_question(self):
    current_question = self.question_li[self.question_number]
    self.question_number += 1
    user_answer = input(f"Otázka č. {self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)

  def has_question(self):
    if self.question_number < len(self.question_li):
      return True
    else:
      return False
    
  def check_answer(self, us_answer, correct_answer):
    if us_answer.lower() == correct_answer.lower():
      print("Uhádli jste!")
      self.score += 1
      print(f"Vaše skóre je: {self.score} / {self.question_number}")
    else:
      print("Špatná odpověď")
      print(f"Vaše skóre je: {self.score} / {self.question_number}")
    print(f"Správná odpověď {correct_answer}.")