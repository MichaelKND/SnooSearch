# SnooSearch: A Reddit Parser
Obtains subreddit information and allows for basic parsing.
________________________________________
# User Guide

# What is Reddit?

Reddit is an online forum comprised of subforums, called subreddits. Each subreddit is dedicated to a particular subject, ranging from general topics such as world news, science, or technology to more niche subjects such as subreddits dedicated to a particular college or programming language. Posts to each subreddit are voted on by users and tagged with metadata. Reddit’s algorithm then uses those votes, alongside metadata such as the date, to keep the subreddit filled with relevant and topical posts.

# Requirements

SnooSearch requires PRAW, which is a Python-based API wrapper for Reddit's API. It can be installed via pip:

pip install praw
pip install --upgrade praw (to update to the latest version)

# What is SnooSearch?

SnooSearch is a program that takes in information about posts from a particular subreddit and displays information about each post. Metadata includes:

    - Post title
    - Post author
    - Post date
    - Post vote ratio
    - Number of comments on the post
    - Post score
    - If the post was edited or not
    - URL directly to the post.
    - ADDED : Content of the post.

# What is “the data”?

The previous version of the program pulled data from a collection of 50 posts. The program now is able to access Reddit's API directly, and thus "the data" is Reddit itself. Be aware that this data can change freely as the hour changes, so time is important when referencing this data.

# What requirements are needed?

SnooSearch was built on Python version 3.8.2 and is confirmed to work for that version. Older versions may not be compatible. Otherwise, SnooSearch uses entirely built in Python libraries and does not currently require pre-installed libraries.

# How does it work?

SnooSearch uses a preset Reddit account to access the API and display information to the user.
    - Entering a subredidt name (text after /r/ in the subreddit URL), and clicking "Reload Posts" will populate the main window listbox with a list of posts.
    - The number of posts and category of posts to show can be changed via a dropdown menu.
    - This list can be sorted, filtered, and searched by using the sidebar buttons/entryboxes.
    - Posts in the listbox can be double clicked to open a popup menu.
        - This pop menu displays the post content (if the post is not just a URL or image) and the post metadata.
        - This popup menu also includes a button to go directly to the post in the user's browser.
  

# Version History

## 1.0 – Initial Release
    - Current Features:
    - List posts in dedicated display window
    - Load post information based on selected post.
    - Sort by title, ratio, score, and author name.
    - Filter for edited and unedited posts
    - Open a browser window with the loaded post’s URL.
   
## 2.0 - 
    - Modified the program to pull from Reddit's API directly instead of having to use a program.
    - Changed the UI to incorporate a popup window instead of two separate listboxes.
    - Made the background blue.
 
# Future Plans
    - Add a post saving functionality.

# Reference Materials
    - Lundh, Fredrik. “An Introduction to Tkinter (Work in Progress).” Effbot.Org, 2019, effbot.org/tkinterbook/.
    - “W3Schools Online Web Tutorials.” W3schools.Com, 2019, www.w3schools.com.
