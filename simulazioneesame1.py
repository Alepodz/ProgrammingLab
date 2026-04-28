
class ExamException(Exception):
    pass


class MovingAverage():

    def __init__(self, window_length):
        # controllo sul parametro
        if not isinstance(window_length, int) or window_length <= 0:
            raise ExamException("window_length deve essere un intero positivo")
        
        self.window_length = window_length


    def compute(self, data):

        # controllo che data sia una lista
        if not isinstance(data, list):
            raise ExamException("data deve essere una lista")

        # controllo che tutti gli elementi siano numeri
        for element in data:
            if not isinstance(element, (int, float)):
                raise ExamException("gli elementi della lista devono essere numeri")

        # controllo caso limite
        if len(data) < self.window_length:
            raise ExamException("lista troppo corta")

        result = []

        # ciclo per calcolare la media mobile
        for i in range(len(data) - self.window_length + 1):

            window = data[i : i + self.window_length]
            average = sum(window) / self.window_length
            result.append(float(average))

        return result


 

    