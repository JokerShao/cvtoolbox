# cvtoolbox

Some utilities code for image preprocessing and 3D rotation.

## Useful Library

### [numpy-quaternion][1]

This package creates a quaternion type in python, and further enables numpy to create and manipulate arrays of quaternions. The usual algebraic operations (addition and multiplication) are available, along with numerous properties like norm and various types of distance measures between two quaternions. There are also additional functions like “squad” and “slerp” interpolation, and conversions to and from axis-angle, matrix, and Euler-angle representations of rotations. The core of the code is written in C for speed.

[1]:https://pypi.org/project/numpy-quaternion/