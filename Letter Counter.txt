d1 = {0 : "", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}

d2 = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen",
       18 : "eighteen", 19 : "nineteen"}

d3 = {0 : "", 1: "ten", 2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty", 7 : "seventy", 8 : "eighty", 9 : "ninety"}

def letterCounter(num):
    if num == 1000:
        return 11
    if len(str(num)) == 1:
        return len(d1[num])
    elif len(str(num)) == 2:
        if num < 20:
            return len(d2[num])
        else:
            return (len(d3[int(num / 10)]) + len(d1[int(num % 10)]))
    else:
        if num % 100 == 0:
            return (len(d1[int(num / 100)]) + 7)
        else:
            if num % 100 < 10:
                return (len(d1[int(num / 100)]) + 10 + len(d1[(num % 10)]))
            elif num % 100 < 20:
                return (len(d1[int(num / 100)]) + 10 + len(d2[(num % 100)]))
            else:
                return (len(d1[int(num / 100)]) + 10 + len(d3[int(num / 10 % 10)]) + len(d1[num % 10]))


res = 0
for i in range(1, 1001):
    res += letterCounter(i)

print(res)
