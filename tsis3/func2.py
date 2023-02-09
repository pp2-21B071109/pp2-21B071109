  # Dictionary of movies

movies = [
{
"name": "Usual Suspetcs", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1)Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def good(movies ,movie_name):
    curr_movie = dict(())
    for movie in movies:
        if movie["name"] == movie_name:
            curr_movie = movie
    return curr_movie["imdb"] > 5.5


print(good(movies, "Usual Suspetcs"))

#2)Write a function that returns a sublist of movies with an IMDB score above 5.5.
def list(movies):
    list_movies = []
    for i in movies:
        if i["imdb"] > 5.5:
            list_movies.append(i["name"])
    return list_movies

print(list(movies))
#3) Write a function that takes a category name and returns just those movies under that category.
def kateg( movies, category):
    list = []
    for i in movies:
        if i['category'] == category:
            list.append(i)
    return list

print(kateg(movies, "Romance"))

#4)Write a function that takes a list of movies and computes the average IMDB score.

def average(movies):
    sum = 0
    num_movies = len(movies)
    for i in movies:
        sum += i["imdb"]
    result = sum/num_movies
    return result
print(average(movies))
#5) Write a function that takes a category and computes the average IMDB score.
def avg_kateg(movies, category):
    sum = 0
    num = 0
    for i in movies:
        if i['category'] == category:
            sum += i['imdb']
            num += 1
    return sum / num

print(avg_kateg(movies, 'Romance'))