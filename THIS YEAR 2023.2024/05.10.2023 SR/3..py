class NoArgsError(Exception):
    pass

class TooSmallResultError(Exception):
    pass
def lucky_ones(*args,criterion=10):
    try:
        result = []
        # вот тут пишем код
        # каие-то проверки аргументов
        if not args:
            raise NoArgsError
        # проверяем, что все элементы args это строка

        for i in args:
            if type(i) is not str:
                raise TypeError

        for i in args:
            if len(set(i)) <= criterion:
                result.append(i)
        result.sort(key=lambda x: len(x), reverse=True)

        if len(result) < 2:
            raise TooSmallResultError
    except NoArgsError:
        print('Empty input strings list;')
    except TypeError:
        print('Not string argument;')
    except TooSmallResultError:
        print('Too few items in result')


    return  result

data = ('children\'s writer', 'humorist', 'cartoonist', 'poet')
print(lucky_ones(*data, criterion=5))
