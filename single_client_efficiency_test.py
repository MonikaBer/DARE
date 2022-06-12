from argparse import ArgumentParser
import requests
import time

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("--url", type = str, default = "http://localhost:8080",
                        help = "URL for HTTP GET request (default: %(default)s)")
    parser.add_argument("--requests-count", type = int, default = 5000,
                        help = "requests count (default: %(default)s)")
    parser.add_argument("--results-path", type = str, default = "results.csv",
                        help = "path to results (default: %(default)s)")
    return parser


def main():
    args = create_parser().parse_args()

    open(args.results_path, "w").close()

    with open(args.results_path, "a") as f:
        for i in range(args.requests_count):
            start_time = time.time()        # current time in seconds
            response = requests.get(args.url)
            elapsed_time = time.time() - start_time

            f.write(f'{elapsed_time}\n')
            print(f'{i}/{args.requests_count}')


if __name__ == "__main__":
    exit(main())
