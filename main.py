import matplotlib.pyplot as plt


def calc_wfs(VGPRs):
    return min(32768 // (VGPRs * 32), 16)


# noinspection PyPep8Naming
def occupancy(VGPRs):
    WFs = calc_wfs(VGPRs)
    return WFs, WFs / 16


def print_table():
    prev = 16
    v = 1
    wfs = calc_wfs(v)
    print('|%3d|%2d|%2.2f' % (v, wfs, wfs / 16))
    for v in range(2, 256):
        wfs = calc_wfs(v)
        if wfs < prev:
            print('|%3d|%2d|%2.2f' % (v - 1, prev, prev / 16))
            print('|%3d|%2d|%2.2f' % (v, wfs, wfs / 16))
            prev = wfs


def create_plot():
    vgprs = range(1, 256)
    wfs = list(calc_wfs(v) for v in vgprs)

    fig, axis = plt.subplots()
    axis.plot(vgprs, wfs)
    plt.ion()
    plt.show()


if __name__ == '__main__':
    print_table()
    create_plot()
    plt.show()
