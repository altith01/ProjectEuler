# Marsh Crossing
#  Make use of Snell's Law

from math import asin, pi, sqrt, cos, sin, tan

V1 = 10
D = 25*sqrt(2)-25
V2 = 9
V3 = 8
V4 = 7
V5 = 6
V6 = 5
V7 = 10

GOAL_COORD = 50*sqrt(2)
bestTime = 20

# Ran with less precision (0 -> 4999 scaled down by 10000) then increased
for n in range(3100000, 3199999):
    T1 = n*pi/10000000
    T2 = asin((V2*sin(T1))/V1)
    T3 = asin((V3*sin(T2))/V2)
    T4 = asin((V4*sin(T3))/V3)
    T5 = asin((V5*sin(T4))/V4)
    T6 = asin((V6*sin(T5))/V5)

    h1 = D / cos(T1)
    h2 = 10 / cos(T2)
    h3 = 10 / cos(T3)
    h4 = 10 / cos(T4)
    h5 = 10 / cos(T5)
    h6 = 10 / cos(T6)

    y1 = D * tan(T1)
    y2 = 10 * tan(T2)
    y3 = 10 * tan(T3)
    y4 = 10 * tan(T4)
    y5 = 10 * tan(T5)
    y6 = 10 * tan(T6)
    y7 = GOAL_COORD - (y1+y2+y3+y4+y5+y6)

    h7 = sqrt(D**2 + y7**2)

    thisTime = h1/V1 + h2/V2 + h3/V3 + h4/V4 + h5/V5 + h6/V6 + h7/V7
    bestTime = min(thisTime, bestTime)
    if thisTime == bestTime:
        bestN = n

print(bestN, bestTime)