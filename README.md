# Netflix Data Visualization

![Netflix Logo](https://images.ctfassets.net/y2ske730sjqp/5QQ9SVIdc1tmkqrtFnG9U1/de758bba0f65dcc1c6bc1f31f161003d/BrandAssets_Logos_02-NSymbol.jpg?w=940)

This repository contains a Python application for visualizing and analyzing Netflix data. The application is built using Streamlit, pandas, and matplotlib, providing insights into country-wise visualization, Netflix rating data, movie and show ratios, and overall Netflix shows analysis.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly

Install the required dependencies using the following command:

```bash
pip install matplotlib==3.7.2
```
```bash
pip install pandas==2.0.3
```
```bash
pip install plotly==5.18.0
```
```bash
pip install streamlit==1.29.0
```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

## Application Features

### Country-wise Visualization

- **Select a country to analyze specific data.**
  - Choose a country from the available options to explore detailed insights into Netflix content specific to that country.
- **View country-wise data and top 10 actors.**
  - Gain a comprehensive view of Netflix content in the selected country, including information about the top 10 actors.

### Netflix Rating Data Visualization

- **Pie chart for movie and show proportion.**
  - Visualize the distribution of movies and TV shows using a pie chart.
- **Rating distribution across all shows.**
  - Explore the distribution of ratings across the entire dataset.
- **Compare ratings across genres, directors, and visualize top directors.**
  - Analyze how ratings vary across genres and directors. Visualize the top directors based on their average ratings.
- **Explore the top genre and top 10 directors.**
  - Identify the most popular genre and the top 10 directors in the Netflix dataset.

### Country-wise Movie & Show Ratio

- **Analyze movie and show ratios for a specific country.**
  - Understand the distribution of movies and TV shows for the selected country.
- **Visualize the content distribution with a pie chart.**
  - Use a pie chart to visually represent the proportion of movies and TV shows.

### Netflix Shows Analysis

- **View the total number of shows.**
  - Get an overview of the total number of shows in the Netflix dataset.
- **Explore the distribution by release year.**
  - Understand how shows are distributed across different release years.
- **Visualize the last 10 years' number of shows.**
  - Visualize the trend in the number of shows released over the last 10 years.
- **Analyze genres distribution, top directors, and top cast members.**
  - Gain insights into the distribution of genres, identify the top directors, and explore the top cast members in the dataset.

## Customization

The application allows for easy customization, including theming and background color changes. Modify the `app.py` file and helper functions in `helper.py` to suit your preferences.

## Dataset

The Netflix dataset used in this project is stored in a CSV file named "Netflix-Changed.csv". Ensure you have this dataset in the correct location before running the application.

Feel free to explore, contribute, and adapt the code for your own projects!

## APP Link -
https://netflixdatavisulization.streamlit.app/
