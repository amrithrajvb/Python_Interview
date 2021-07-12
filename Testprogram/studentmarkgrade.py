physics = int(input("enter the physics mark"))
chemistry = int(input("enter the Chemistry mark"))
maths = int(input("enter the maths mark"))
social = int(input("enter the social mark"))
compter = int(input("enter the computer mark"))


total=physics + chemistry + maths + social + compter
print("total mark=", total)

if total > 90:
    print("you are awarded A+")
elif 80 < total < 90:
    print("A")
elif 70 < total < 60:
    print("b+")
elif 50 <total< 60:
    print("b")
elif 40 < total < 50:
    print("d")
else:
    print("failed")
# print("your total mark=", physics + chemistry + maths + social + compter )
#
# print("your avarege score is", (physics + chemistry + maths + social + compter) / 5 )

print("average mark", (total )/ 5)