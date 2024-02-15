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
        a: (int)
        b: (int)
    Return:
        a + b (int)
    """
    try:
        total = first_number + second_number + 0
        logging.info(
            "SUCCESS: numbers %s and %s were added correctly",
            first_number,
            second_number,
        )
        return total
    except TypeError:
        logging.error("ERROR: was not able to perform addition")
        return None


if __name__ == "__main__":
    sum_vals("no", "way")
    sum_vals(4, 5)
    # check the logs after
