
"""a) retornar somente os valores que pertencem as duas listas"""
def merge_both(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1

"""b) retornar somente os valores que pertencem a lista 1 e nao pertence a lista 2"""
def merge_only_first(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1

"""c) retornar somente os valores que pertencem a lista 2 e nao pertence a lista 1"""
def merge_only_second(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(ys[yi])
            yi += 1
        else:
            xi += 1

"""d) retornar somente os valores que pertencem ou a lista 1 ou a lista 2"""
def merge_or(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

"""e) bagdiff"""
def bagdiff(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1


result1 = merge_both([5,7,11,12,13], [7,8,11,14])
result2 = merge_only_first([5,7,11,12,13], [7,8,11,14])
result3 = merge_only_second([5,7,11,12,13], [7,8,11,14])
result4 = merge_or([5,7,11,12,13], [7,8,11,14])
result5 = bagdiff([5,7,11,11,12,13], [7,8,11,14])
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
