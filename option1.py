# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

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

def findDuplicate(input: list[int]) -> int:
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] == list[j]:
                return list[i]
    return 0


# Time Complexity <- O(nlog(n))
# Space Complexity <- O(1)
# As the previous solution was very time taking, even sorting the array out first (in an increasing order by default
# but it could also be decreasing as well) is faster. I just used the built-in sort function if that is fine.

def findDuplicate2(input: list[int]) -> int:
    list.sort()
    for i in range(len(list)):
        if list[i] == list[i+1]:
            return list[i]
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

def findDuplicate3(input: list[int]) -> int:
    for i in range(len(list)):
        if list[abs(list[i])] < 0:
            return list[i]
        list[i] = -list[i]
    return 0

# Test 1
test1 = []
for i in range(1,100):
    test1.append(i)
test1.append(1)

print(test1)
print(findDuplicate(test1))
print(findDuplicate2(test1))
print(findDuplicate3(test1))