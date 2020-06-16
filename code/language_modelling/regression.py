def regress(xVals, yVals):
    """
    Simple linear regression: find the straight line that minimises the
    sum of the distance squared to each sample point. Then use the line to
    smooth y
    """
    assert len(xVals) == len(yVals)
    xMean = mean(xVals)
    yMean = mean(yVals)
    ss_xy = 0.0
    ss_xx = 0.0
    coords = zip(xVals, yVals)
    for x, y in coords:
        xDist = x - xMean
        yDist = y - yMean
        # SS_xy = sum the product of the distances from the mean
        ss_xy += xDist*yDist
        # SS_xx = sum the squares of the x distance
        ss_xx  += xDist*xDist
    # Gradient
    m  = ss_xy/ss_xx
    # Intercept
    b = yMean - m*xMean
    regressed = []
    for x, y in coords:
        # y=mx+b...
        regressed.append(m*x+b)
    return m, b
        
    
def mean(nums):
    """
    The mean. Self explanatory innit?
    """
    return float(sum(nums))/float(len(nums))
    
if __name__ == '__main__':    
    # Answers should be m=4.56; b=4242
    xVals = [160, 175, 192, 195, 238, 240, 252, 282]
    yVals = [4862, 5244, 5128, 5052, 5298, 5410, 5234, 5608]
    gradient, intercept = regress(xVals, yVals)
    print "Gradient: %s" % gradient
    print "Intercept: %s" % intercept
