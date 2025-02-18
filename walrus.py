# without using walrus operator:
# foods=list()
# while True:
#     food=input("what would you like:")
#     if food=="quit":
#         break
#     foods.append(food)
# with using walrus operator:
foods=list()
while(food:=input("what you like-"))!="quit":
    foods.append(food)
