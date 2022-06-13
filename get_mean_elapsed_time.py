import pandas as pd
import numpy as np
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("--results-path", type = str, default = "results.csv",
                        help = "path to results (default: %(default)s)")
    return parser


def main():
    args = create_parser().parse_args()

    df = pd.DataFrame()
    df['elapsed_time'] = pd.read_csv(args.results_path)
    y = df['elapsed_time'].to_numpy()

    m = np.mean(y)
    print(m)

if __name__ == "__main__":
    exit(main())
