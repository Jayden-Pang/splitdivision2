import math

iteration = 0
gcd2 = [2,4,6,8]
gcd3 = [3,6,9]
gcd4 = [4,8]
dividends = list()
divisors = list()
answer = list()

def gcd_equal_filled (x, y, target):
    if math.gcd(int(x),int(y)) == target:
        return True
    else:
        return False

def gcd_equal_blank (x, y):
    if x == "0" or y == "0":
        return True
    else:
        if math.gcd(int(x),int(y)) == 1:
            return True
        else:
            return False

def divide (dividend, divisor):
    remainder_divide = int(dividend)%int(divisor)
    multiplier_divide = int(dividend)-remainder_divide
    quotient_divide = multiplier_divide/int(divisor)
    return str(int(quotient_divide)), str(int(remainder_divide)), str(int(multiplier_divide))

def equal(dividend_1, divisor_1, dividend_2, divisor_2):
    sub_dividend_1 = dividend_1[:5]
    sub_dividend_2 = dividend_2[:5]
    blank = [0,2,3,4]
    for i in blank:
        if not gcd_equal_blank(sub_dividend_1[i], sub_dividend_2[i]):
            return False
    filled = [5,6]
    target = [2,3]
    for i in range(len(filled)):
        if not gcd_equal_filled(dividend_1[filled[i]],dividend_2[filled[i]],target[i]):
            return False
    blank = [1]
    for i in blank:
        if not gcd_equal_blank(divisor_1[i], divisor_2[i]):
            return False
    filled = [0,2,3]
    target = [3,2,2]
    for i in range(len(filled)):
        if not gcd_equal_filled(divisor_1[filled[i]],divisor_2[filled[i]],target[i]):
            return False
    quotient_equal_1, remainder_equal_1, multiplier_equal_1 = divide(sub_dividend_1, divisor_1)
    quotient_equal_2, remainder_equal_2, multiplier_equal_2 = divide(sub_dividend_2, divisor_2)
    blank = [0,1,2,3]
    for i in blank:
        if not gcd_equal_blank(multiplier_equal_1[i], multiplier_equal_2[i]):
            return False
    blank = [0,1,2,3]
    for i in blank:
        if not gcd_equal_blank(remainder_equal_1[i], remainder_equal_2[i]):
            return False
    filled = [4]
    target = [2]
    for i in range(len(filled)):
        if not gcd_equal_filled(multiplier_equal_1[filled[i]],multiplier_equal_2[filled[i]],target[i]):
            return False
    sub_dividend_1 = remainder_equal_1 + dividend_1[5]
    sub_dividend_2 = remainder_equal_2 + dividend_2[5]
    quotient_equal_1, remainder_equal_1, multiplier_equal_1 = divide(sub_dividend_1, divisor_1)
    quotient_equal_2, remainder_equal_2, multiplier_equal_2 = divide(sub_dividend_2, divisor_2)
    blank = [0]
    for i in blank:
        if not gcd_equal_blank(quotient_equal_1[i], quotient_equal_2[i]):
            return False
    blank = [1]
    for i in blank:
        if not gcd_equal_blank(multiplier_equal_1[i], multiplier_equal_2[i]):
            return False
    blank = [0,2]
    for i in blank:
        if not gcd_equal_blank(remainder_equal_1[i], remainder_equal_2[i]):
            return False
    filled = [2]
    target = [3]
    for i in range(len(filled)):
        if not gcd_equal_filled(multiplier_equal_1[filled[i]],multiplier_equal_2[filled[i]],target[i]):
            return False
    filled = [1,3]
    target = [3,2]
    for i in range(len(filled)):
        if not gcd_equal_filled(remainder_equal_1[filled[i]],remainder_equal_2[filled[i]],target[i]):
            return False
    sub_dividend_1 = remainder_equal_1 + dividend_1[6]
    sub_dividend_2 = remainder_equal_2 + dividend_2[6]
    quotient_equal_1, remainder_equal_1, multiplier_equal_1 = divide(sub_dividend_1, divisor_1)
    quotient_equal_2, remainder_equal_2, multiplier_equal_2 = divide(sub_dividend_2, divisor_2)
    blank = [0]
    for i in blank:
        if not gcd_equal_blank(multiplier_equal_1[i], multiplier_equal_2[i]):
            return False
    filled = [1,2,4]
    target = [3,2,2]
    for i in range(len(filled)):
        if not gcd_equal_filled(multiplier_equal_1[filled[i]],multiplier_equal_2[filled[i]],target[i]):
            return False
    filled = [0]
    target = [3]
    for i in range(len(filled)):
        if not gcd_equal_filled(remainder_equal_1[filled[i]],remainder_equal_2[filled[i]],target[i]):
            return False
    return True

for i in range(1,10):
    for j in range(7,8):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in gcd2:
                        for o in gcd3:
                            for a in gcd3:
                                for b in range(10):
                                    for c in gcd2:
                                        for d in gcd2:
                                            iteration += 1
                                            print(iteration)
                                            dividend = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)
                                            divisor = str(a)+str(b)+str(c)+str(d)
                                            sub_dividend = int(dividend[:5])
                                            quotient, remainder, multiplier = divide(sub_dividend, divisor)
                                            # quotient
                                            if int(quotient[0]) % 4 != 0 or quotient[0] == "0":
                                                continue
                                            # remainder
                                            if len(remainder) != 4:
                                                continue
                                            # multiplier
                                            if len(multiplier) == 5:
                                                if multiplier[4] == "0":
                                                    continue
                                            else:
                                                continue
                                            sub_dividend = remainder+dividend[5]
                                            quotient, remainder, multiplier = divide(sub_dividend, divisor)
                                            # remainder
                                            if len(remainder) == 4:
                                                if int(remainder[1]) % 3 != 0 or remainder[1] == "0" or int(remainder[3]) % 2 != 0 or remainder[3] == "0":
                                                    continue
                                            else:
                                                continue
                                            # multiplier
                                            if len(multiplier) == 4:
                                                if multiplier[0] != "9" or int(multiplier[2]) % 3 != 0 or multiplier[2] == "0" or multiplier[3] != "8":
                                                    continue
                                            else:
                                                continue
                                            sub_dividend = remainder+dividend[6]
                                            quotient, remainder, multiplier = divide(sub_dividend, divisor)
                                            # quotient
                                            if int(quotient) % 2 != 0 or quotient == "0":
                                                continue
                                            # multiplier
                                            if len(multiplier) == 5:
                                                if int(multiplier[1]) % 3 != 0 or multiplier[1] == "0" or int(multiplier[2]) % 2 != 0 or multiplier[2] == "0" or multiplier[3] != "7" or int(multiplier[4]) % 2 != 0 or multiplier[4] == "0":
                                                    continue
                                            else:
                                                continue
                                            # remainder
                                            if len(remainder) == 2:
                                                if int(remainder[0]) % 3 != 0 or remainder[0] == "0" or remainder[1] != "7":
                                                    continue
                                            else:
                                                continue
                                            dividends.append(dividend)
                                            divisors.append(divisor)


for i in range(len(dividends)-1):
    for j in range(i+1,len(dividends)):
        if equal(dividends[i],divisors[i],dividends[j],divisors[j]):
            answer.append([dividends[i],divisors[i],dividends[j],divisors[j]])

print(int(answer[0][0])+int(answer[0][2]))