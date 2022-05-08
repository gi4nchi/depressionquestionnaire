class Health:
    def __init__(self, questions):
        self.score = 0
        self.results = {}
        self.data = questions

    def generate_question(self):
        """
        questions = {}
        for k, v in self.data.items():
            questions[v['question']] = []
            for o, r in v['options'].items():
                questions[v['question']].append(o)
        """
        return self.data

    def save_answer(self, question, answer):
        self.data[question]['answer'] = answer

    def evaluate(self):
        for k, v in self.data.items():
            if 'answer' in v:
                temp_score = v['options'][v['answer']]
                self.score +=  temp_score
                if temp_score >= v['min_requirement_to_include']:
                    if v['type'] in self.results:
                        self.results[v['type']] += 1
                    else:
                        self.results[v['type']] = 1
        self.results['score'] = self.score

    def reset(self):
        for k, v in self.data.items():
            if 'answer' in v:
                self.data.pop('answer', None)
        self.results = {}
        self.score = 0

