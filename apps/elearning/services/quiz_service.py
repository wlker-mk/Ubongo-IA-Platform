class QuizService:
    def grade(self, answers):
        # TODO: implémenter correction quiz
        return {"score": len(answers), "passed": True}
