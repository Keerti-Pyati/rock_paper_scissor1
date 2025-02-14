# import random
# rock=0
# paper=1
# scissor=2
# user =int(input("enter the value from user side"))
# if user >= 3 or user <0:
#     print("you entered a invalid range")
# else:
#     computer=random.randint(0,2)
#     print("computer choose")
#     print(computer)
#     if computer==0 and user==2:
#      print("user loose")
#     elif computer < user:
#      print("user wins")
#     elif computer==2 and user==0:
#      print("user wins")
#     elif computer > user:
#      print("user loose")
#     elif user == computer:
#      print("grame is draw")




     #set related programs
set1={"A", 1, "B", 2, "C" , 3}
set2={"keerti"}
#print("size of set 1" + str(sys.getsizeof(set1)) +"by bytes")
# print(str(set1.__sizeof__()))
# print(str(set2.__sizeof__()))

#iteration through the set
# test_set=set("geEks")
# for val in test_set:
#     print(val)

#max and min value in the sets
def max(sets):
#return (max(sets))
 sets=set([8,16,24,1,25,3,10,65,55])
 print(max(sets))
