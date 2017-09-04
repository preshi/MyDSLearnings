# -*- coding: utf-8 -*-

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist=radians(12)*r

# Print out dist
print(dist)

#importing a single package and aliasing
#using the inverse function 

#There are several ways to import packages and modules into 
#Python. Depending on the import call, you'll have to use different Python code.
#
#Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:
#
#my_inv([[1,2], [3,4]])
from scipy.linalg import inv as my_inv

my_inv([[1,2], [3,4]])


import numpy as np
#w*h^2 is not possible

height=[1.73,1.68,1.71,1.89,1.79]
weight=[65.4,59.2,63.6,68.4,68.7]

np_height=np.array(height)
np_weight=np.array(weight)

print(np_height)

print(np_weight)



#numpy


# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
#import numpy as np


# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))



heightnew=[74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74,
           74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 71, 75, 77, 74,
           73, 74, 78, 73, 75, 73, 75, 75, 74, 69, 71, 74, 73, 73, 76,
           74, 74, 70, 72, 77, 74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 
           77, 81, 78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 70, 
           70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 74, 78, 71, 73,
           76, 74, 74, 79, 75, 73, 76, 74, 74, 73, 72, 74, 73, 74, 72,
           73, 69, 72, 73, 75, 75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 
           75, 76, 80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 74,
           76, 76, 74, 73, 74, 70, 72, 73, 73, 73, 73, 71, 74, 74, 72,
           74, 71, 74, 73, 75, 75, 79, 73, 75, 76, 74, 76, 78, 74, 76,
           72, 74, 76, 74, 75, 78, 75, 72, 74, 72, 74, 70, 71, 70, 75,
           71, 71, 73, 72, 71, 73, 72, 75, 74, 74, 75, 73, 77, 73, 76,
           75, 74, 76, 75, 73, 71, 76, 75, 72, 71, 77, 73, 74, 71, 72,
           74, 75, 73, 72, 75, 75, 74, 72, 74, 71, 70, 74, 77, 77, 75,
           75, 78, 75, 76, 73, 75, 75, 79, 77, 76, 71, 75, 74, 69, 71, 
           76, 72, 72, 70, 72, 73, 71, 72, 71, 73, 72, 73, 74, 74, 72,
           75, 74, 74, 77, 75, 73, 72, 71, 74, 77, 75, 75, 75, 78, 78, 
           74, 76, 78, 76, 70, 72, 80, 74, 74, 71, 70, 72, 71, 74, 71, 
           72, 71, 74, 69, 76, 75, 75, 76, 73, 76, 73, 77, 73, 72, 72,
           77, 77, 71, 74, 74, 73, 78, 75, 73, 70, 74, 72, 73, 73, 75,
           75, 74, 76, 73, 74, 75, 75, 72, 73, 73, 72, 74, 78, 76, 73, 
           74, 75, 70, 75, 71, 72, 78, 75, 73, 73, 71, 75, 77, 72, 69, 
           73, 74, 72, 70, 75, 70, 72, 72, 74, 73, 74, 76, 75, 80, 72,
           75, 73, 74, 74, 73, 75, 75, 71, 73, 75, 74, 74, 72, 74, 74,
           74, 73, 76, 75, 72, 73, 73, 73, 72, 72, 72, 72, 71, 75, 75,
           74, 73, 75, 79, 74, 76, 73, 74, 74, 72, 74, 74, 75, 78, 74,
           74, 74, 77, 70, 73, 74, 73, 71, 75, 71, 72, 77, 74, 70, 77,
           73, 72, 76, 71, 76, 78, 75, 73, 78, 74, 79, 75, 76, 72, 75, 
           75, 70, 72, 70, 74, 71, 76, 73, 76, 71, 69, 72, 72, 69, 73, 
           69, 73, 74, 74, 72, 71, 72, 72, 76, 76, 76, 74, 76, 75, 71, 
           72, 71, 73, 75, 76, 75, 71, 75, 74, 72, 73, 73, 73, 73, 76, 
           72, 76, 73, 73, 73, 75, 75, 77, 73, 72, 75, 70, 74, 72, 80, 
           71, 71, 74, 74, 73, 75, 76, 73, 77, 72, 73, 77, 76, 71, 75, 
           73, 74, 77, 71, 72, 73, 69, 73, 70, 74, 76, 73, 73, 75, 73, 
           79, 74, 73, 74, 77, 75, 74, 73, 77, 73, 77, 74, 74, 73, 77, 
           74, 77, 75, 77, 75, 71, 74, 70, 79, 72, 72, 70, 74, 74, 72, 
           73, 72, 74, 74, 76, 82, 74, 74, 70, 73, 73, 74, 77, 72, 76, 
           73, 73, 72, 74, 74, 71, 72, 75, 74, 74, 77, 70, 71, 73, 76, 
           71, 75, 74, 72, 76, 79, 76, 73, 76, 78, 75, 76, 72, 72, 73, 
           73, 75, 71, 76, 70, 75, 74, 75, 73, 71, 71, 72, 73, 73, 72, 
           69, 73, 78, 71, 73, 75, 76, 70, 74, 77, 75, 79, 72, 77, 73, 
           75, 75, 75, 73, 73, 76, 77, 75, 70, 71, 71, 75, 74, 69, 70, 
           75, 72, 75, 73, 72, 72, 72, 76, 75, 74, 69, 73, 72, 72, 75, 
           77, 76, 80, 77, 76, 79, 71, 75, 73, 76, 77, 73, 76, 70, 75, 
           73, 75, 70, 69, 71, 72, 72, 73, 70, 70, 73, 76, 75, 72, 73, 
           79, 71, 72, 74, 74, 74, 72, 76, 76, 72, 72, 71, 72, 72, 70, 
           77, 74, 72, 76, 71, 76, 71, 73, 70, 73, 73, 72, 71, 71, 71, 
           72, 72, 74, 74, 74, 71, 72, 75, 72, 71, 72, 72, 72, 72, 74, 
           74, 77, 75, 73, 75, 73, 76, 72, 77, 75, 72, 71, 71, 75, 72, 
           73, 73, 71, 70, 75, 71, 76, 73, 68, 71, 72, 74, 77, 72, 76, 
           78, 81, 72, 73, 76, 72, 72, 74, 76, 73, 76, 75, 70, 71, 74, 
           72, 73, 76, 76, 73, 71, 68, 71, 71, 74, 77, 69, 72, 76, 75, 
           76, 75, 76, 72, 74, 76, 74, 72, 75, 78, 77, 70, 72, 79, 74, 
           71, 68, 77, 75, 71, 72, 70, 72, 72, 73, 72, 74, 72, 72, 75, 
           72, 73, 74, 72, 78, 75, 72, 74, 75, 75, 76, 74, 74, 73, 74, 
           71, 74, 75, 76, 74, 76, 76, 73, 75, 75, 74, 68, 72, 75, 71, 
           70, 72, 73, 72, 75, 74, 70, 76, 71, 82, 72, 73, 74, 71, 75, 
           77, 72, 74, 72, 73, 78, 77, 73, 73, 73, 73, 73, 76, 75, 70, 
           73, 72, 73, 75, 74, 73, 73, 76, 73, 75, 70, 77, 72, 77, 74, 
           75, 75, 75, 75, 72, 74, 71, 76, 71, 75, 76, 83, 75, 74, 76, 
           72, 72, 75, 75, 72, 77, 73, 72, 70, 74, 72, 74, 72, 71, 70, 
           71, 76, 74, 76, 74, 74, 74, 75, 75, 71, 71, 74, 77, 71, 74, 
           75, 77, 76, 74, 76, 72, 71, 72, 75, 73, 68, 72, 69, 73, 73, 
           75, 70, 70, 74, 75, 74, 74, 73, 74, 75, 77, 73, 74, 76, 74, 
           75, 73, 76, 78, 75, 73, 77, 74, 72, 74, 72, 71, 73, 75, 73, 
           67, 67, 76, 74, 73, 70, 75, 70, 72, 77, 79, 78, 74, 75, 75, 
           78, 76, 75, 69, 75, 72, 75, 73, 74, 75, 75, 73]


np_heightnew=np.array(heightnew)

# Print out np_height
print(np_heightnew)


# Convert np_height to m: np_height_m

np_heightnew_m=np_heightnew*0.0254
# Print np_height_m
print(np_heightnew_m)


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg=np.array(weight)*0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/(np_height_m)**2

# Print out bmi
print(bmi)


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmisubset = np_weight_kg / np_height_m ** 2

# Create the light array
light=bmisubset<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmisubset[light])

#as shown below As Filip explained before, numpy is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

#First of all, numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. This is known as type coercion.

#Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.
newhomogeneous=np.array([True, 1, 2]) + np.array([3, 4, False])
print(newhomogeneous)

print(np.array([4, 3, 0]) + np.array([0, 2, 2]))


