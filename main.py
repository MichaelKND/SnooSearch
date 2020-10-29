from tkinter import *
import csv
import operator
import webbrowser


class LetterError(Exception):
    """Exception to catch letters as invalid input."""
    pass


class greaterNumberInputError(Exception):
    """Exception to catch invalid numbers as input."""
    pass


class PostClass:
    """A custom class for each post."""

    def __init__(self, title, author, score,
                 ratio, comments, date, edited, url):
        self.title = title
        self.author = author
        self.score = score
        self.ratio = ratio
        self.comments = comments
        self.date = date
        self.edited = edited
        self.url = url


POSTS_DATA = []
postsList = []


def replaceList(listbox, popList):
    listbox.delete(0, END)
    for num, post in enumerate(popList):
        listbox.insert(num, post.title)


def loadData():
    with open('dataset.csv') as dataset:
        readCSV = csv.reader(dataset, delimiter=',')
        header = next(readCSV)
        if header is not None:
            for row in readCSV:
                POSTS_DATA.append(PostClass(row[0], row[1], row[2],
                                            row[3], row[4], row[5],
                                            row[6], row[7]))
        dataset.close()


def show_gui():
    """Create the main window."""
    root_window = Tk()
    root_window.config(background='grey30')
    root_window.title("Subreddit Parser")
    root_window.geometry('1050x470')

    POST_TITLE = StringVar()
    POST_AUTHOR = StringVar()
    POST_SCORE = StringVar()
    POST_RATIO = StringVar()
    POST_COMMENTS = StringVar()
    POST_DATE = StringVar()
    POST_EDITED = StringVar()
    POST_URL = StringVar()

    """Create the window that shows the list of posts."""
    label_listPosts = Label(root_window, text="Posts",
                            bg="grey30", fg="grey80", font={"Garamond", 34, })
    label_listPosts.grid(row=0, column=0)

    "Creating the Frame that contains the Listbox of the display."
    postListFrame = Canvas(root_window)
    postListFrame.grid(row=1, column=0, sticky=NW + SW, rowspan=3)

    """Creating a scrollbar."""
    postListScrollbar = Scrollbar(postListFrame, orient="vertical")
    postListScrollbar.pack(side=RIGHT, fill=Y)

    "Creating the listbox for the displays."
    postListbox = Listbox(postListFrame, width=80, bg="white",
                          yscrollcommand=postListScrollbar.set,
                          font=("Garamond", 12))

    for num, post in enumerate(postsList):
        postListbox.insert(num, post.title)

    postListScrollbar.config(command=postListbox.yview)

    postListbox.bind("<B1-Leave>", lambda event: "break")

    """Creating the load button to load the CSV."""
    button_Posts = Button(root_window, text="Load Posts",
                          command=lambda: replaceList(postListbox,
                                                      POSTS_DATA))
    button_Posts.grid(row=4, column=0, sticky=W, pady=5, padx=5)
    button_SinglePost = Button(root_window,
                               text="View Post Information", width=50,
                               command=lambda: loadPostInfo(postListbox, POST_TITLE,
                                                            POST_AUTHOR, POST_SCORE,
                                                            POST_RATIO, POST_COMMENTS,
                                                            POST_DATE, POST_EDITED,
                                                            POST_URL))
    button_SinglePost.grid(row=4, column=0, sticky=W, pady=5, padx=100)

    button_URL = Button(root_window, text="Go to post", width=50,
                        command=lambda: openURL(POST_URL.get()))
    button_URL.grid(row=8, column=0, sticky=W, pady=5, padx=100)

    postListbox.pack(expand=True, fill=Y)

    """Creating the Frame for the single Post info display."""
    displayPostInfo = Frame(width=400, bg="grey30")
    displayPostInfo.grid(row=7, column=0, sticky='NW', padx=5, columnspan=1)

    label_postTitle = Label(displayPostInfo,
                            text="Title", bg="grey30", fg="white")
    label_postTitle.grid(row=0, column=0, sticky=W, padx=10)
    label_postAuthor = Label(displayPostInfo,
                             text="Author", bg="grey30", fg="white")
    label_postAuthor.grid(row=1, column=0, sticky=W, padx=10)
    label_postScore = Label(displayPostInfo,
                            text="Score", bg="grey30", fg="white")
    label_postScore.grid(row=2, column=0, sticky=W, padx=10)
    label_postRatio = Label(displayPostInfo,
                            text="Upvote Ratio", bg="grey30", fg="white")
    label_postRatio.grid(row=3, column=0, sticky=W, padx=10)
    label_postComments = Label(displayPostInfo,
                               text="Comments", bg="grey30", fg="white")
    label_postComments.grid(row=4, column=0, sticky=W, padx=10)
    label_postDate = Label(displayPostInfo,
                           text="Date", bg="grey30", fg="white")
    label_postDate.grid(row=5, column=0, sticky=W, padx=10)
    label_postEdited = Label(displayPostInfo,
                             text="Edited", bg="grey30", fg="white")
    label_postEdited.grid(row=6, column=0, sticky=W, padx=10)
    label_postUrl = Label(displayPostInfo,
                          text="URL", bg="grey30", fg="white")
    label_postUrl.grid(row=7, column=0, sticky=W, padx=10)

    labelBox_postTitle = Label(displayPostInfo, textvariable=POST_TITLE,
                               anchor='w', width=78, bg="white")
    labelBox_postTitle.grid(row=0, column=1, sticky=W)
    labelBox_postAuthor = Label(displayPostInfo, textvariable=POST_AUTHOR,
                                anchor='w', width=78, bg="white")
    labelBox_postAuthor.grid(row=1, column=1, sticky=W)
    labelBox_postScore = Label(displayPostInfo, textvariable=POST_SCORE,
                               anchor='w', width=78, bg="white")
    labelBox_postScore.grid(row=2, column=1, sticky=W)
    labelBox_postRatio = Label(displayPostInfo, textvariable=POST_RATIO,
                               anchor='w', width=78, bg="white")
    labelBox_postRatio.grid(row=3, column=1, sticky=W)
    labelBox_postComments = Label(displayPostInfo, textvariable=POST_COMMENTS,
                                  anchor='w', width=78, bg="white")
    labelBox_postComments.grid(row=4, column=1, sticky=W)
    labelBox_postDate = Label(displayPostInfo, textvariable=POST_DATE,
                              anchor='w', width=78, bg="white")
    labelBox_postDate.grid(row=5, column=1, sticky=W)
    labelBox_postEdited = Label(displayPostInfo, textvariable=POST_EDITED,
                                anchor='w', width=78, bg="white")
    labelBox_postEdited.grid(row=6, column=1, sticky=W)
    labelBox_postUrl = Label(displayPostInfo, textvariable=POST_URL,
                             anchor='w', width=78, bg="white")
    labelBox_postUrl.grid(row=7, column=1, sticky=W)

    """Creating the Frame for the sort/filter buttons."""
    displayInteraction = Frame(root_window, bg='grey30', width=600)
    displayInteraction.grid(row=2, column=1, sticky='NW', padx=5, pady=10)

    button_sortByTitle = Button(displayInteraction, text="Sort By Title",
                                command=lambda: sortByTitle(postListbox))
    button_sortByTitle.grid(row=0, column=0, sticky=W, padx=4, )
    button_sortByRatio = Button(displayInteraction, text="Sort By Ratio",
                                command=lambda: sortByRatio(postListbox))
    button_sortByRatio.grid(row=0, column=1, sticky=W, padx=4)
    button_sortByScore = Button(displayInteraction, text="Sort By Score",
                                command=lambda: sortByScore(postListbox))
    button_sortByScore.grid(row=0, column=2, sticky=W, padx=4)
    button_sortByAuthor = Button(displayInteraction, text="Sort By Author",
                                 command=lambda: sortByAuthor(postListbox))
    button_sortByAuthor.grid(row=0, column=3, sticky=W, padx=4)
    button_FilterEdited = Button(displayInteraction, text="Filter Edited",
                                 command=lambda: filterForEdited(postListbox))
    button_FilterEdited.grid(row=1, column=0, pady=5, columnspan=2)
    button_FilterUnedited = Button(displayInteraction, text="Filter Unedited",
                                   command=lambda: filterForUnedited(postListbox))
    button_FilterUnedited.grid(row=1, column=2, pady=5, columnspan=2)

    """Creating the Frame for the search buttons and entry buttons."""
    displaySearchFrame = Frame(root_window, bg='grey30', width=600)
    displaySearchFrame.grid(row=3, column=1, sticky='NW', padx=5)

    entry_searchByTitle = Entry(displaySearchFrame, width=40)
    entry_searchByTitle.grid(row=0, column=1, sticky=E, padx=5)
    entry_searchByAuthor = Entry(displaySearchFrame, width=40)
    entry_searchByAuthor.grid(row=1, column=1, sticky=E, pady=5, padx=5)

    button_SearchByTitle = Button(displaySearchFrame, text="Search For Title",
                                  command=lambda: searchForTitle(entry_searchByTitle, postListbox))
    button_SearchByTitle.grid(row=0, column=0, sticky=W)
    button_SearchByAuthor = Button(displaySearchFrame, text="Search For Author",
                                   command=lambda: searchForAuthor(entry_searchByAuthor, postListbox))
    button_SearchByAuthor.grid(row=1, column=0, sticky=W, pady=5)

    root_window.mainloop()


