import pandas as pd


def main():

    filePath = 'netflix_titles.csv'

    df = pd.read_csv(filePath)

    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    df['year_added'] = df['date_added'].dt.year
    count_by_year = df.groupby(
        ['year_added', 'type']).size().unstack(fill_value=0)

    count_by_year.to_csv('NetflixYearlyData.csv')


if __name__ == "__main__":
    main()
