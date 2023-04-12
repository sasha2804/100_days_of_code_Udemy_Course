

# arr = [5,4,2,1]


# arr[0] = 3

# print(arr)



def rec(x):

    if x != 1:
        print('before: ', x)
        rec(x-1) 
        
        print('after: ', x)
  


rec(5)

        
    
