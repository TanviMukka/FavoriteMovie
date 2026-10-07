import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Legally Blonde"

print("\nThe data for my favorite movie is:\n")
favMovieBooleanList = movieData["movie_title"] == favMovie

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)
print("\n\n")

comedyMovieBooleanList = movieData["genres"].str.contains("Comedy")
comedyMovieData = movieData.loc[comedyMovieBooleanList]
numOfMovies = comedyMovieData.shape[0]

print("We will be comparing " + favMovie + " to other movies under the genre Comedy in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Comedy.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie + " compares to other movies in this genre.\n")

min = comedyMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 72 points higher than the lowest rated movie.")
print()

max = comedyMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 28 points lower than the highest rated movie.")
print()

mean = comedyMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " higher than the mean movie rating.")
print()

median = comedyMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

plt.hist(comedyMovieData["audience_rating"], range = (0,100), bins = 20)

plt.grid(True)
plt.title("Audience Ratings of Comedy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Comedy Movies")

print("According to the histogram, over 450 movies are rated around 70 to 75.")
print("(Search the file explorer for 'histogram.png' in order to view the histogram)")
print()

plt.savefig("histogram.png")
input("Press enter to see the next data visualization.\n")
plt.close()

plt.scatter(data = comedyMovieData, x = "audience_rating", y = "critic_rating")

plt.grid(True)
plt.title("Audience Rating vs. Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating ")
plt.xlim(0, 100)
plt.ylim(0, 100)

print("According to the scatter plot, there is a positive correlation between audience ratings and critic ratings")
print("(Search the file explorer for 'scatterplot.png' in order to view the scatterplot)")
print()

plt.savefig("scatterplot.png")

print("\nThank you for reading through my data analysis!")