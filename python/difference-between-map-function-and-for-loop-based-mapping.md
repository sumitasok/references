### Difference between map and for loop based mapping

```
outputs = [[1,2,3,4,'No'], [1,2,3,4,'Yes']]
```

Consider the above data,

If we want to collect the ‘No’ s alone. Without having an array size 2. We need to use

```
output[4] for output in outputs if output[4] == ‘No'
```

this will return,

```
['No']
```

If we do

```
def x(c):
    if c[4] == 'No':
        return c[4]

list(map(x, outputs))

```

It will return,

```
['No', None]
```

On top of this data we will have to run

```
results = ['No', None]
[x for x in results if results is not None]
```

or

```
from operator import is_not
from functools import partial

filter(partial(is_not, None), results)
```