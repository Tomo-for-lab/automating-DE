# Automating Data Extraction (DE)

## Overview
This repository leverages large language models (LLMs) for systematic review, enabling efficient information extraction. There are Jupyter notebooks to automate the data extraction (DE) process, develop metaprompts, and evaluate results. All notebooks are designed to run on Google Colaboratory. Below are the descriptions of each notebook and their functionalities.

## Notebooks

### 1. Create Original Description

This section contains notebooks for creating original descriptions for variables.
- `create_original_description.ipynb`: Generates original descriptions for each variable based on the DE manual.

### 2. Develop Metaprompt

This section includes notebooks for developing metaprompts using different methods.
- `development_of_metaprompt_with_chat_prompting.ipynb`: Develops metaprompt using the chat prompting method.
- `development_of_metaprompt_with_chat_prompting_modified.ipynb`: Develops metaprompt using the chat prompting method (modified version).
- `development_of_metaprompt_with_one_by_one_n_shots.ipynb`: Develops metaprompt using the one-by-one n-shot prompting method.
- `development_of_metaprompt_with_conventional_n_shots.ipynb`: Develops metaprompt using the cnventional n-shot prompting method.


### 3. Data Extraction

This section is dedicated to data extraction processes.
- `data_extraction.ipynb`: Extracts data for all variables at once (All-in-one data extraction).
- `data_extraction_modified.ipynb`: Extracts data using modified methods, including re-check and re-extract prompting, re-extract prompting and batch data extraction.

### 4. Evaluation

This section focuses on the evaluation of extracted data.
- `arm_matching.ipynb`: Matches names of arms extracted by GPT with those extracted by humans.
- `score_calculation.ipynb`: Calculates accuracy, sensitivity, and specificity.

## Citation
```
@misc{kataoka2024automating,
  author = {KATAOKA, Yuki},
  title = {Automating the Data Extraction Process for Systematic Reviews using GPT-4o},
  year = {2024},
  url = {https://osf.io/cqg8u},
  note = {Retrieved October 19, 2024}
}
```
