# Code of Automating Data Extraction (DE)

## Overview
This repository leverages large language models (LLMs) for systematic review, enabling efficient information extraction. There are Jupyter notebooks to automate the data extraction (DE) process, develop metaprompts, and evaluate results. All notebooks are designed to run on Google Colaboratory. Below are the descriptions of each notebook and their functionalities.

## Notebooks

### 1. Create Original Description

This section contains notebooks for creating original descriptions for variables.
- `create_original_description.ipynb`: Generates original descriptions for each variable based on the DE manual.

### 2. Development of Metaprompt

This section includes notebooks for developing metaprompts using different methods.
- `development_of_metaprompt_with_chat_prompting.ipynb`: Develops metaprompt using the chat prompting method.
- `development_of_metaprompt_with_prompting.ipynb`: Develops metaprompt using an alternative prompting method.

### 3. Data Extraction

This section is dedicated to data extraction processes.
- `data_extraction.ipynb`: Extracts data for all variables at once (All-in-one data extraction).
- `data_extraction_modified.ipynb`: Extracts data using modified methods, including re-check and re-extract prompting, as well as batch data extraction.

### 4. Evaluation

This section focuses on the evaluation of extracted data.
- `arm_matching.ipynb`: Matches names of arms extracted by GPT with those extracted by humans.
- `score_calculation.ipynb`: Calculates accuracy, sensitivity, and specificity.

## Citation
Coming soon
