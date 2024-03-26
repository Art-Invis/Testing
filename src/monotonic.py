def is_monotonic(array):
    if len(array) <= 1:
        return True
    
    increase, decrease = True, True

    for i in range(len(array) - 1):
        if not (array[i] >= array[i + 1]):
            decrease = False
        elif not (array[i] <= array[i + 1]):
            increase = False

    return increase or decrease
