import os
import pandas as pd
import numpy as np
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("--results-dir", type = str, default = "result/multi_mtd_5000",
                        help = "path to dir with results (default: %(default)s)")
    return parser


def main():
    args = create_parser().parse_args()

    results = dict()

    df = pd.DataFrame()
    for i, filename in enumerate(os.listdir(args.results_dir)):
        filepath = os.path.join(args.results_dir, filename)
        df[i] = pd.read_csv(filepath)

        results[i] = df[i].to_numpy()

        mean_time = np.mean(results[i])
        print(f"Client {i} - mean elapsed time: {round(mean_time, 3)}")

        max_time = np.max(results[i])
        print(f"Client {i} - max elapsed time: {round(max_time, 3)}")

if __name__ == "__main__":
    exit(main())
