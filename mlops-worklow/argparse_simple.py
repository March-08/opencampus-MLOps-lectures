import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def go(args):
    logging.info("info here")
    logging.warning("warning here")
    logging.error("error here")

    logger.info(f"{args.number_1}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tutorial on argparser")

    parser.add_argument(
        "--number_1", type=float, help="enter the firs number", required=True
    )

    parser.add_argument(
        "--number_2",
        type=float,
        help="enter the second number",
        default=3.14,
        required=False,
    )

    args = parser.parse_args()
    go(args)
