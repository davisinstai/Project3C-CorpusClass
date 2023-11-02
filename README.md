# Analyzing Corpora with Spacy - The Corpus Class

# Project 3c

## Name

## Class year

## Extension(s) - Describe your extension(s) here

## Resources - Who or what did you use to finish this project deliverable?


-----------------------------------------------------------------------------------------------------------------------------------------------
*Please do not edit below this line!*
-----------------------------------------------------------------------------------------------------------------------------------------------

## Project Description

The goals of this assignment are:
* To develop an object oriented version of our corpus code, focusing on writing the most concise readable code possible.

Here are the steps you should do to successfully complete this project:
1. From moodle, accept the assignment. Open and set up a code space (install a python kernel and select it).
2. Complete the notebook and commit it to Github. Make sure to answer all questions, and to commit the notebook in a "run" state!
3. I wrote the comments; you write the code! Complete and run `spacy_on_corpus.py` following the instructions in this notebook.
4. Edit the README.md file. Provide your name, your class year, links to/descriptions of any extensions and a list of resources. 
5. Commit your code often. We will take the last commit before the deadline as your submission of the project.

Possible extensions (from least points to most points):

* Add one other type of corpus or document visualization or statistic.
* Modify the token, entity, and noun chunk functions so they count only lower cased tokens, entities and noun chunks.
* the `collections` package in python has a counter class. Copy `spacy_on_corpus.py` to `spacy_on_corpus_collections.py`. Try using that class instead. Time the execution of the test code for counter in section **Test the Counter Class** below. Which is faster: your counter class, or the one in collections?
* Copy `spacy_on_corpus.py` to `spacy_on_corpus_document.py`. In the new file, make a document class. Move the methods `render_doc_markdown`, `render_doc_table` and `render_doc_statistics` to the document class. Test it.
* We can currently represent tokens, entities and sentences. Use the span class we developed this week in class to implement a representation of paragraphs. Add a list of paragraph spans to each document. Add summary statistics about paragraphs to `get_basic_statistics`.
* Your other ideas are welcome! If you'd like to discuss one with Dr Stent, feel free.

## Project Rubric

- [] Notebook is code-complete and outputs are correct. (5 points)
- [] All ten questions in notebook are completely and correctly answered. (5 points)
- [] File spacy_on_corpus.py is complete, runs and is commented. (6  points)
- [] In spacy_on_corpus.py, the number of lines of code specified by Dr. Stent is the number student used to complete each method. (6 points) 
- [] Student made meaningful commit messages (1 pt)
- [] Readme has student's name, class year and resources student used. (2 points)
- [] Extension (1-2 points for a start; 3-4 points for a complete extension; 5 points for a surprising and creative extension)

### Comments from grader
