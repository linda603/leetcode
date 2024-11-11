class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # primes[i] = largest prime <= i
        primes = self.largest_primes(max(nums))
        
        prev = 0
        for num in nums:
            upper_bound = num - prev - 1

            largest_prime = primes[upper_bound]
            
            if num - largest_prime <= prev:
                return False
            prev = num - largest_prime
        return True

    def is_prime(self, n):
        # if n < 2: return False
        for f in range(2, int(sqrt(n)) + 1): # convert to int will round down
            if n % f == 0:
                return False
        return True
    
    def largest_primes(self, n):
        primes = [0, 0]

        for i in range(2, n):
            if self.is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i - 1])
        return primes

# Time: O(m*sqrt(n) + n). n: len(nums), m: max(nums)
# Space: O(m)