import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language="en",
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="rag-knowledgebase/1.0 "
)

def load_wikipedia_pages(titles):
    documents = []

    for title in titles:
        page = wiki.page(title)

        if page.exists():
            documents.append({
                "title": title,
                "text": page.text
            })

    return documents
