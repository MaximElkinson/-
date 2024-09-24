import matplotlib.pyplot as plt

plt.plot([-100,100],[-52,48],c="b")
plt.plot([-4,100],[0,52],c="g")
plt.plot([6,0],[0,3],c="r")
plt.axhline(y=0, color="black", linestyle="--")
plt.axvline(color="black", linestyle="--")
plt.fill_between([-4,100],[0,52], facecolor="none", hatch="X", edgecolor="g", linewidth=0.0)
plt.fill_between([6,0],[0,3], facecolor="none", hatch="X", edgecolor="b", linewidth=0.0)
plt.show()