#Mini Project: Movie Analyzer System

class MovieAnalyzer:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating

    def good_or_bad(self):
        if self.rating>=7:
            return "Good"
        else:
            return "Bad"
        
    def information(self):
        return self.name,self.rating
    
def read_file(file_name):
    movies=[]

    try:
        with open(file_name,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()

                if line=="":
                    continue

                try:
                    pieces=line.split(",")
                    names=pieces[0]
                    ratings=int(pieces[1])
                    movie=MovieAnalyzer(names,ratings)

                    movies.append(movie)

                except ValueError:
                    print("Rating must be a number.")

    except FileNotFoundError:
        print("The file is empty.")

    finally:
        print("The program ran.")

    return movies

def analyze(movies):
    if len(movies) == 0:
        print("There is no movie to analyze.")
        return
    
    total=0
    the_highest_rating=movies[0]
    the_lowest_rating=movies[0]
    good_movies=[]
    bad_movies=[]

    for f in movies:
        total+=1 

        if f.rating>the_highest_rating.rating:
            the_highest_rating=f

        if f.rating<the_lowest_rating.rating:
            the_lowest_rating=f

        if f.good_or_bad()=="Good":
            good_movies.append(f.name)
        else:
            bad_movies.append(f.name)

    print("Total number of movies:", total)
    print("The highest rated movie:",the_highest_rating)
    print("The lowest rated movie:", the_lowest_rating)
    print("Good movies:", good_movies)
    print("Bad movies:", bad_movies)

movies=read_file("movies.txt")

for f in movies:
    print(f.information(),f.good_or_bad())

analyze(movies)