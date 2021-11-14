import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris


def pca_use_org(data):
    cov_matrix = np.cov(data, rowvar=False)
    l, v = np.linalg.eig(cov_matrix)
    l_index = np.argsort(l)[::-1]
    l_ = l[l_index]
    v_ = v[:, l_index]
    data_trans = np.dot(data, v_)
    return data_trans, v_


if __name__ == "__main__":
    d_index = [0, 2]
    iris = load_iris()
    data = iris.data
    data = data[:, d_index]

    print('data=', data)
    data -= data.mean(axis=0)
    print('data=', data)

    data_trans, v = pca_use_org(data)

    vec_s = [0, 0]
    vec_1st_e = [2 * v[0, 0], 2 * v[0, 1]]
    vec_2nd_e = [2 * v[1, 0], 2 * v[1, 1]]

    plt.figure(figsize=[8, 8])
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.quiver(vec_s[0], vec_s[1], vec_1st_e[0], vec_1st_e[1],
               angles='xy', scale_units='xy', scale=1, color='r', label='1st')
    plt.quiver(vec_s[0], vec_s[1], vec_2nd_e[0], vec_2nd_e[1],
               angles='xy', scale_units='xy', scale=1, color='b', label='2nd')
    plt.grid()
    plt.legend()
    plt.scatter(data[:, 0], data[:, 1], c=iris.target)
    # plt.savefig('charts/fig-3.png')

    plt.figure(figsize=[8, 8])
    plt.subplot2grid((4, 1), (0, 0), rowspan=2)
    plt.title('1st principal - 2nd principal')
    plt.grid()
    plt.scatter(data_trans[:, 0], data_trans[:, 1], c=iris.target)
    plt.subplot2grid((4, 1), (2, 0))
    plt.tick_params(labelleft="off", left="off")
    plt.title('1st principal')
    plt.grid()
    plt.scatter(data_trans[:, 0], np.zeros(len(data_trans[:, 0])), c=iris.target)
    plt.subplot2grid((4, 1), (3, 0))
    plt.title('2nd principal')
    plt.grid()
    plt.tick_params(labelleft="off", left="off")
    plt.scatter(data_trans[:, 1], np.zeros(len(data_trans[:, 1])), c=iris.target)
    plt.tight_layout()
    plt.show()
