##################################################
##  Problem 5b. Find order
##################################################

# Given a tuple of order id's, find the index of a particular
# order id, or return None if it doesn't exist
def find_order(all_orders, order):
    '''
    Inputs:
        all_orders (tuple(int)) | Tuple of unique positive integer order id's
        order      (int)        | Positive integer order id to find
    Output:
        -          (int)        | Index of order id if it exists, otherwise None
    '''
    ##################
    # YOUR CODE HERE #
    #use binary search O(logn)

    #finding min
    def find_trough(nums):
        start = 0
        end= len(nums)-1
        last_val = nums[len(nums)-1]
        while start < end:
            mid = int((start+end)/2)
            if nums[mid] < last_val:
                end = mid
            else:
                start = mid+1
        return start

    pivot = find_trough(all_orders)
    s1 = 0
    e1 = pivot-1

    s2 = pivot
    e2 = len(all_orders)-1

    if order > all_orders[e2]:
        while s1 <= e1:
            mid = int((s1+e1)/2)
            if all_orders[mid] == order:
                return mid
            elif all_orders[mid] > order:
                e1 = mid -1
            else:
                s1 = mid + 1
    else:
        while s2 <= e2:
            mid = int((s2+e2)/2)
            if all_orders[mid] == order:
                return mid
            elif all_orders[mid] > order:
                e2 = mid -1
            else:
                s2 = mid + 1
    return None
    ##################
