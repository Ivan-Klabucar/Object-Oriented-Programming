#4. CETVRTI
import numpy as np
    
def DistributionTester(distribution, percentile_finder):
    numbers = distribution()
    for x in range(10,100,10):
        print(f'{x}th percentile: {percentile_finder(x, numbers)}')
    return numbers

def numgen_seqential(lower_lim, upper_lim, step):
    return [x for x in range(lower_lim, upper_lim, step)]

def numgen_normal(mean, stddev, n):
    return list(np.random.normal(mean, stddev, n))

def numgen_fibonacci(n):
    if n == 0: return []
    if n == 1: return [0]
    r = [0, 1]
    for i in range(n - 2):
        r.append(r[-1] + r[-2])
    return r

def percentile_way1(percentile, numbers):
    n_p = percentile*len(numbers)/100 + 0.5
    sorted_nums = sorted(numbers)
    return sorted_nums[int(round(n_p)) - 1]

def percentile_way2(percentile, numbers):
    sorted_nums = sorted(numbers)
    last_percentile = None
    for i in range(len(sorted_nums)):
        curr_p = 100*((i + 1)-0.5)/len(numbers)
        if curr_p > percentile:
            if i == 0: return sorted_nums[i]
            return sorted_nums[i-1] + len(numbers) * (percentile-last_percentile)*(sorted_nums[i]-sorted_nums[i-1])/100
        last_percentile = curr_p
    return sorted_nums[-1]

print("distribution of [1,100] with step 1 with percentile calculation way1:")
d = DistributionTester(distribution=lambda: numgen_seqential(1,101,1), percentile_finder=percentile_way1)
print()

print("normal distribution with mu=200, std=1 with 1000 numbers with percentile calculation way1:")
d = DistributionTester(distribution=lambda: numgen_normal(200, 1, 1000), percentile_finder=percentile_way1)
print()

print("Fibonacci distribution with with 100 numbers with percentile calculation way1:")
d = DistributionTester(distribution=lambda: numgen_fibonacci(100), percentile_finder=percentile_way1)
print()

print("distribution of [1,100] with step 1 with percentile calculation way2:")
d = DistributionTester(distribution=lambda: numgen_seqential(1,101,1), percentile_finder=percentile_way2)
print()

print("normal distribution with mu=200, std=1 with 1000 numbers with percentile calculation way2:")
d = DistributionTester(distribution=lambda: numgen_normal(200, 1, 1000), percentile_finder=percentile_way2)
print()

print("Fibonacci distribution with with 100 numbers with percentile calculation way2:")
d = DistributionTester(distribution=lambda: numgen_fibonacci(100), percentile_finder=percentile_way2)
print()

        




