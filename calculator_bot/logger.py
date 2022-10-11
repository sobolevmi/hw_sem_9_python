from datetime import datetime

def log_time():
    """Функция по записи в журнал логов времени выполнения операции"""
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        file.write("Время выполнения новой математической операции: " + str(operation_time) + "\n" + "\n")

def log_message(message):
    """Функция по записи в журнал логов сообщения о типе ошибки: WARNING (предупреждение) и CRITICAL (критическая ошибка)"""
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        if message == "start":
            file.write("START: пользователем начата работа с ботом\n" + str(operation_time) + "\n" + "\n")
        if message == "critical":
            file.write("CRITICAL: дальнейшая математическая операция невозможна\n" + str(operation_time) + "\n" + "\n")