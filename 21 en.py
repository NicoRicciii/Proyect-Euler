from math import floor

# in the sumdiv's list, we can save the d() of
# each number, adding each divisor i to every multiple of i

sumdiv = [0 for k in range(0, 10000)]
for i in range(1, 10000):
    for j in range(2, floor(9999/i)+1):
        sumdiv[j*i] += i

# for each k, we can verify either k is an amicable number or not 
# in order for that to happen, 
# d(k) != k, d(d(k)) = k, so that k has a distinct pair
# furthermore, this pair should be <= 10000 as well

amsum = 0
for k in range(1, 10000):
    if sumdiv[k] != k and sumdiv[k] <= len(sumdiv):
        if sumdiv[sumdiv[k]] == k:
            amsum += k

print(amsum)

