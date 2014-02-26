"""
Nitrogenium problem


Key observation here:

N(island) = N(local maxima above water) - N(local minima above water)
"""


def peaks_and_troughs(land, water):
    """
    Return a peaks and troughs array, where
    peaks[h] = number of peaks at height >= h
    troughs[h] = number of troughs at height >= h
    """
    n = max(max(land), max(water)) + 2

    peaks = [0] * n
    troughs = [0] * n

    rising, falling = True, False

    # first pass -- height of each peak/trough
    for x, y in enumerate(land[1:], 1):
        y0 = land[x - 1]
        if y < y0:
            if rising:
                peaks[y0] += 1
            falling, rising = True, False
        if y > y0:
            if falling:
                troughs[y0] += 1
            rising, falling = True, False

    # handle peak at last spot
    if rising and len(land) > 1 and land[-1] >= land[-2]:
        peaks[land[-1]] += 1

    if len(land) == 1:
        peaks[land[0]] += 1

    # second pass for cumulative sum
    for i in xrange(n - 2, -1, -1):
        peaks[i] += peaks[i + 1]
        troughs[i] += troughs[i + 1]

    return peaks, troughs


def solution(land, water):
    p, t = peaks_and_troughs(land, water)
    return [p[w + 1] - t[w + 1] for w in water]
