import pandas as pd
import wikipediaapi
import os

### DATA COLLECTION ##########################################################################

def fetchBiographies(categorymembers, category, data, number_people, level=0, max_level=1): 
        # Iterate through each page in the category members to fetch the biographies
        for page in categorymembers.values():
            if page.ns == 0 and 'List' not in page.title and number_people < 130: #limit the number of people for each category to 130
                number_people += 1 
                text = page.text
                data.append({'text': text, 'category': category})
                #creation of txt file for the biography
                f = open(f"Biographies_{category}/{(page.title).replace(' ', '')}_{category}.txt", "w")
                f.write(text)
                f.close()
                print(f"{category} {page.title} processed")
            if page.ns == wikipediaapi.Namespace.CATEGORY and level < max_level and number_people < 130:
                # Recursively call the function to process pages in the subcategory 
                number_people = fetchBiographies(page.categorymembers, category, data, number_people, level=level + 1, max_level=max_level)
        # updated count of processed people
        return number_people


def formatData():
    wiki = wikipediaapi.Wikipedia('Mozilla/5.0', 'en')

    data = []
    
    sculptors = wiki.page("Category:Sculptors")
    if not os.path.exists('Biographies_Sculptors'):
        os.mkdir('Biographies_Sculptors') #creates a directory to store all sculptors' biographies
    fetchBiographies(sculptors.categorymembers, "Sculptors", data, 0)
    

    journalists = wiki.page("Category:Journalists")
    if not os.path.exists('Biographies_Journalists'):
        os.mkdir('Biographies_Journalists') #creates a directory to store all journalists' biographies
    fetchBiographies(journalists.categorymembers, "Journalists", data, 0)

    df = pd.DataFrame(data)
    return df



### DATA ANALYSIS ############################################################################


### CLUSTERING ###############################################################################


### MAIN #####################################################################################

def main():
    print(formatData())


if __name__=='__main__':
    main()