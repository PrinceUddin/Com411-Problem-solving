import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)

x = ["poland","Romania", "Bangladesh"]
y =[2,17,2]
y2 = [5,6,12]
y3 = [1,1,3]
axes[0,0] .plot(x,y)
axes[0,1] .pie(y2, labels = x)
axes[1,1] .bar(x,y3)

plt.show()