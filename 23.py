import feedparser
import webbrowser
import os


def parse_scipost_rss():
    url = "https://scipost.org/atom/publications/comp-ai"
    feed = feedparser.parse ( url )

    news_list = []

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        summary = entry.content[
            0].value if 'content' in entry else entry.summary if 'summary' in entry else "No content available."

        news_list.append ( {
            "title": title ,
            "link": link ,
            "summary": summary
        } )

    return news_list


def generate_html(news):
    html_content = """
    <html>
    <head><title>SciPost News</title></head>
    <body>
        <h1>Latest SciPost AI News</h1>
        <ul>
    """
    for item in news:
        html_content += f"<li><a href='{item['link']}'><strong>{item['title']}</strong></a><br>{item['summary']}</li><br>"

    html_content += """
        </ul>
    </body>
    </html>
    """

    file_path = "news.html"
    with open ( file_path , "w" , encoding="utf-8" ) as f:
        f.write ( html_content )

    print ( "HTML файл з новинами збережено як news.html" )
    webbrowser.open ( "file://" + os.path.abspath ( file_path ) )


if __name__ == "__main__":
    news = parse_scipost_rss ()
    if news:
        generate_html ( news )
