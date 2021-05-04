import matplotlib.pyplot as plt

labels = ["Lithuania", "Roamnia", "Poland", "Bangladesh", "Brazil", "Colombia", "Others"]

data = [2,17,1,2,2,2,6]
plt.pie(data, labels = labels, shadow = True, explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1])
plt.show()