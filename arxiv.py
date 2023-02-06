import requests
import feedparser

def search_arxiv(query):
    url = "http://export.arxiv.org/api/query?search_query=" + query + "&start=0&max_results=10&sortBy=relevance&sortOrder=descending"
    response = requests.get(url)
    feed = feedparser.parse(response.text)

    for i in range(n):
        article = feed.entries[i]
        print("Title:", article.title)
        pdf_url = article.links[1]['href']
        print("PDF URL:", pdf_url)

        response = requests.get(pdf_url)
        file_name = article.title + ".pdf"
        open(file_name, "wb").write(response.content)
        print("PDF saved to disk as", file_name)

n=int(input())
search_arxiv(input())
