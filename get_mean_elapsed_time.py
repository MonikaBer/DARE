import pandas as pd
import numpy as np
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("--results-path", type = str, default = "result/plain_html/single_client_eff_rotation_test_1.csv",
                        help = "path to results (default: %(default)s)")
    return parser


def main():
    args = create_parser().parse_args()

    df = pd.DataFrame()
    df['elapsed_time'] = pd.read_csv(args.results_path)
    y = df['elapsed_time'].to_numpy()

    mean_time = np.mean(y)
    print(f"mean elapsed time: {mean_time}")

    max_time = np.max(y)
    print(f"max elapsed time: {max_time}")

if __name__ == "__main__":
    exit(main())
