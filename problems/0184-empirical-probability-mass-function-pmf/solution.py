def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    values = {}
    keys = []
    value = []
    result = []
    
    if samples == []:
        return []

    for i in range(len(samples)):
        if str(samples[i]) not in keys:
            keys.append(str(samples[i]))

    for key in keys:
        count = samples.count(int(key))
        value.append(count)

    values = dict(zip(keys, value))

    for i in range(len(value)):
        denominator = len(samples)
        pmf = value[i] / denominator
        result.append((int(keys[i]), pmf))

    return result
