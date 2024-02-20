 <!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<h3 align="center">Machine Learning Movie Recommendation System</h3>

  <p align="center">
  </p>

<!-- ABOUT THE PROJECT -->
## About The Project

<p>The goal of this project is to utizlise machine learning to create a recommendation system for movies based on the features of the target movie. We will be evaluating different methods to achieve this outcome by comparing the method results with TMDB recommendation api. 

</p>

### Built With

* HTML
* JavaScript
* Python

## Creation of movie recommendation
Built a content based filtering movie recommendation system with the movie features but instead of using a user's like features,we will compare a target movie feature with other movie features to create a recommendation list. 

To do this, we turned the movie features into a Term Frequency Inverse Document Frequency (TFIDF) matrix, which we can then use to compute the consine similarity using Linearl Kernal from SK learn and hence determine movies that have similar features. 

We also looked into using Nearest Neighbors and KDtree from SK learn to fit the TFIDF matrix and compute the nearest neighbors to the target movie features. 

### Results of project 

#### Cosine Similarity 
##### Gerne 
Overall Accuracy at 10: 0.14
##### Plot
Overall Accuracy at 10: 0.17
##### Genre + Plot
Overall Accuracy at 10: 0.17

#### Nearest Neighbors 
##### Genre
Overall Accuracy at 10: 0.12
##### Plot
Overall Accuracy at 10: 0.17
##### Genre  + Plot 
Overall Accuracy at 10: 0.17
##### Genre + Plot + train/test
Overall Accuracy at 10: 0.05

#### KD TREE
##### Genre 
Overall Accuracy at 10: 0.1 

### Method of calculcating accuracy
By comparing the list of recommendation to what TMDB api recommends for the movie, we can calculate how accurate our models is. The list of movies in the recommendation that are in the API recommendation list would give us our Accuracy. 

For example: Toy story recommendation for cosine similarity for plot has only 2 movies recommended that are in the API recommendation for toy story, so it would have a score of 2/10 = 0.2.

We do this for 10 different movies for each method and take the average of the scores to calculate the overall Accuracy for the method. 


<!-- ROADMAP -->
## Roadmap

#### Part 1: Data selection & Data Cleaning
- [x] Selection of dataset [TMDB API](https://developer.themoviedb.org/docs/getting-started)

- [x] Create dataframe from TMDB API 

#### Part 2: Model creation
- [x] Create function to run the cosine similarity against features of the movie to compute 10 recommendations 
- [x] Create function to use Nearest Neighbors for recommendation
- [x] Create function to use KD tree for recommendation

#### Part 3: Model Precision and testing
- [x] Define Accuracy method to use for model
- [x] Calculate general Accuracy of model and its method.

#### Part 4: Create flask webpage 
- [x] Host the model onto flask server
- [x] Implement search bar
- [x] Display the recommendation


<!-- CONTACT -->
## Colaboraters

[Peter Tram](https://github.com/PeterTramm)

[Yared Haile](https://github.com/YaredHaile)

[Ekjyot](https://github.com/Ework1989)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
[TMDB API](https://developer.themoviedb.org/docs/getting-started)
[OMDB API](https://omdbapi.com/)


