def quickSelect(seq, k):
    # this part is the same as quick sort
    len_seq = len(seq)
    if len_seq < 2: return seq

    ipivot = len_seq // 2
    pivot = seq[ipivot]

    smallerList = [x for i,x in enumerate(seq) if x <= pivot and  i != ipivot]
    largerList = [x for i,x in enumerate(seq) if x > pivot and  i != ipivot]

    # here starts the different part
    m = len(smallerList)
    if k == m:
        return pivot
    elif k < m:
        return quickSelect(smallerList, k)
    else:
        return quickSelect(largerList, k-m)




if __name__ == '__main__':
    # Checking the Answer
    seq = [10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200]

    # we want the middle element
    k = len(seq) // 2

    # Note that this only work for odd arrays, since median in
    # even arrays is the mean of the two middle elements
    print(quickSelect(seq, k))
    import numpy
    print numpy.median(seq)