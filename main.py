import streamlit as st
import pandas as pd
import helper

netflix_data=helper.netflix_data


def country_wise_analysis(netflix_data):
    st.title('Country-wise Visulization')

    country_list=netflix_data['country'].dropna().unique().tolist()
    country_list.sort()

    selected_country=st.selectbox('Select a Country', country_list)

    st.title(f"{selected_country} Data")

    # Placeholder functions from helper.py
    country_df=helper.get_country_data(netflix_data, selected_country)
    top_10_actors=helper.get_top_actors(netflix_data, selected_country)
    # Perform other analyses based on selected country

    st.write("Country-wise Data:")
    st.write(country_df)

    st.write("Top 10 Actors in " + selected_country + ":")
    st.write(top_10_actors)


def rating_analysis(netflix_data):
    st.title("Netflix Rating Data Visulization")

    st.write("Pie Chart for Movie and Show Proportion:")
    movie_show_proportion=helper.calculate_movie_show_proportion(netflix_data)
    fig=helper.plot_movie_show_proportion_pie(movie_show_proportion)
    st.plotly_chart(fig)

    # Display rating distribution
    st.write("Rating Distribution:")
    rating_distribution=helper.calculate_rating_frequency(netflix_data)
    st.bar_chart(rating_distribution, color='#FF0000')

    # Compare ratings across genres
    st.write("Compare Ratings Across Genres:")
    genre_ratings=helper.compare_ratings_across_genres(netflix_data)
    st.bar_chart(genre_ratings, color='#FF0000')

    # Compare ratings across directors
    st.write("Compare Ratings Across Directors:")
    director_ratings=helper.compare_ratings_across_directors(netflix_data)
    st.bar_chart(director_ratings, color='#FF0000')

    # Top 10 directors
    st.write("Top 10 Directors:")
    top_directors=helper.top_10_directors(netflix_data)
    st.write(top_directors)

    # Top genre
    st.write("Top Genre:")
    top_genre=helper.top_genre(netflix_data)
    st.write(top_genre)


def country_movie_show_ratio(selected_country, data):
    st.sidebar.title("Netflix Movie and Show Analysis")
    # Display results for country-wise analysis
    st.header("Netflix Movie and Show Ratio Analysis")
    helper.show_ratios(selected_country, data)


def netflix_shows_analysis(data):
    # Display results for Netflix Shows Analysis
    st.header("Netflix Shows Analysis")

    # Number of shows
    total_shows=helper.get_total_shows(data)
    st.subheader(f'Total Number of Shows: {total_shows}')

    # Release year distribution
    st.subheader('Distribution by Release Year')
    fig_year=helper.get_release_year_distribution(data)
    st.plotly_chart(fig_year)

    #  Display top 10 years with the highest number of shows
    st.subheader('Last 10 Years-Number of Shows')
    fig_top_years=helper.visualize_top_years(data)
    st.plotly_chart(fig_top_years)

    # Genres distribution
    st.subheader('Distribution by Genres')
    fig_genres=helper.get_genre_distribution(data)
    st.plotly_chart(fig_genres)

    # Top Directors
    st.subheader('Top 10 Directors')
    fig_directors=helper.get_top_directors(data)
    st.plotly_chart(fig_directors)

    # Top Cast Members
    st.subheader('Top 10 Cast Members')
    fig_cast=helper.get_top_cast_members(data)
    st.plotly_chart(fig_cast)


def main():


    # Set page configuration with default layout
    st.set_page_config(
        page_title="Netflix Data Visualization",
        page_icon=":popcorn:",
        initial_sidebar_state="expanded"
    )
    # Add CSS to dynamically adjust image width
    st.markdown(
        f"""
        <style>
            img {{
                max-width: 100%;
                width: 100%;
                height: auto;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )


    # Display the image with custom styling and caption
    st.sidebar.markdown(
        """
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/rajsingh162120/NetflixDataVisulization/master/logo.jpg" 
                 alt="Netflix"
            />
            <p style="color: white;">Netflix</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    hide_st_style="""
                  <style>
                  #MainMenu {visibility: hidden;}
                  footer {visibility: hidden;}
                  </style>
                  """
    
    st.markdown(hide_st_style,unsafe_allow_html=True)
    
    analysis_options=[
        "Country-wise Visualization",
        "Netflix Rating Data Visualization",
        "Country-wise Movie & Show Ratio",
        "Netflix Shows Analysis"
    ]
    user_menu=st.sidebar.selectbox("Select Menu", analysis_options)

    if user_menu == 'Country-wise Visualization':
        country_wise_analysis(netflix_data)
    elif user_menu == 'Netflix Rating Data Visualization':
        rating_analysis(netflix_data)
    elif user_menu == 'Country-wise Movie & Show Ratio':
        selected_country=st.sidebar.text_input("Enter a country name (Press Enter for overall ratio):").strip()
        country_movie_show_ratio(selected_country, netflix_data)
    elif user_menu == 'Netflix Shows Analysis':
        netflix_shows_analysis(netflix_data)


if __name__ == "__main__":
    main()
