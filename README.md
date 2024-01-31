# T9 Texting Solution 

## Overview

In our solution we implement the [Backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) to solve the problem. We ennumerate through all possible word combinations generated from the number sequence. Each number maps to 3-4 letters given by the `numbers_to_letters` dictionary. 

## Runtime complexity 

### Time Complexit 

The worst case time complexity is O(4^N) where N is the length of the sequence. The 4^N corresponds
to all possible combinations of the number sequence if we only had 7s and 9s (worst case upper bound).

## Space complexity

We would need O(4^N). Worst case we would need to store all 4^N possible combinations. 

## Run the code 

The code has been tested with Python version 3.10.4. You will also need [make](https://en.wikipedia.org/wiki/Make_(software)) installed. 

To run the solution 

```
% make 
python findWords.py
['gm', 'gmmd', 'gmme', 'gmmf', 'gmnd', 'gmne', 'gmnf', 'gmod', 'gmoe', 'gmof', 'gn', 'gnmd', 'gnme', 'gnmf', 'gnnd', 'gnne', 'gnnf', 'gnod', 'gnoe', 'gnof', 'go', 'gomd', 'gome', 'gomf', 'gond', 'gone', 'gonf', 'good', 'gooe', 'goof', 'hm', 'hmmd', 'hmme', 'hmmf', 'hmnd', 'hmne', 'hmnf', 'hmod', 'hmoe', 'hmof', 'hn', 'hnmd', 'hnme', 'hnmf', 'hnnd', 'hnne', 'hnnf', 'hnod', 'hnoe', 'hnof', 'ho', 'homd', 'home', 'homf', 'hond', 'hone', 'honf', 'hood', 'hooe', 'hoof', 'im', 'immd', 'imme', 'immf', 'imnd', 'imne', 'imnf', 'imod', 'imoe', 'imof', 'in', 'inmd', 'inme', 'inmf', 'innd', 'inne', 'innf', 'inod', 'inoe', 'inof', 'io', 'iomd', 'iome', 'iomf', 'iond', 'ione', 'ionf', 'iood', 'iooe', 'ioof']
```

To run tests 

```
% make test
python -m unittest test_findWords.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.015s

OK
```