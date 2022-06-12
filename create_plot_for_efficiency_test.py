import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("--results-path", type = str, default = "results.csv",
                        help = "path to results (default: %(default)s)")
    parser.add_argument("--plot-path", type = str, default = "plots/plot.png",
                        help = "path to plot (default: %(default)s)")
    return parser


def main():
    args = create_parser().parse_args()

    df = pd.DataFrame()
    df['elapsed_time'] = pd.read_csv(args.results_path, header = None)
    y = df['elapsed_time'].to_numpy()

    x = np.arange(1, 101, 1)

    plt.xlabel("zapytania GET")
    plt.ylabel("czas [s]")
    plt.title("Zależność czasu odpowiedzi od numeru zapytania")

    plt.plot(x, y)
    plt.savefig(args.plot_path)


if __name__ == "__main__":
    exit(main())
