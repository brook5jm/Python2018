#Jordan Brooks
#New baseball statistic calculator
#PAM = Pitcher Accuracy Metric
#Calculates average PAM value

x = input('Enter the Pitchers name: ')

a = eval(input('Enter all the PAMs you recorded seperated by a comma: '))

print("The PAM of all the pitches thrown were " + str(a)) 

print("The average PAM for "  + x +  " is")

print(sum(a) / len(a))

#Essentially calculates average of values you input
#Data collection method for PAM is still uncertain