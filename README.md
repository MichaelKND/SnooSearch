# SnooSearch
Obtains subreddit information and allows for basic parsing.

SnooSearch – A Reddit Parser
________________________________________
User Guide

•	What is Reddit?
Reddit is an online forum comprised of subforums, called subreddits. Each subreddit is dedicated to a particular subject, ranging from general topics such as world news, science, or technology to more niche subjects such as subreddits dedicated to a particular college or programming language. Posts to each subreddit are voted on by users and tagged with metadata. Reddit’s algorithm then uses those votes, alongside metadata such as the date, to keep the subreddit filled with relevant and topical posts.

•	What is SnooSearch?
SnooSearch is a program that takes in information about posts from a particular subreddit and displays information about each post. Metadata includes:

  o	Post title

  o	Post author

  o	Post date

  o	Post vote ratio

  o	Number of comments on the post

  o	Post score

  o	If the post was edited or not

  o	URL directly to the post.

•	What is “the data”?
For the purposes of this class, a subset of 50 posts were pulled as a dataset from the top posts of the subreddit /r/learnpython on September 30th, 2020. This allows for easier assert statements and a constant dataset. Information collected is comprised only of the above listed metadata, and all information is publicly available by visiting the /r/learnpython subreddit and sorting for the “top” posts.

•	What requirements are needed?
SnooSearch was built on Python version 3.8.2 and is confirmed to work for that version. Older versions may not be compatible. Otherwise, SnooSearch uses entirely built in Python libraries and does not currently require pre-installed libraries.

•	How does it work?
SnooSearch reads a .csv file that lists the metadata of the posts, manipulating and sorting it for easier readability as well as adding search functions.
o	Clicking the “Load Posts” Button will refresh the top left display box with the list of posts loaded from a “dataset.csv” file. Posts are initially listed in descending order as shown on the /r/learnpython subreddit “top” listing.
o	Selecting a post and clicking “View Post Information” will load the selected post’s metadata into the metadata display below. 
o	Selecting “Go to Post” while a post is loaded will open a browser window to the selected post on the subreddit /r/learnpython.
o	On the right, posts may be sorted and filtered in several ways.

  	Sort by Title sorts in descending alphanumeric order (0-9, A-Z).
  
  	Sort by Ratio sorts by ascending upvote ratio order.
  
  	Sort by Score sorts by ascending score order.
  
  	Sort by Author sorts by descending alphanumeric author order.
  
  	Filter Edited displays only posts that were edited by the author after initial posting.
  
  	Filter Unedited shows posts that were not edited after initial posting.
  
  	Entering a string into the topmost entry box and selecting the adjacent “Search For Title” button will search the posts whose title contains the string.
  
  	Likewise, entering a string in the lower entry box and selecting “Search For Author” will search for posts whose author’s name contains the entered string.
  

Version Update

•	1.0 – Initial Release

o	Current Features:

o	List posts in dedicated display window

o	Load post information based on selected post.

o	Sort by title, ratio, score, and author name.

o	Filter for edited and unedited posts.

o	Open a browser window with the loaded post’s URL.
 
Future Plans

•	Add a key column that shows the category of relevance when a user sorts or filters.

•	Add a error functionality when there is no post selected and the user tries to load post information.




Reference Materials

•	Lundh, Fredrik. “An Introduction to Tkinter (Work in Progress).” Effbot.Org, 2019, effbot.org/tkinterbook/.

•	“W3Schools Online Web Tutorials.” W3schools.Com, 2019, www.w3schools.com.
