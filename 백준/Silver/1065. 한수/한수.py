n = int(input())

if n < 100: #less than 100, all are hansoo
    print(n)
else: #else more than 3 digits; gotta check
    ct = 99
    for i in range(100, n+1):
        num_sep = [int(i) for i in str(i)]
        d = list()
        #print('num_sep',num_sep)
        #find the subt of each num
        for i in range(1,len(num_sep)):
            d.append(num_sep[i]-num_sep[i-1])
        #print('d', d)
        
        val1 = d[0]
        for i in range(1, len(d)):
            if d[i] == d[i-1]:
                pass
                if i == len(d) - 1:
                    ct += 1
            else:
                break
    print(ct)
       