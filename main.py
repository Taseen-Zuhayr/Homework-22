def multiply(nums):
    result = 1
    for num in nums:
        result = result * num 
    return result


nums = {2,3,6}

product = multiply(nums)

print("The product of all the numbers is:", product)