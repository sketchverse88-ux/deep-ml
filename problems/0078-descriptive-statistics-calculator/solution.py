import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    #Mean (Average)
    mean = 0 
    for i in range(len(data)):
        mean += data[i]
    mean = mean / len(data)

    #Median (Middle Value)
    median = np.median(data)

    #Mode
    vals, counts = np.unique(data, return_counts=True)
    mode = vals[np.argmax(counts)]

    #Variance
    variance = np.nanvar(data)

    #Starndard deviation
    S_deviation =np.nanstd(data)

    #Percentiles
    frst_qrtl = np.percentile(data, 25)
    scnd_qrtl = median
    rd_qrtl = np.percentile(data, 75)

    #IQR
    IQR = rd_qrtl - frst_qrtl

    key = ["mean", "median", "mode", "variance", "standard_deviation", "25th_percentile", "50th_percentile", "75th_percentile", "interquartile_range"]
    value = [mean, median, mode, variance, S_deviation, frst_qrtl, scnd_qrtl, rd_qrtl, IQR]

    statistics = dict(zip(key, value))
    return statistics
     