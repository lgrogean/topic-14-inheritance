# Topic 14 Collaborative Assignment
# Your Name: Lauren Grogean
# Date: 7/27/26

# --- PROVIDED CODE: Do not modify this section ---

class LibraryItem:
    """Base class for all items in the library catalog."""
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        return f"{self.title} ({self.year})"

    def item_type(self):
        return "Library Item"


class Book(LibraryItem):
    """A book in the library catalog."""
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"

    def item_type(self):
        return "Book"


def count_items(catalog, index=0):
    """Recursively count items in a catalog list."""
    if index == len(catalog):
        return 0
    return 1 + count_items(catalog, index + 1)


# --- Sample usage of provided code ---
book1 = Book("The Pragmatic Programmer", 1999, "Hunt & Thomas")
print(book1.describe())
print("Type:", book1.item_type())

catalog = [book1]
print("Items in catalog:", count_items(catalog))

# --- YOUR CODE BELOW THIS LINE ---
# Add at least one new subclass (e.g., Magazine, DVD, Audiobook, Journal)
# Override describe() and item_type() in your subclass
# Create instances of your new subclass and add them to the catalog
# Call count_items(catalog) again to show the updated count

class Audiobook(LibraryItem):
  """An audiobook in the library catalog."""
  def __init__(self, title, year, narrator):
    super().__init__(title, year)
    self.narrator = narrator
    
  def describe(self):
    return f"{self.title}, narrated by {self.narrator} ({self.year})"
    
  def item_type(self):
    return "Audiobook"

# Create Audiobook
audiobook1 = Audiobook("Throne of Glass", 2012, "Erika Evans")

# Add it to the catalog
catalog.append(audiobook1)

# Polymorphism
print("\nLibrary Catalog:")
for item in catalog:
  print(item.describe())
  print("Type:", item.item_type())

# Show recursive count
print("\nItems in catalog:", count_items(catalog))

