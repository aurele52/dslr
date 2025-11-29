import math


def au_sort(a):
    b = []
    for i in a:
        if not math.isnan(i):
            b.append(i)
    l = au_count(b)
    i, j = 0, 1
    while i < l:
        while j < l:
            if b[i] < b[j]:
                b[i], b[j] = b[j], b[i]
            j += 1
        i += 1
        j = 0
    return b


def au_50(a):
    b = au_sort(a)
    co = au_count(b)
    return b[(co + 1) // 2]


def au_75(a):
    b = au_sort(a)
    co = au_count(b)
    return b[(3 * co + 1) // 4]


def au_25(a):
    b = au_sort(a)
    co = au_count(b)
    return b[(co + 3) // 4]


def au_mean(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += i
    return ret / len(a)


def au_sum(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += i
    return ret


def au_max(a):
    ret = -100000000
    for i in a:
        if not math.isnan(i):
            if i > ret:
                ret = i
    return ret


def au_min(a):
    ret = 100000000
    for i in a:
        if not math.isnan(i):
            if i < ret:
                ret = i
    return ret


def au_count(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += 1
    return ret


def au_std(a):
    N = au_count(a)
    mean = au_mean(a)
    d2 = 0
    for i in a:
        if not math.isnan(i):
            d2 = abs(i - mean)**2
    return (d2 / (N)) ** 0.5
