from tkinter import *
import operator
import webbrowser
import praw

reddit = praw.Reddit(client_id='zSSSh_xVCB2CQg',
                     client_secret='zDlIP1ENlrX08Xlqu_l4FQgfujc',
                     password='orangecoast22',
                     user_agent='Python Test App',
                     username='cs131praw')


class PostClassPRAW:
    """A custom class for each post."""

    def __init__(self, rawPost):
        self.title = rawPost.title
        self.author = rawPost.author.name
        self.score = rawPost.score
        self.ratio = rawPost.upvote_ratio
        self.comments = rawPost.num_comments
        self.date = rawPost.created_utc
        self.edited = rawPost.edited
        self.url = rawPost.url


POSTS_DATA = []


def returnListFromSub(sub, category, postLimit) -> list:
    result = []
    subreddit = reddit.subreddit(sub)
    if category == "controversial":
        for subpost in subreddit.controversial(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    if category == "gilded":
        for subpost in subreddit.gilded(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    if category == "hot":
        for subpost in subreddit.hot(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    if category == "new":
        for subpost in subreddit.new(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    if category == "rising":
        for subpost in subreddit.rising(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    if category == "top":
        for subpost in subreddit.top(limit=postLimit):
            result.append(PostClassPRAW(subpost))
    return result


def replaceList(listbox, popList) -> NONE:
    """Clears the current listbox and replaces it."""
    listbox.delete(0, END)
    for num, post in enumerate(popList):
        listbox.insert(num, post.title)


def loadDataPRAW(listbox, sub, category, limit=20):
    listbox.delete(0, END)
    returnedList = returnListFromSub(sub, category, int(limit))
    for num, post in enumerate(returnedList):
        listbox.insert(num, post.title)
        POSTS_DATA.append(post)


def show_gui() -> NONE:
    """Main GUI window loop."""
    """Create the main window."""
    root_window = Tk()
    root_window.config(background='#24A0ED')
    root_window.title("Subreddit Parser")
    root_window.geometry('800x350')

    CATEGORY = StringVar()

    "Creating the Frame that contains the Listbox of the display."
    postListFrame = Canvas(root_window)
    postListFrame.grid(row=1, column=0, sticky=NW + SW, rowspan=3, padx=5)

    """Creating a scrollbar."""
    postListScrollbar = Scrollbar(postListFrame, orient="vertical")
    postListScrollbar.pack(side=RIGHT, fill=Y)

    "Creating the listbox for the displays."
    postListbox = Listbox(postListFrame, width=80, bg="white",
                          yscrollcommand=postListScrollbar.set,
                          font=("Garamond", 12))

    postListScrollbar.config(command=postListbox.yview)

    postListbox.bind("<B1-Leave>", lambda event: "break")

    """Creating the Frame for the subreddit bar.."""
    displaySubreddit = Frame(root_window, bg='#24A0ED', width=600)
    displaySubreddit.grid(row=0, column=0, sticky='NW', padx=5)

    """Creating the subreddit entry bar."""
    entry_subreddit = Entry(displaySubreddit, width=60)
    entry_subreddit.grid(row=0, column=1, sticky='NW', padx=5, pady=12)

    """Creating the post category dropdown menu."""
    categories = {'hot', 'top', 'new', 'rising'}
    CATEGORY.set('hot')
    dropdownMenu = OptionMenu(displaySubreddit, CATEGORY, *categories)
    dropdownMenu["highlightthickness"]=0
    dropdownMenu.grid(row=0, column=2, sticky='NW', padx=5, pady=8)

    postListbox.pack(expand=True, fill=Y)

    """Creating the entry box to set the number of posts."""
    entry_count = Entry(displaySubreddit, width=10)
    entry_count.grid(row=0, column=3)

    """Creating the load button to load the posts."""
    button_Posts = Button(displaySubreddit, text="Reload Posts",
                          command=lambda: loadDataPRAW(postListbox,
                                                       entry_subreddit.get(),
                                                       CATEGORY.get(),
                                                       entry_count.get()))
    button_Posts.grid(row=0, column=0, sticky=W, pady=5, padx=5)

    """Creating the Frame for the sort/filter buttons."""
    displayInteraction = Frame(root_window, bg='#24A0ED', width=600)
    displayInteraction.grid(row=1, column=1, sticky='NW', padx=5)

    button_sortByTitle = Button(displayInteraction, text="Sort By Title",
                                command=lambda: sortByTitle(postListbox))
    button_sortByTitle.grid(row=0, column=0, sticky=W)
    button_sortByRatio = Button(displayInteraction, text="Sort By Ratio",
                                command=lambda: sortByRatio(postListbox))
    button_sortByRatio.grid(row=1, column=0, sticky=W)
    button_sortByScore = Button(displayInteraction, text="Sort By Score",
                                command=lambda: sortByScore(postListbox))
    button_sortByScore.grid(row=2, column=0, sticky=W)
    button_sortByAuthor = Button(displayInteraction, text="Sort By Author",
                                 command=lambda: sortByAuthor(postListbox))
    button_sortByAuthor.grid(row=3, column=0, sticky=W)
    button_FilterEdited = Button(displayInteraction, text="Filter Edited",
                                 command=lambda: filterForEdited(postListbox))
    button_FilterEdited.grid(row=4, column=0, sticky=W)
    button_FilterUnedited = Button(displayInteraction, text="Filter Unedited",
                                   command=lambda:
                                   filterForUnedited(postListbox))
    button_FilterUnedited.grid(row=5, column=0, sticky=W)

    """Creating the Frame for the search buttons and entry buttons."""
    displaySearchFrame = Frame(root_window, bg='#24A0ED', width=600)
    displaySearchFrame.grid(row=3, column=1, sticky='NW', padx=5, pady=5)

    entry_searchByTitle = Entry(displaySearchFrame, width=15)
    entry_searchByTitle.grid(row=1, column=0, sticky=W, pady=5)
    entry_searchByAuthor = Entry(displaySearchFrame, width=15)
    entry_searchByAuthor.grid(row=3, column=0, sticky=W, pady=5)

    button_SearchByTitle = Button(displaySearchFrame, text="Search For Title",
                                  command=lambda:
                                  searchForTitle(entry_searchByTitle,
                                                 postListbox))
    button_SearchByTitle.grid(row=0, column=0, sticky=W, pady=1)
    button_SearchByAuthor = Button(displaySearchFrame,
                                   text="Search For Author",
                                   command=lambda:
                                   searchForAuthor(entry_searchByAuthor,
                                                   postListbox))
    button_SearchByAuthor.grid(row=2, column=0, sticky=W, pady=1)

    root_window.mainloop()


def showPost() -> NONE:
    print("Test")


def searchForTitle(entryBox, listbox) -> NONE:
    """Gets the entered title query, searches through the post data,
    and then replaces the listbox with matching posts."""
    if entryBox.get() != "":
        titleQuery = entryBox.get()
        resultsList = []
        for postListing in POSTS_DATA:
            if titleQuery in postListing.title:
                resultsList.append(postListing)
        replaceList(listbox, resultsList)


def searchForAuthor(entryBox, listbox) -> NONE:
    """Gets the entered author query, searches through the post data,
        and then replaces the listbox with matching posts."""
    titleQuery = entryBox.get()
    resultsList = []
    for postListing in POSTS_DATA:
        if titleQuery in postListing.author:
            resultsList.append(postListing)
    replaceList(listbox, resultsList)


def sortByTitle(listbox) -> NONE:
    """Sort the posts by alphabetical order of titles."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('title'))
    replaceList(listbox, sortedList)


def sortByRatio(listbox) -> NONE:
    """Sort the posts by numerical value of upvote ratio."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('ratio'))
    replaceList(listbox, sortedList)


def sortByScore(listbox) -> NONE:
    """Sort the posts by numerical value of score."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('score'))
    replaceList(listbox, sortedList)


def sortByAuthor(listbox) -> NONE:
    """Sort the posts by alphabetical order of post authors."""
    sortedList = sorted(POSTS_DATA, key=operator.attrgetter('author'))
    replaceList(listbox, sortedList)


def filterForEdited(listbox) -> NONE:
    """Search for posts that have been edited."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if 'False' != postListing.edited:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


def filterForUnedited(listbox) -> NONE:
    """Search for posts that have been edited."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if 'False' == postListing.edited:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


if __name__ == '__main__':
    show_gui()
