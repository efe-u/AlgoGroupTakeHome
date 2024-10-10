# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer

# Time Complexity <- O(n^2)
# Space Complexity <- O(1)
# This is most basic and brute force approach one can take. You look at every element in the list
# and compare it to every other element in the list. If they are the same, you've found your duplicate.

def findDuplicate(input: List[int]) -> int:
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[i] == input[j]:
                return input[i]
    return 0


# Time Complexity <- O(nlog(n))
# Space Complexity <- O(1)
# As the previous solution was very time taking, even sorting the array out first (in an increasing order by default
# but it could also be decreasing as well) is faster. I just used the built-in sort function if that is fine.

def findDuplicate2(input: List[int]) -> int:
    input.sort()
    for i in range(len(input)):
        if input[i] == input[i+1]:
            return input[i]
    return 0

# Time Complexity <- O(n)
# Space Complexity <- O(1)
# It is very lucky I got this problem because I did discuss and research this before with a friend while I was
# taking AP CSA. The idea behind this solution is that as all integers in the domain [1,N] appear at least once,
# so if we just check the index for every element (List[value of element]), then we shouldn't check any index twice.
# Any already checked index is a duplicate. Although we can't just change it to any value such as "0" either, 
# because then what happens if we change something the loop hasn't reached yet and we already lose the data by 
# changing it to 0. Then the whole thing falls apart. So we have to indicate the index has already been checked
# without losing the value. For that we can just assign the value its negative and omit the negative when it is turn
# to check the index the value points to.
# Say we have [3,2,4,1,4]. We check index [2], it is 4, so we change it to -4. We check index [1], it is 2, so we
# change it to -2. When we get to index [4], the last step, we check the index, it is negative; therefore, [5] must
# be the duplicate.

def findDuplicate3(input: List[int]) -> int:
    for i in range(len(input)):
        if input[abs(input[i])-1] < 0:
            return input[i]
        input[i] = -input[i]
    return 0

# Tests (I hope this is enough?)
test1 = []
for i in range(1,100):
    test1.append(i)
test1.append(1)

test2 = [1,3,2,4,4,5,7,6,8,9,10]

test3 = [10,8,9,4,5,2,3,6,8,7,1]

if 1 == findDuplicate(test1) and 1 == findDuplicate2(test1) and 1 == findDuplicate3(test1):
    print("Test 1 works!")

if 4 == findDuplicate(test2) and 4 == findDuplicate2(test2) and 4 == findDuplicate3(test2):
    print("Test 2 works!")

if 8 == findDuplicate(test3) and 8 == findDuplicate2(test3) and 8 == findDuplicate3(test3):
    print("Test 3 works!")
