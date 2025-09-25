# 1 to 9

sumL= 0

digitsum = len('onetwothreefourfivesixseveneightnine')

sumL += digitsum

print(sumL)

#10 to 19

tenssum = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')

sumL += tenssum

# 20-99

tnsum = 10*len('twentythirtyfortyfiftysixtyseventyeightyninety') + 8*digitsum

sumL += tnsum

#100-999

hsum = 99*9*len('and') + digitsum*100+len('hundred')*900 + 9*(digitsum+tenssum+tnsum)

sumL += hsum



#1000

sumL += len('onethousand')

print(sumL)
