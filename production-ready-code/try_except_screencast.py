import pandas as pd


def read_data(file_pth):
    try:
        df = pd.read_csv(file_pth)
        print(df)
        return df
    except FileNotFoundError:
        print("find does not exist")


if __name__ == "__main__":
    read_data("fake_path.csv")