def searchForTitle(entryBox, listbox):
    titleQuery = entryBox.get()
    resultsList = []
    for postListing in POSTS_DATA:
        if titleQuery in postListing.title:
            resultsList.append(postListing)
    replaceList(listbox, resultsList)


def searchForAuthor(entryBox, listbox):
    titleQuery = entryBox.get()
    resultsList = []
    for postListing in POSTS_DATA:
        if titleQuery in postListing.author:
            resultsList.append(postListing)
    replaceList(listbox, resultsList)


def loadPostInfo(postListbox, title, author, score, ratio, comments, date, edited, url):
    curSelection = postListbox.curselection()
    curTitle = (postListbox.get(curSelection[0]))
    for post in POSTS_DATA:
        if post.title == curTitle:
            foundPost = PostClass(post.title, post.author, post.score, post.ratio, post.comments, post.date,
                                  post.edited, post.url)
    title.set(foundPost.title)
    author.set(foundPost.author)
    score.set(foundPost.score)
    ratio.set(foundPost.ratio)
    comments.set(foundPost.comments)
    date.set(foundPost.date)
    edited.set(foundPost.edited)
    url.set(foundPost.url)


def openURL(url):
    webbrowser.open(url)


def sortByTitle(listbox):
    """Sort the posts by alphabetical order of titles."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('title'))
    replaceList(listbox, sortedList)


def sortByRatio(listbox):
    """Sort the posts by numerical value of upvote ratio."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('ratio'))
    replaceList(listbox, sortedList)


def sortByScore(listbox):
    """Sort the posts by numerical value of score."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('score'))
    replaceList(listbox, sortedList)


def sortByAuthor(listbox):
    """Sort the posts by alphabetical order of post authors."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('author'))
    replaceList(listbox, sortedList)


def filterForEdited(listbox):
    """Search for posts that have been edited."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if 'False' != postListing.edited:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


def filterForUnedited(listbox):
    """Search for posts that have been edited."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if 'False' == postListing.edited:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


if __name__ == '__main__':
    loadData()
    show_gui()
