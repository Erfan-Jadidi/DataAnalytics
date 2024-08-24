from matplotlib import pyplot as plt

x = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
y1 = [10, 5, 7, 9, 12, 14, 8]
y2 = [7, 15, 14, 13, 18, 12, 1]
# y1 = selling data for company A
# y2 = selling data for company B

plt.plot(x, y1, label="Company A")
plt.plot(x, y2, label="Company B")

plt.title("Title")
plt.xlabel("Days")
plt.ylabel("Total")
plt.legend()
plt.grid()
plt.show()
