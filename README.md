# Automating Data Extraction (DE)

## Overview
This repository leverages large language models (LLMs) for systematic review, enabling efficient information extraction. There are Jupyter notebooks to automate the data extraction (DE) process, develop metaprompts, and evaluate results. All notebooks are designed to run on Google Colaboratory. Below are the descriptions of each notebook and their functionalities.

## Pre‑processing Pipeline (run **before** the notebooks)

| Source format    | Action                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| **.docx / .txt** | *No preprocessing required* – these files are consumed directly by the notebooks                    |
| **.pdf**         | Processed with the **Adobe PDF Extract API**  to split the file into main text, tables, and figures |

Adobe PDF Extract API: https://github.com/adobe/pdfservices-extract-python-sdk-samples

### Output directory layout

After processing, each study is placed in its own sub‑folder inside `IncludedTrials/`:

```text
IncludedTrials/
  Kataoka2024/
    figures/fileoutpartX.png   # Figures (PNG)
    tables/fileoutpartY.xlsx   # Tables  (Excel)
    structuredData.json        # Structured main text (JSON)
```

The notebooks assume this hierarchy when they load the source files.

## Notebooks

### 1. Create Original Description

This section contains notebooks for creating original descriptions for variables.
- `create_original_description.ipynb`: Generates original descriptions for each variable based on the DE manual.

The generated initial meta-prompt is [`here`](https://drive.google.com/drive/folders/1OELDlyaUvN1IHaYHQuPJCPZx8yrShY8M?usp=share_link)

### 2. Develop Metaprompt

This section includes notebooks for developing metaprompts using different methods.
- `development_of_metaprompt_with_chat_prompting.ipynb`: Develops metaprompt using the chat prompting method.
- `development_of_metaprompt_with_chat_prompting_modified.ipynb`: Develops metaprompt using the chat prompting method (modified version).
- `development_of_metaprompt_with_one_by_one_n_shots.ipynb`: Develops metaprompt using the one-by-one n-shot prompting method.
- `development_of_metaprompt_with_conventional_n_shots.ipynb`: Develops metaprompt using the cnventional n-shot prompting method.

#### 🔗 Links to generated metaprompts

| Method                    | Directory                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| Contextual Chat prompting | [`2_contextual_chat_prompting`](https://drive.google.com/drive/folders/1M-5uZXmPAwtABHrV4J5uEoa8Q4WcO35g?usp=share_link)                   |
| Contextual Chat prompting (modified) | [`2_contextual_chat_prompting_modified`](https://drive.google.com/drive/folders/13huXupRN6SM3beaMYvPyLHDEFdGlL23I?usp=share_link) |
| One‑by‑one n‑shots        | [`2_one_by_one_n_shots`](https://drive.google.com/drive/folders/1qFS1SbWYRgVTcpopHKXYcLLORzX05JeZ?usp=share_link)           |
| Conventional n‑shots      | [`2_conventional_n_shots`](https://drive.google.com/drive/folders/1TqajIv0HWgmOMHaO25DwKXJA-OXJHrz4?usp=share_link)       |


### 3. Data Extraction

This section is dedicated to data extraction processes.
- `data_extraction.ipynb`: Extracts data for all variables at once (All-in-one data extraction).
- `data_extraction_modified.ipynb`: Extracts data using modified methods, including re-check and re-extract prompting, re-extract prompting and batch data extraction.
- `data_extraction_additional_o3.py`: Extracts data using o3-high–based methods.

The extracted data is stored [`here`](https://drive.google.com/drive/folders/1K7ROs1h3PLrgOAUd2iYbYcCyifOIzi5o?usp=share_link)

### 4. Evaluation

This section focuses on the evaluation of extracted data.
- `arm_matching.ipynb`: Matches names of arms extracted by GPT with those extracted by humans.
- `value_checker.ipynb`: Check whether the value extracted by human matches the value extracted by GPT.
- `metric_calculation_with_precision.ipynb`: Calculates accuracy, sensitivity, specificity and precision.
- `metric_calculation_with_variable_detection_comprehensiveness.ipynb`: Calculates accuracy, sensitivity, specificity and variable detection comprehensiveness.

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
