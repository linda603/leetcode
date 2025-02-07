class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt_secret = {}
        cnt_guess = {}

        bulls = 0
        cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                continue
            cnt_secret[secret[i]] = 1 + cnt_secret.get(secret[i], 0)
            cnt_guess[guess[i]] = 1 + cnt_guess.get(guess[i], 0)
        
        for num in cnt_secret:
            if num in cnt_guess:
                cows += min(cnt_secret[num], cnt_guess[num])
        return str(bulls) + "A" + str(cows) + "B"