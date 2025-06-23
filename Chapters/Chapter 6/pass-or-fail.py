p= int(input("Enter marks scored in Physics: "))
c= int(input("Enter marks scored in Chemistry: "))
m= int(input("Enter marks scored in Maths: "))

total_percentage=100*(p+c+m)/300 
print(f"Total marks scored : {total_percentage:.2f}%")

#Method 1
if(p>=33 and c>=33 and m >= 33):
    if(total_percentage>=40):
        print("You passed the Exam")
    else:
        print("You Failed, try again next year")
elif(p<33 and c<33 and m <33):
    print("YOu failed all subjects. Work Hard!")
elif(p<33 or c<33 or m<33):
    if(p<33):
        print("You failed in Physics")
    if(c<33):
        print("You failed in Chemistry")
    if(m<33):
        print("You failed in Maths")

#ethod 2
if(total_percentage >= 40 and p>=33 and c>=33 and m>=33):
    print("You passed the Exam")
else:
    print("You failed")