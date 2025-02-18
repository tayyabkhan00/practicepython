def my_generators():
    for i in range(10):
        yield i
gen=my_generators()
for j in gen:
    print(j)