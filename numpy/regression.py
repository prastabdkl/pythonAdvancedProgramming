import numpy as np
import matplotlib.pyplot as plot

x = np.array(range(1, 19))
y = np.array([147026,144272,140020,143801,146233,144539,141273,135389,142500,139452,139722,135300,137289,136511,132884,125683,127255,124275])

#Use np.polyfit to determine the coefficients of the regression line.
[a, b] = np.polyfit(x, y, 1)
print('[a b]',a,b)

plot.scatter( x, y )
plot.plot( [0, 30], [b, 30*a+b] )
plot.show()