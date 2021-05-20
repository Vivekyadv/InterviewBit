# Given array, Count the number of ways to split all the elements of the 
# array into 3 contiguous parts so that the sum of elements in each part 
# is the same.


def partition(A,B):
    total = sum(B)
    if total % 3 == 0:
        target = total // 3
    else: return 0
    ans = 0
    f = 0
    ele_sum = 0
    for i in range(A - 1):
        ele_sum += B[i]
        if ele_sum == 2 * target:
            ans += f
        if ele_sum == target:
            f += 1
    return ans

def partition2(A, B):
        if(sum(B)%3!=0):
            return 0
        target=sum(B)//3
        prefix_sum=[0]*(A)
        suffix_arr=[0]*(A)
        for i in range(A):
            prefix_sum[i]=prefix_sum[i-1]+B[i]
        temp=0
        for i in range(A-1,-1,-1):
            temp+=B[i]
            if(temp==target):
                suffix_arr[i]=1
        
        ans=0
        for i in range(A):
            if(prefix_sum[i]==target):
                for j in range(i+2,A):
                    if(suffix_arr[j]==1):
                        ans += 1
        return ans


arr = [5,4,0,9,0,9]
print(partition(len(arr), arr))
print(partition2(len(arr), arr))
