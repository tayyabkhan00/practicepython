import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 51)
y = np.random.randint(10, 100, 50)

print("x values:", x)
print("y values:", y)

fig, axs = plt.subplots(5, 2, figsize=(12, 18))

axs = axs.ravel()

axs[0].plot(x, y)
axs[1].bar(x, y)
axs[2].scatter(x, y)
axs[3].hist(y)
axs[4].boxplot(y)
axs[5].pie([30, 40, 30], labels=["A","B","C"])
axs[6].stem(x[:20], y[:20])
axs[7].plot(x, np.cumsum(np.random.randn(50)))
axs[8].violinplot(y)
axs[9].plot(sorted(y), np.linspace(0,1,50))

plt.tight_layout()
plt.show()
