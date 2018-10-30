import matplotlib.pyplot as plt
# x-coordinates of left sides of bars
left=[1,2,3,4,5]
# heights of bars 
height=[10,24,36,40,5]
# labels for bars
tick=['one','two','three','four','five']
# plotting a bar chart
plt.bar(left,height,tick_label=tick,width=0.8,color=['green','red'])
#naming the x-axis
plt.xlabel("x-axis")
#naming the y-axis
plt.ylabel("y-axis")
plt.title("bar graph")
plt.show()