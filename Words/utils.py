from random import choice, shuffle


menu = ({"name": "Домашняя страница", "url": "home", "select": 1},
        {"name": "Добавить слова", "url": "add_words", "select": 2},
        {"name": "Учеба", "url": "study", "select": 3},
        )


class DataMixin:
    """Класс для устранения дублирования кода,
    Тут содержится общая информация"""
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class QuestionMaker:
    """Класс для генерации вопросов"""
    def __init__(self, english_in_question: bool, words: list):
        if english_in_question:
            self.__language_question = "name_eng"
            self.__language_answer = "name_rus"
        else:
            self.__language_question = "name_rus"
            self.__language_answer = "name_eng"
        self.__words = words

    def get_questions(self):
        """ возвращает list словарей типа {'pk':1, 'question': 'кот',
        'answers': ('dog', 'cat', 'red', 'black'), correct: 1} """
        quiz = []
        if len(self.__words) < 5:
            return quiz

        for word in self.__words:
            dict_element = {}
            dict_element["pk"] = word.pk
            dict_element["question"] = getattr(word, self.__language_question)
            answers, correct_index = self.__get_objects_for_answer(word)
            dict_element["answers"] = answers
            dict_element["correct"] = correct_index
            quiz.append(dict_element)

        return quiz

    def __get_objects_for_answer(self, question_word):
        answers = []
        answers.append(getattr(question_word, self.__language_answer)) # добавляем правильный вариант ответа

        while len(answers) < 4:
            """добавляем 3 ложных варианта ответа"""
            word = choice(self.__words)
            if getattr(word, self.__language_answer) not in answers:
                answers.append(getattr(word, self.__language_answer))

        shuffle(answers)
        correct = getattr(question_word, self.__language_answer)
        return answers, correct











