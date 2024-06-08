Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

def highest_rank(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    highest_rank = max(count.values())
    highest_ranks = [key for key, value in count.items() if value == highest_rank]
    
    return max(highest_ranks)
