import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [10,15.5,18.2,20,25,36,40]

x1 = [1,2,3,4,5,6,7]
y1 = [10,25.5,28.2,30,35,46,50]

x2 = ["baby","toddler","teen","no one"]
y2 = [10,25,28,30]

plt.xlabel("age")
plt.ylabel("score")

plt.plot(x,y,"mo--")
plt.step(x1,y1,"g")
plt.bar(x2,y2, color = ["m","g","r","b"])

plt.show()