Biostat 823
<br />
Name: Jiajie Shen
<br />
HW 1
<br />
`blog information`: This blog is the property of Jiajie Shen and the blog contains the homework solution and explanation for the class of Biostatistics 823 of Fall 2021.

<br />

# Question 1 (Euler problem 9)


### Question: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
<br />
<br />

Solution code:
```
def special(s):

"""
The first for loop sets the shortest side's range
"""
    for a in range(1,s):
        for b in range(a+1, s-a):
        """
        The second for loop sets the second longest side's range
        """
            c = s - a - b;
            if a**2 + b**2 == c**2:
                return a*b*c
            
special(1000)

```
<br />

### Explanation for my solution: 
firstly, I created a function named `speical` and we have a random variable `s` in the parenthesis mark. We need to use two for loop to find the special value for each side of this triangle, and all sides should satisfy the conditions we have set. 

The first for loop is looking for the shortest side `a` which ranges from 1 to s, and the second for loop is looking for the second longest side `b` which ranges from a+1 to s-a, and the first for loop contains the second for loop because side a and side b are in the same triangle. 

It is obvious that `c = s - a - b ` and we set the Pythagorean theorem function. After finding the side `a`, `b`, `c` we finally let the function return the product of abc.

<br />

# Question 2 (Euler problem 16)

### Question: What is the sum of the digits of the number 2^1000?

<br />
<br />
solution code:

```
import math


def digit(num):

    total = 0
    while num >= 1:
    """
    Go through a while loop to in order to get every digit for the random variable num
    """

        mid = num % 10
        
        """
        get each digit from num as remainders.
        """
    
        total = total + mid
        num = num//10
    return total
    
digit(2**1000)

```

### Explanation for my solution: 
firstly, I created a function named `digit` and we have a random variable `num` in the parenthesis mark. I set the variable `total` eqaul to 0 to accumulate the sum of all the digits. If the input value `num` is greater or equal to 1 then it will keep the while loop running.

Inside of the while loop, we need to get the number on each digit so I use `mid = num % 10` to get remainder and then accumlate all the remainder which is the same as get the sum of digits of random variable `num`, at the end of each round of the while loop, I divide `num` by 10 so we can get the digits one by one.


<br />

# Question 3 (Euler Problem 76) 

### Question: How many different ways can one hundred be written as a sum of at least two positive integers?

<br />

part of solution code:
```
            if j == i:
                val = 1
            elif j > i:
                val = 0
            elif j == 0:
                val = par[i][j + 1]
                """
                if j equals to 0 here, I will do the partition as par[i][j+1]
                """
            else:
                val = par[i][j + 1] + par[i - j][j]
                """
                Otherwise, I will do the partition as 
                par[i][j + 1] + par[i - j][j]
                """
            par[i][j] = val
```

### Explanation for my solution: 
firstly, I created a function named `compute` and we have a random variable `limit` in the parenthesis mark. I set up an empty list for `par` at the beginning. The first for loop is to set random variable `i` from range 0 to `limit + 1`, and the second for loop to set `j` from range 0 to reversed `limit +1` 

And the above combination of if, elif, else is to make the partition algorithm. I will just use an example to illustrate how this code works.

`Example:` We can use number 6. 
We have the following 3 methods to get the result of 6 without using all the 1s.
<br />
5+1
<br />
4+2
<br />
3+3

If we use 1 to let the algorithm expand then have the following as our algorithms for number 6. Thus, 6 has 10 addition method in total. 
<br />
5+1
<br />
  4+1+1
  <br />
    3+1+1+1
    <br />
      2+1+1+1+1
      <br />
        1+1+1+1+1+1
        <br />
    2+2+1+1
    <br />
  3+2+1
  <br />
4+2
<br />
  2+2+2
  <br />
3+3

Finally, we use the same method to get the result of 100, so we get the result is 190569291. This is a very complex loop to get the result. 

