import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Enter city: ").lower()
        if city not in city_name:
            print("That's not a valid input")
            continue
        
        print('\n Attempted Input\n')
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter month (or 'all' for no month filter): ").lower()
        if month not in month_name:
            print("That's not a valid input")
            continue
        
        print('\n Attempted Input\n')
        break 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter day (or 'all' for no day filter): ").lower()
        if day not in day_name:
            print("That's not a valid input")
            continue
        
        print('\n Attempted Input\n')
        break 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
        df=df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
                                     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print(popular_month)

    # TO DO: display the most common day of week

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print(popular_day)
    
    # TO DO: display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station_counts = df['Start Station'].value_counts()

    most_popular_start_station = start_station_counts.index[0]

    print(most_popular_start_station)

    # TO DO: display most commonly used end station

    end_station_counts = df['End Station'].value_counts()

    most_popular_end_station = end_station_counts.index[0]

    print(most_popular_end_station)
    
    
    # TO DO: display most frequent combination of start station and end station trip

    df['both'] = df['Start Station'] + " & " + df['End Station']

    both_station_counts = df['both'].value_counts()

    most_popular_both_station = both_station_counts.index[0]

    print(most_popular_both_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Diff'] = df['End Time'] - df['Start Time']

    print(df['Diff'].sum())

    # TO DO: display mean travel time

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Diff'] = df['End Time'] - df['Start Time']

    print(df['Diff'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_counts = df['User Type'].value_counts()
    print(user_counts)
    
    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        print(int(df['Birth Year'].min()))
        print(int(df['Birth Year'].max()))
        print(int(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Displays 5 rows of data from the dataframe at a time.

    Args:
        df: The dataframe containing bikeshare data.
    """
    view_data = input("Would you like to view the first 5 rows of individual trip data? Enter yes or no: ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue viewing the next 5 rows? Enter yes or no: ").lower()
        if view_data != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
