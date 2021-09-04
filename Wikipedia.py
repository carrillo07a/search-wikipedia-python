import wikipedia

# Language fr, en
wikipedia.set_lang("es")

# Search title
search = wikipedia.search("python")
print("search: ", str(search))

# Search Page
page = wikipedia.page("New York City")
print("title: ", page.title)
print("URL: ", page.url)
print("Content: ", page.content)

# Summary Wikipedia
summary = wikipedia.summary("wikipedia", sentences=1)
print("summary: ", str(summary))
