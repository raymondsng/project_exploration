class Question:

    def __init__(self, text, answer, justification):
        self.text = text
        self.answer = answer
        self.justification = justification

    def check(self, answer):
        return self.answer == answer

    def display_text(self):
        return self.text

    def display_justification(self):
        return print(f"Justification: {self.justification}")