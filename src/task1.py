import pandas as pd
import wikipediaapi

### DATA COLLECTION ##########################################################################

def fetchBiographies():
    wiki = wikipediaapi.Wikipedia('en')

    data = []

    sculptors = wiki.page("Category:sculptors")
    articles = sculptors.categorymembers

    for title, page in articles.items():
            if page.ns == 0: 
                text = page.text
                data.append({'text': text, 'category': "Sculptors"})

    df = pd.DataFrame(data)
    return df


### DATA ANALYSIS ############################################################################


### CLUSTERING ###############################################################################


### MAIN #####################################################################################

def main():
    fetchBiographies()


if __name__=='__main__':
    main()