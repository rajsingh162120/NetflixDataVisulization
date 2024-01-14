import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read the CSV file
netflix_data = pd.read_csv("https://raw.githubusercontent.com/rajsingh162120/NetflixDataVisulization/"
                           "master/Netflix-Changed.csv")


def extract_actors(netflix_data):
    # Make a copy to avoid modifying the original DataFrame
    netflix_data=netflix_data.copy()

    # Drop NaN values in 'cast' column
    netflix_data=netflix_data.dropna(subset=['cast'])

    # Use .str.split() to split the 'cast' column and assign it to 'actors'
    netflix_data['actors']=netflix_data['cast'].str.split(', ')

    return netflix_data


def get_country_data(netflix_data, selected_country):
    country_df=netflix_data[netflix_data['country'] == selected_country]
    return country_df


def get_top_actors(netflix_data, selected_country):
    country_df=get_country_data(netflix_data, selected_country)
    if 'cast' in country_df.columns and not country_df['cast'].isnull().all():
        country_df=country_df.dropna(subset=['cast'])
        top_actors=country_df['cast'].str.split(', ').explode().value_counts().head(10)
        return top_actors
    else:
        return None


def analyze_actors(netflix_data):
    netflix_data=extract_actors(netflix_data)
    all_actors=[actor for sublist in netflix_data['actors'].tolist() for actor in sublist]
    actor_frequency=pd.Series(all_actors).value_counts()
    return actor_frequency


def calculate_rating_frequency(netflix_data):
    rating_counts=netflix_data['rating'].value_counts()
    return rating_counts


def calculate_movie_show_proportion(netflix_data):
    movie_show_counts=netflix_data['type'].value_counts()
    return movie_show_counts


def plot_movie_show_proportion_pie(movie_show_counts):
    colors=['red', 'white']  # Red and White colors
    fig=px.pie(values=movie_show_counts, names=movie_show_counts.index)

    # Set the overall color of the chart
    fig.update_traces(marker=dict(colors=colors))

    return fig


# Mapping of movie ratings to numerical values
rating_mapping={
    'G': 1,
    'NC-17': 2,
    'NR': 3,
    'PG': 4,
    'PG-13': 5,
    'R': 6,
    'TV-14': 7,
    'TV-G': 8,
    'TV-MA': 9,
    'TV-PG': 10,
    'TV-17': 11,
    'TV-Y': 12,
    'TV-Y7': 13,
    'TV-Y7-FV': 14,
    'UR': 15,
    'N/A': 0  # Add this line to handle the 'N/A' values
}

# Convert movie ratings to numerical values using the mapping
netflix_data['numeric_rating']=netflix_data['rating'].map(rating_mapping)


def compare_ratings_across_genres(netflix_data):
    genre_ratings=netflix_data.groupby('listed_in')['numeric_rating'].mean().sort_values(ascending=False)
    return genre_ratings


def compare_ratings_across_directors(netflix_data):
    director_ratings=netflix_data.groupby('director')['numeric_rating'].mean().sort_values(ascending=False)
    return director_ratings


def top_10_directors(netflix_data):
    top_directors=netflix_data['director'].value_counts().head(10)
    return top_directors


def top_genre(netflix_data):
    top_genre=netflix_data['listed_in'].value_counts().idxmax()
    return top_genre


def get_total_shows(data):
    return len(data)


def get_release_year_distribution(data):
    release_year_counts=data['release_year'].value_counts().reset_index()
    release_year_counts.columns=['Release Year', 'Number of Shows']
    fig_year=px.bar(release_year_counts, x='Release Year', y='Number of Shows', title='Distribution by Release Year',
                    color='Release Year', color_continuous_scale='reds')
    return fig_year


def visualize_top_years(data):
    top_years=data['release_year'].value_counts().head(10)

    fig_top_years=px.bar(
        x=top_years.index,
        y=top_years.values,
        labels={'x': 'Year', 'y': 'Number of Shows'},
        title='Last 10 Years - Number of Shows',
        # color=top_years.index,
        color_discrete_sequence=['red'] * len(top_years.index)
    )

    return fig_top_years


def get_genre_distribution(data):
    genres_count=data['listed_in'].str.split(',').explode().value_counts().reset_index()
    genres_count.columns=['Genre', 'Number of Shows']
    fig_genres=px.bar(genres_count, x='Genre', y='Number of Shows', title='Top Genres', color='Genre',
                      color_discrete_sequence=['red'])
    return fig_genres


def get_top_directors(data):
    directors_count=data['director'].value_counts().reset_index()
    directors_count.columns=['Director', 'Number of Shows']
    top_directors=directors_count.head(10)
    fig_directors=px.bar(top_directors, x='Director', y='Number of Shows', title='Top Directors', color='Director',
                         color_discrete_sequence=['red'])
    return fig_directors


def get_top_cast_members(data):
    cast_count=data['cast'].str.split(',').explode().value_counts().reset_index()
    cast_count.columns=['Cast Member', 'Number of Shows']
    top_cast=cast_count.head(10)
    fig_cast=px.bar(top_cast, x='Cast Member', y='Number of Shows', title='Top Cast Members', color='Cast Member',
                    color_discrete_sequence=['red'])
    return fig_cast


def show_ratios(selected_country, data):
    if selected_country:

        # Filter dataset for the selected country
        country_data=data[data['country'].str.contains(selected_country, case=False, na=False)]
        total_country=len(country_data)
        movie_count_country=len(country_data[country_data['type'] == 'Movie'])
        show_count_country=len(country_data[country_data['type'] == 'TV Show'])

        if total_country > 0:
            movie_ratio_country=movie_count_country / total_country
            show_ratio_country=show_count_country / total_country

            st.write(
                f"For {selected_country}, Movie ratio: {movie_ratio_country:.2f}, Show ratio: {show_ratio_country:.2f}")

            # Visualization - Pie chart for movie and show ratio for the selected country
            labels=['Movies', 'TV Shows']
            sizes=[movie_count_country, show_count_country]
            colors=['red', 'white']
            explode=(0.1, 0)

            fig1, ax1=plt.subplots(figsize=(6, 6))  # Adjust the size by changing the figsize parameter
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            fig1.set_facecolor('black')
            plt.title(f'{selected_country} Content Distribution')
            st.pyplot(fig1)
        else:
            st.write(f"No data available for {selected_country}")
    else:
        # Analyze overall movie and show ratio
        total=len(data)
        movie_count=len(data[data['type'] == 'Movie'])
        show_count=len(data[data['type'] == 'TV Show'])

        if total > 0:
            movie_ratio=movie_count / total
            show_ratio=show_count / total

            st.write(f"Overall, Movie ratio: {movie_ratio:.2f}, Show ratio: {show_ratio:.2f}")

            # Visualization - Pie chart for overall content distribution
            labels=['Movies', 'TV Shows']
            sizes=[movie_count, show_count]
            colors=['red', 'white']
            explode=(0.1, 0)

            fig1, ax1=plt.subplots(figsize=(6, 6))  # Adjust the size by changing the figsize parameter
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            fig1.set_facecolor('black')
            plt.title('Overall Content Distribution')
            st.pyplot(fig1)
        else:
            st.write("No data available")
