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
    while True:
        city = input("Which city would you like to explore ?")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month you want to explore, (January to june, else type 'all') ")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details specific to a particular day? If yes, type day name else type 'all'")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")

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
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    
    # ------ Filteration
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ", df['Month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of week  is ", df['Day'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['Hour'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common Start Station is " , df['Start Station'].mode()[0] , "\n")

    # TO DO: display most commonly used end station
    print("The most common end station is ", df['End Station'].mode()[0], "\n")


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['Combined'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel duration is ", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("Mean of travel time is ", df['Trip Duration'].mean(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
        # TO DO: Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        # TO DO: Display earliest, most recent, and most common year of birth
        mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mcyob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", eyob, "\n")
        print("The most recent year of birth is ", mryob, "\n")
        print("The most common year of birth is ", mcyob, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    if view_data == 'yes':
        start_loc = 1
        while True:
            print(df[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: yes or no ").lower()
            if view_display == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
