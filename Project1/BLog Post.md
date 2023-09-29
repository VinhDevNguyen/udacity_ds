# IMDB  
### Home Page
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/pageIMDB.png)
# Blog Post  
### Analyzing and exploring IMDB data files from 1960 - 2015 helped me answer the questions below.  
Analyzing and exploring IMDB data files from 1960 - 2015 helped me answer the questions below.  
Are you interested?  
1. Which genres are most popular from year to year?
2. What kinds of properties are associated with movies that have high revenues?  
3. Statistics from 1960 - 2015: How many movies reached IMDB:  
IMDB < 6.9  
6.9 < IMDB < 8  
IMDB > 8  
4. Does the IMDB index relate to revenue and popularity?  
Note, that this is a personal comment and opinion, so it may be right or wrong, you can believe it or not.  
For a general overview and easier understanding, I will provide charts along with my own comments.  
The data are analyzed and processed in the file **Investigate_a_Dataset.ipynb**  

**Q1. Which genres are most popular from year to year?**   
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/Question%201.png)

    * Popular movie genres over the years have been evenly distributed.  
    * Particularly from 2001 to 2003, the Adventure, Fantasy, and Action genres were the most popular.  
    * Particularly from 2004 to 2005, the Adventure, Fantasy, and Family genres were the most popular.  
    * From 1960 - 2013 the popularity of the genre was not high, until 2014-2015, the popularity increased, maybe the manufacturer has promoted           marketing to attract the audience.  
**Q2. What kinds of properties are associated with movies that have high revenues?**
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/Question%202.png)
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/Question%2022.png)

    * With the above data, it is very difficult to draw conclusions about which properties are associated with high-grossing movies.
    * Overall, high-grossing movies usually have high review scores, averaging > 6.9 IMDb.
    * Most of the genres are Adventure.
    * The actors in the movie are famous people.
    * There are high-grossing movies but after deducting the production fees, the revenue multiplier is not too high.
    * There is a special movie: The Karate Kid, Part II. Revenue multiplier: 1,018,619
3. Statistics from 1960 - 2015: How many movies reached IMDB:  
IMDB < 6.9  
6.9 < IMDB < 8  
IMDB > 8  
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/Question%203.png)

    * IMDB ratings are really strict when ratings < 6.9 account for 86% and ratings > 8 account for less than 1% on a 10-point scale.  
5. Does the IMDB index relate to revenue and popularity?  
![](https://github.com/tienductk4dhqb/Data-Scientist-Project-1/blob/main/Images/Question%204.png)

    * IMDB rating, revenue, and popularity are related to each other.
    * X-axis, in the IMDB 2-5 rating range, the color (sales) starts to darken and the height (popularity) is very low.
    * And in the IMDB rating range of 5 onwards, color (revenue) is darker, than height (popularity) begins to increase clearly.
    * But when looking at the IMDB rating range from 8 onwards, they are related but not dependent on each other.
    * It means: that a high IMDB rating does not mean required high popularity or high revenue.
    * Or high revenue,  required a high IMDB rating, and high popularity.  

### Thank you for taking the time to read my article, I hope it does not waste your time.
