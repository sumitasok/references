# https://stackoverflow.com/questions/2462725/cv-saveimage-in-opencv

import cv2
filename = 'pic.jpeg'
cam = cv2.VideoCapture(filename)
s, img = cam.read()
picName = 'pic.png'
cv2.imwrite(picName, img)`

# https://stackoverflow.com/questions/684171/how-to-re-import-an-updated-package-while-in-python-interpreter
# All the answers above about reload() or imp.reload() are deprecated.

# reload() is no longer a builtin function in python 3 and imp.reload() is marked deprecated (see help(imp)).

# It's better to use importlib.reload() instead.

# https://stackoverflow.com/questions/31751464/how-do-i-close-an-image-opened-in-pillow
with Image.open('test.png') as test_image:
    do_things(test_image)
# An example of using Image.close():

test = Image.open('test.png')
test.close()

# https://stackoverflow.com/questions/15746675/how-to-write-a-python-module
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py

# create hello.py then write the following function as its content:

def helloworld():
   print "hello"
# Then you can import hello:

>>> import hello
>>> hello.helloworld()
'hello'
>>>
# To group many .py files put them in a folder. Any folder with an __init__.py is considered a module by python and you can call them a package

# |-HelloModule
#   |_ __init__.py
#   |_ hellomodule.py
# You can go about with the import statement on your module the usual way.

# For more information, see 6.4. Packages.

# https://stackoverflow.com/questions/19839488/upgrade-to-numpy-1-8-0-on-ubuntu-12-04
sudo pip install numpy --upgrade


# https://stackoverflow.com/questions/18265935/python-create-list-with-numbers-between-2-values
>>> numpy.arange(11, 17, 0.5)
array([ 11. ,  11.5,  12. ,  12.5,  13. ,  13.5,  14. ,  14.5,  15. ,
        15.5,  16. ,  16.5])
>>> list(range(11, 17))
[11, 12, 13, 14, 15, 16]

# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object

>>> type([]) is list
True
>>> type({}) is dict
True
>>> type('') is str
True
>>> type(0) is int
True
>>> type({})
<type 'dict'>
>>> type([])
<type 'list'>

>>> class Test1 (object):
        pass
>>> class Test2 (Test1):
        pass
>>> a = Test1()
>>> b = Test2()
>>> type(a) is Test1
True
>>> type(b) is Test2
True

>>> type(b) is Test1
False

>>> isinstance(b, Test1)
True
>>> isinstance(b, Test2)
True
>>> isinstance(a, Test1)
True
>>> isinstance(a, Test2)
False
>>> isinstance([], list)
True
>>> isinstance({}, dict)
True

# isinstance() is usually the preferred way to ensure the type of an object because it will also accept derived types. So unless you actually need the type object (for whatever reason), using isinstance() is preferred over type().

# The second parameter of isinstance() also accepts a tuple of types, so it’s possible to check for multiple types at once. isinstance will then return true, if the object is of any of those types: