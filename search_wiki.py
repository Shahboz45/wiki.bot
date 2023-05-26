import wikipediaapi

def get_wiki_page(text: str):
    # en - English, ru - Rus, fr - Farnsuzlar
    wiki = wikipediaapi.Wikipedia('eng')
    
    result = wiki.page(text)

    return result.summary