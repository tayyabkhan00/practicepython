import time
# print(4)
# time.sleep(3)
# # time.sleep() will print after given sec
# print("this will run after 3 seconds")
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)