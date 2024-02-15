"""
Logging Exercise

Author: Marcello
Date: February 2023
"""

import logging

logging.basicConfig(
    filename="./results.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def sum_vals(first_number, second_number):
    """
    Args:
        first_number: (int)
        second_number: (int)
    Return:
        first_number + second_number (int)
    """
    try:
        logging.info("%s, %s", first_number, second_number)
        assert isinstance(first_number, (int, float))
        assert isinstance(second_number, (int, float))
        logging.info(
            "SUCCESS: numbers %s and %s were added correctly",
            first_number,
            second_number,
        )
        return first_number + second_number

    # assert goes in error, it will raise an AssertionError, so we need to
    # catch that
    except AssertionError:
        logging.error("ERROR: was not able to perform addition")
        return None


if __name__ == "__main__":
    sum_vals("no", "way")
    sum_vals(4, 5)
    sum_vals(3, "hello")
    # check the logs after
