import matplotlib.pyplot as plt
import pickle


def graph():
    with open("docs/pig_perfect_play.bin", "rb") as f:
        z_dics = pickle.load(f)

    plot2dto3d(z_dics)

    plt.xlim(100, 0)
    plt.xlabel("player 2 points")
    plt.ylabel("player 1 points")

    plt.show()


def plot2dto3d(z_dics):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    for i in z_dics.keys():
        x = list(z_dics[i].keys())
        y = list(z_dics[i].values())
        ax.plot(x, y, zs=i, zdir="y")

    ax.set_zlabel("round score")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
