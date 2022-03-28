class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_q = Question("What is gold color? ", "yellow")
print(new_q.text)