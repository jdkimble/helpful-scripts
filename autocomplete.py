from tkinter import *
from tkinter.scrolledtext import ScrolledText


# This script will use a data structure called a Trie (or tree)
# This structure is useful for autocomplete programs. It will show all possible routes to spell words.
# If a word is spelled wrong, nothing will display. e.g. if the user types "app", words such as apple will appear.
# If a user types "appz", nothing will appear. This trie works dynamically, so you can see results appear as you type.

class Trie:
    def __init__(self, is_word=False, links=None):
        self.is_word = is_word
        self.links = {} if links is None else links

    # this function finds words not already in the trie.
    def add(self, word):
        n = self
        for c in word:
            if c not in n.links:
                n.links[c] = Trie()
            n = n.links[c]
        n.is_word = True

    # the function below finds all words starting with the user input.
    def starting_with(self, prefix):
        n = self
        for c in prefix:
            if c not in n.links:
                return []
            n = n.links[c]
        return self.all_below(n, prefix)

    # the function below will find all words 'below' what is typed. e.g. if user types "zen",
    # the words zenith and zeniths will appear.
    def all_below(self, n, s):
        M = [s] if n.is_word else []
        if n.links == {}:
            return M
        for c in n.links:
            M.extend(self.all_below(n.links[c], s + c))
        return M


# uses Tkinter to create a popup-like widget to display the words.
root = Tk()
entry = Entry(font=('Veranda', 20), width=20)
entry.grid(row=0, column=0)
text = ScrolledText(height=35, width=30)
text.grid(row=1, column=0)


# the main function loops through txt file to add to the trie. Binds to Tkinter widget.
# with every keypress, send key to root (widget)
def main():
    n = Trie()
    with open("wordlist.txt") as file:
        for line in file:
            n.add(line.strip())
    root.bind('<Key>', lambda e: autocomplete(e, n))


# deletes and updates predicted words with every keypress.
def autocomplete(e, n):
    text.delete(1.0, END)
    text.update()
    e = entry.get()
    text.insert(END, n.starting_with(e))


main()
mainloop() #loops main
