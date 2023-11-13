class NoArgumentsError(Exception):
    pass


class EmptyResultError(Exception):
    pass


def fate_oil(*args, comparison=0):
    try:
        result = []
        data = list(map(list, args))
        if not data:
            raise NoArgumentsError

        for i in range(len(data)):
            for k in range(2):
                if data[i][k] == '':
                    raise ValueError

        for i in range(len(data)):
            tmp1 = data[i][0]
            tmp2 = data[i][1]
            num = 0
            letters1 = []
            for k in range(len(tmp1)):
                if tmp1[k] != ' ':
                    letters1.append(tmp1[k])
            for k in range(len(tmp2)):
                if tmp2[k] in letters1:
                    num += 1
            if num >= comparison:
                result.append(data[i][1])
            result.sort()
            result.sort(key=lambda x: len(x), reverse=True)
        if len(result) == 0:
            raise EmptyResultError
        else:
            return result

    except ValueError:
        return 'ValueError: Empty string'

    except EmptyResultError:
        return 'EmptyResultError: No result'

    except NoArgumentsError:
        return 'NoArgumentsError: Too few arguments'
