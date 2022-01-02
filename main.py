from tkinter import *
from datetime import datetime
import operator
import webbrowser
import praw


class PostClassPRAW:
    """A custom class for each post."""

    def __init__(self, rawPost):
        self.title = rawPost.title
        self.author = rawPost.author.name
        self.score = rawPost.score
        self.ratio = rawPost.upvote_ratio
        self.comments = rawPost.num_comments
        self.date = datetime.fromtimestamp(rawPost.created_utc)
        self.isSelf = rawPost.is_self
        self.stickied = rawPost.stickied
        self.url = rawPost.url
        self.content = rawPost.selftext


POSTS_DATA = []


def returnListFromSub(sub, category, postLimit) -> list:
    result = []
    subreddit = reddit.subreddit(sub)
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
    POSTS_DATA.clear()
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
    root_window.title("SnooSearch")
    root_window.geometry('800x350')

    CATEGORY = StringVar()
    COUNT = IntVar()

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
    postListbox.config(yscrollcommand=postListScrollbar.set)

    """Binding double click of the listbox to a function."""
    postListbox.bind('<Double-1>', loadPostInfo)

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
    dropdownMenu["highlightthickness"] = 0
    dropdownMenu.grid(row=0, column=2, sticky='NW', padx=5, pady=8)

    postListbox.pack(expand=True, fill=Y)

    """Creating the dropdown menu to set the number of posts."""
    # entry_count = Entry(displaySubreddit, width=10)
    # entry_count.grid(row=0, column=3)

    counts = {5, 10, 25, 50}
    COUNT.set(5)
    dropdownMenu = OptionMenu(displaySubreddit, COUNT, *sorted(counts))
    dropdownMenu["highlightthickness"] = 0
    dropdownMenu.grid(row=0, column=3, sticky='NW', padx=5, pady=8)

    """Creating the load button to load the posts."""
    button_Posts = Button(displaySubreddit, text="Reload Posts",
                          command=lambda: loadDataPRAW(postListbox,
                                                       entry_subreddit.get(),
                                                       CATEGORY.get(),
                                                       COUNT.get()))
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
    button_FilterStickied = Button(displayInteraction, text="Hide Stickied",
                                   command=lambda: hideStickied(postListbox))
    button_FilterStickied.grid(row=4, column=0, sticky=W)
    button_FilterSpecial = Button(displayInteraction, text="Show Self Posts",
                                  command=lambda:
                                  filterForSelf(postListbox))
    button_FilterSpecial.grid(row=5, column=0, sticky=W)

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
    print(len(POSTS_DATA))


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


def hideStickied(listbox) -> NONE:
    """Search for posts that have been stickied."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if not postListing.stickied:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


def filterForSelf(listbox) -> NONE:
    """Search for posts that are self posts.."""
    listOfResults = []
    for postListing in POSTS_DATA:
        if postListing.isSelf:
            listOfResults.append(postListing)
    replaceList(listbox, listOfResults)


def loadPostInfo(event):
    listbox = event.widget
    selectionIndex = listbox.curselection()[0]
    selection = listbox.get(selectionIndex)
    for postListing in POSTS_DATA:
        if selection in postListing.title:
            postPopup(postListing)


def savePost(post):
    file = open("Saved Posts.txt", "a")
    file.write(post.title + "\n")
    file.write(post.url + "\n" + "\n")


def postPopup(post):
    popUp = Tk()
    popUp.wm_title(post.title)
    popUp.config(background='#24A0ED')
    popUp.geometry('680x700')

    """Creating the content Frame."""
    contentWindow = Frame(popUp, width=400, bg="#24A0ED")
    contentWindow.grid(row=1, column=0, padx=17, columnspan=1)

    label_popUp_content = Label(popUp, text="Post Text: ", bg='#24A0ED', fg='white')
    label_popUp_content.grid(row=0, column=0)

    "Creating the content window."
    content = post.content
    text_popUp_content = Text(contentWindow, height=20, width=100, font=("Arial Narrow", 10))
    text_popUp_content.insert(END, content)
    text_popUp_content.pack(side=LEFT)

    """Creating a scrollbar."""
    postListScrollbar = Scrollbar(contentWindow, orient="vertical")
    postListScrollbar.pack(side=RIGHT, fill=Y)
    postListScrollbar.config(command=text_popUp_content.yview)
    text_popUp_content.bind("<B1-Leave>", lambda event: "break")
    text_popUp_content.config(yscrollcommand=postListScrollbar.set)

    """Creating the Frame for the single Post info display."""
    displayPostInfo = Frame(popUp, width=400, bg="grey30")
    displayPostInfo.grid(row=2, column=0, sticky='NW', padx=17, pady=10)

    """Creating the post info displays."""
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
    label_postStickied = Label(displayPostInfo,
                               text="Stickied", bg="grey30", fg="white")
    label_postStickied.grid(row=6, column=0, sticky=W, padx=10)
    label_postUrl = Label(displayPostInfo,
                          text="URL", bg="grey30", fg="white")
    label_postUrl.grid(row=7, column=0, sticky=W, padx=10)

    labelBox_postTitle = Label(displayPostInfo, text=post.title,
                               anchor='w', width=78, bg="white")
    labelBox_postTitle.grid(row=0, column=1, sticky=W)
    labelBox_postAuthor = Label(displayPostInfo, text=post.author,
                                anchor='w', width=78, bg="white")
    labelBox_postAuthor.grid(row=1, column=1, sticky=W)
    labelBox_postScore = Label(displayPostInfo, text=post.score,
                               anchor='w', width=78, bg="white")
    labelBox_postScore.grid(row=2, column=1, sticky=W)
    labelBox_postRatio = Label(displayPostInfo, text=post.ratio,
                               anchor='w', width=78, bg="white")
    labelBox_postRatio.grid(row=3, column=1, sticky=W)
    labelBox_postComments = Label(displayPostInfo, text=post.comments,
                                  anchor='w', width=78, bg="white")
    labelBox_postComments.grid(row=4, column=1, sticky=W)
    labelBox_postDate = Label(displayPostInfo, text=post.date,
                              anchor='w', width=78, bg="white")
    labelBox_postDate.grid(row=5, column=1, sticky=W)
    labelBox_postStickied = Label(displayPostInfo, text=post.stickied,
                                  anchor='w', width=78, bg="white")
    labelBox_postStickied.grid(row=6, column=1, sticky=W)
    labelBox_postUrl = Label(displayPostInfo, text=post.url,
                             anchor='w', width=78, bg="white")
    labelBox_postUrl.grid(row=7, column=1, sticky=W)

    """Creating the url button."""
    button_URL = Button(popUp, text="Go to post", width=50,
                        command=lambda: webbrowser.open(post.url))
    button_URL.grid(row=3, column=0, pady=5, padx=100)

    """Creating the save post button."""
    button_URL = Button(popUp, text="Save post", width=50,
                        command=lambda: savePost(post))
    button_URL.grid(row=4, column=0, pady=5, padx=100)

    popUp.mainloop()


if __name__ == '__main__':
    show_gui()
