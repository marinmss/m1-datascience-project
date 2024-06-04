import pandas as pd
import wikipediaapi
import os
from SPARQLWrapper import SPARQLWrapper, JSON
import json


### DATA COLLECTION ##########################################################################

def fetchBiographies(categorymembers, category, data, number_people, level=0, max_level=1): 
        """Iterate through each page in the category members to fetch the biographies"""

        for page in categorymembers.values():
            if page.ns == 0 and 'List' not in page.title and number_people < 130: #limit the number of people for each category to 130
    
                #some wikipedia page cannot be found in dbpedia, we ignore them
                try: 

                    #knowledge graph of facts
                    kg_graph = fetchFacts(page.pageid, page.title)
                    # Save the graph of facts to a JSON file
                    with open('knowledge_graph.json', 'a') as json_file:
                        json.dump(kg_graph, json_file, indent=4)
                    print(f"{category} {page.title} processed")


                    text = page.text
                    data.append({'text': text, 'category': category})
                    #creation of txt file for the biography
                    f = open(f"Biographies_{category}/{(page.title).replace(' ', '')}_{category}.txt", "w")
                    f.write(text)
                    f.close()

                    #keep track of people processed
                    number_people += 1  

                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}, could not process {page.title}")
                    continue


            if page.ns == wikipediaapi.Namespace.CATEGORY and level < max_level and number_people < 130:
                # Recursively call the function to process pages in the subcategory 
                number_people = fetchBiographies(page.categorymembers, category, data, number_people, level=level + 1, max_level=max_level)
        # return updated count of processed people
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

def fetchFacts(wiki_id, page_title):
    """returns triples of facts about the wikipedia page"""

    #initialize the SPARQL wrapper
    sparql = SPARQLWrapper("http://dbpedia.org/sparql/")

    #first query to retrieve the dbpedia page of the person
    sparql.setQuery(f"""
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbp: <http://dbpedia.org/property/>

            SELECT *
            WHERE {{
                    ?person dbo:wikiPageID {wiki_id} .
            }}
    """)
    #?person foaf:isPrimaryTopicOf <{wiki_url}> .
    
    sparql.setReturnFormat(JSON)
    result_link = sparql.query().convert()

    person_wikidata_page = result_link["results"]["bindings"][0]["person"]["value"] #the first value is most likely what we are looking for
    #print(person_wiki_page)
    
    #second query to fetch all information as RDF triples
    sparql.setQuery(f"""
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbp: <http://dbpedia.org/property/>

            DESCRIBE <{person_wikidata_page}>
    """)
    sparql.setReturnFormat(JSON)
    results_facts = sparql.query().convert()
    results_facts['head']['person'] = page_title.replace(" ", "")
    
    return(results_facts)





### DATA ANALYSIS ############################################################################


### CLUSTERING ###############################################################################


### MAIN #####################################################################################

def main():
    print(formatData())


if __name__=='__main__':
    main()