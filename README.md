# m1-datascience-project

by 
- Alexandre ASSMUS
- Abigail BERTHE-PARDO
- Marina MUSSE

for the **Data Science** course in the **M1 TAL** at the IDMC.

Available in [Github](https://github.com/marinmss/m1-datascience-project)

## Code

You can run each of the six notebook files separately. These scripts are in the "src" folder, and are commented.

- 'part1_data_collection.ipynb'
- 'part1_data_analysis.ipynb'
- 'part1_clustering.ipynb'
- 'part2_named_entity_recognition.ipynb'
- 'part2_NER_analysis_by_entity_type.ipynb'

In the folder "Biographies", you can find the two sub-folders "Biographies_Journalists" and "Biographies_Sculptors" containing the biographies we retrieved. It is the same structure for "Biographies_double_data" and "Biographies_triple_data" that we use for extending the data for the clustering part.

# Setup 

Download the folder where this 'README;md' is and install the required packages:

```
pip install -r requirements.txt
```

# Usage

We set up the number_people < 130 in the collectBiographiesFromCategories() function of 'part1_data_collection.ipynb', it is our base case. You can modify it if you want to explore the effect of increasing data size in the clustering part.

## Quick Test (~ 10 min)

If you explore each notebook file in order without modifying the setting values, the execution will take you around 10min.

## Outputs 

Running 'part1_data_collection.ipynb' will create the "Biographie" folder, the subfolders and the .txt files as described above and save the dataframe created as a .csv file that we use in 'data_analysis.ipynb'. The other notebook files will just have the expected outputs according to the instructions of each part of the project.

## Results 

We will explain the results in the presentation.


