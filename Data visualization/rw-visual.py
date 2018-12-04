import matplotlib.pyplot as plt
from random_walk import Random_walk


while True:
    rw = Random_walk(50000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
