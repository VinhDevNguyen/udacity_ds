import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    # reading csv files using pandas
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merging above dataframes
    merged_df = messages.merge(categories, on = ['id'])
    return merged_df


def clean_data(df):
    # Create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)
    
    # Select the first row of the categories dataframe
    row = categories.iloc[0]

    # Rename the column name
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].transform(lambda x: x[-1:])

        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
        
        # replace 2s with 1s in related column
        categories['related'] = categories['related'].replace(to_replace=2, value=1)
        
    # replacing categories column in df with new category columns.
    df = df.drop('categories', axis=1)

    # concatenating the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)

    # removing duplicates
    cleaned_df = df.drop_duplicates(keep='first')
    return cleaned_df


def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+ str(database_filename))
    df.to_sql("disaster_response_data", engine, index=False,if_exists='replace')
    pass


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()