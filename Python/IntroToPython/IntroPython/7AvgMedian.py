# -*- coding: utf-8 -*-

#You now know how to use numpy functions to get a better feeling for your data. It basically comes down to importing numpy and then calling several simple functions on the numpy arrays:
#
#import numpy as np
#x = [1, 4, 8, 10, 12]
#np.mean(x)
#np.median(x)
#The baseball data is available as a 2D numpy array with 3 columns 
#(height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. 
#After restructuring the data, however, you notice that some height values are abnormally high.
# Follow the instructions and discover which summary statistic is best suited if you're dealing with
# so-called outliers.

#Create numpy array np_height that is equal to first column of np_baseball.
#Print out the mean of np_height.
#Print out the median of np_height.

# np_baseball is available


#np_baseball
#
#[[  7.40000000e+04   1.80000000e+02   2.29900000e+01]
# [  7.40000000e+01   2.15000000e+02   3.46900000e+01]
# [  7.20000000e+01   2.10000000e+02   3.07800000e+01]
# ..., 
# [  7.50000000e+01   2.05000000e+02   2.51900000e+01]
# [  7.50000000e+01   1.90000000e+02   3.10100000e+01]
# [  7.30000000e+01   1.95000000e+02   2.79200000e+01]]
# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height=np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))