def sum(*n):
    total=0
    for n1 in n:
        total+=n1
    print("The sum: ", total)

sum(10,20,30,40,50)
sum(10,20,30,40)
sum(10,20,30)
sum(10,20)
sum(10)