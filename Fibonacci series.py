#Display Fibonacci Series 
nterms = int(input('How many terms?'))
#First two terms
n1,n2 = 0,1
count = 0
#Check if the number of terms is valid
if nterms <= 0:
   print ('enter positive number')
#if only one term
elif nterms == 1:
  print('Fibonacci series upto', nterms, ':')
  print(n1)
else:
    print('Fiboncci Sequence:')
    while count < nterms:
        print(n1)
        nth = n1 + n2
#update values
        n1=n2
        n2 = nth
        count += 1
    
