def fibonachi (n, list_result = None):
    if list_result is None:
        list_result = [1, 1]

    if n > len(list_result):
        list_result.append(list_result[-1] + list_result[-2])
        return fibonachi(n, list_result)
    else:
        return list_result

print(fibonachi(10))