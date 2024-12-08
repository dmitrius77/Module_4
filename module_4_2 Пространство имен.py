def test_function():                                         # Создайте новую функцию test_function
    def inner_function():                                    # Создайте внутри test_function другую функцию - inner_function
#        if inner_funktion in test_funktion():
        print('Я в области видимости функции test_function') # Эта функция должна печатать значение "Я в области видимости функции test_function"

    inner_function()                                         #Вызовите функцию inner_function внутри функции test_function


test_function()    # Вызов функции test_function
#inner_function()  # Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат. получим ошибку, т.к. находимся вне видимости
