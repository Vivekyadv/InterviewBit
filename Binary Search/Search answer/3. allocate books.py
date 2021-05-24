# Given an array of int A of size N and an int B.
# College library has N bags,the ith book has A[i] no of pages.
# You have to allocate books to B number of students so that max no of 
# pages alloted to a student is minimum.

# Example: A = [12,34,67,90]    B = 2
# Book distribution -->   12 & (34 67 90) ---> max no of books = 191
# (12 34) & (67 90) --> max no of books = 157
# (12 34 67) & 90   --> max no of books = 113
# result = min(191,157,113) --> result = 113

# Algorithm: 
# Step 1: count noOfStudents having pages <= no_of_pages (mid value)
# Step 2: in while loop from min(arr) to sum(arr)
#             if noOfStudents < B:
#                 check left subarray
#             else: check right subarray
# Step 3: result = min_pages


def noOfStudents(arr, pages):
    count = 0
    students = 1
    for i in range(len(arr)):
        count += arr[i]
        if count > pages:
            count = arr[i]
            students += 1
    return students

def books(arr,B):
    if B > len(arr):
        return -1
    min_pages = max(arr)
    max_pages = sum(arr)
    while min_pages <= max_pages:
        mid = min_pages + (max_pages - min_pages)//2
        if noOfStudents(arr, mid) > B:
            # check right subarray
            min_pages = mid + 1
        else:
            max_pages = mid -1
    return min_pages 

arr = [12,34,67,90]
b = 2
print(books(arr, b))