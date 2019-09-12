# Beer_Choice

With so many different beers on the market, trying to choose a new beer to try seems to be based on a whimsical name and eye-catching label. But with our help, we can tell you what beers to tyr based on similar tastes of users like you.  

After entering one to three of your favorite beers, the app runs your choices through our model and returns a list of new beers to try.  

*Beer Recommender Refined - using Kmeans clustering unsupervised machine learning, Python, Javascript, D3, Plotly

Uses larger beer database of 60000+ beer names

Kmeans clustering model -  main beer styles by users' overall review

## Docs

- Python Flask app
- Python functions used in app
- template folder containing HTML files
- static folder containing Javascript files, CSS files, and images
- database folder containing sqlite file

## Deployment

Website: [http://beerlists.herokuapp.com/]  
Heroku deployment instructions found [here](https://github.com/lprymak/Beer_Choice) 

## Build

## Revisions from original
Homepage changes
- Change layout to a simpler, easier to read format
- Add links to data sites
- Change navbar and header

![Image of Method](https://github.com/lprymak/Beer_Choice/blob/master/static/Images/homepage.png)

List Page changes
- Change layout
- Static page with scrolling list
- List images changed to beer labels/brewery labels instead of beer images
- Keep chosen beers at top => "No Selection" if none chosen
- Add definition explanation popup

![Image of Method](https://github.com/lprymak/Beer_Choice/blob/master/static/Images/listpage.png)

Group Page changes
- Change layout
- Static page with scrolling
- Add mouseover event on treemap

![Image of Method](https://github.com/lprymak/Beer_Choice/blob/master/static/Images/grouppage.png)

Model Page changes
- Change layout
- Change text description
- Change images
- Add silhouette plot distributions

![Image of Method](https://github.com/lprymak/Beer_Choice/blob/master/static/Images/modelpage.png)
