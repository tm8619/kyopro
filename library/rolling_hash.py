#長さnの文字列s
#s[i:j]のハッシュ値:
#(hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1
#((hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1)*(10**10) + (hash2[j]-hash2[i]*power2[j-i]%mod2)%mod2
import random
base1 = 1007
mod1 = 10**9+7
base2 = 2009
mod2 = 10**9+9
modTank1 = [3000012541,3000012553,3000012563,3000012649,3000012683,3000012709]
mod1 = modTank1[random.randint(0,5)]
modTank2 = [3000014753,3000014783,3000014833,3000014839,3000014891,3000015433]
mod2 = modTank2[random.randint(0,5)]
hash1 = [0]*(n+1)
power1 = [1]*(n+1)
hash2 = [0]*(n+1)
power2 = [1]*(n+1)


for i,e in enumerate(s):
    hash1[i+1] = (hash1[i]*base1 + ord(e))%mod1
    power1[i+1] = (power1[i]*base1)%mod1
    hash2[i+1] = (hash2[i]*base2 + ord(e))%mod2
    power2[i+1] = (power2[i]*base2)%mod2

def rolling_hash(i, j):
    return ((hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1)*(10**10) + (hash2[j]-hash2[i]*power2[j-i]%mod2)%mod2




import random
base1 = 1007
mod1 = 10**9+7
modTank1 = [3000012541,3000012553,3000012563,3000012649,3000012683,3000012709]
mod1 = modTank1[random.randint(0,5)]
base1 = 1007
mod1 = 10**9+7
hash1 = [0]*(n+1)
power1 = [1]*(n+1)
for i,e in enumerate(s):
    hash1[i+1] = (hash1[i]*base1 + ord(e))%mod1
    power1[i+1] = (power1[i]*base1)%mod1
def rolling_hash(i, j):
    return (hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1
