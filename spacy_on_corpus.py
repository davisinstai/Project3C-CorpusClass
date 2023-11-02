# import spacy for nlp
import spacy
# import glob in case user enters a file pattern
import glob
# import shutil in case user enters a compressed archive (.zip, .tar, .tgz etc.); this is more general than zipfile
import shutil
# import matplotlib for making graphs
import matplotlib.pyplot as plt
# import wordcloud for making wordclouds
import wordcloud
# import json
import json 
# import re
import re

class counter(dict):
    def __init__(self, list_of_items, top_k=-1):
        """Makes a counter.

        :param list_of_items: the items to count
        :type list_of_items: list
        :param top_k: the number you want to keep
        :type top_k: int
        :returns: a counter
        :rtype: counter
        """
        super().__init__()
        # Add each item in list_of_items to this counter (2 lines)
        # HINT: Use the add_item method

        # Reduce to top k if top_k is greater than 0 (2 lines)
        # HINT: Use the reduce_to_top_k method

        # you don't have to return explicitly, since this is a constructor
        
    def add_item(self, item):
        """Adds an item to the counter.

        :param item: thing to add
        :type item: any
        """
        # Add an item to this counter (3 lines)
        # HINT: use self[item], since a counter is a dictionary
        pass # remove pass

    def get_counts(self):
        """Gets the counts from this counter.

        :returns: a list of (item, count) pairs
        :type item: list[tuple]
        """
        # Return a list of tuples (item, count) from this counter (1 line)
        # HINT: what methods does a counter have? Check using help
        return None # replace None
    
    def reduce_to_top_k(self, top_k):
        """Gets the top k most frequent items.

        :param top_k: the number you want to keep
        :type top_k: int
        """
        # making sure we don't try to remove more elements than there are!
        top_k = min([top_k, len(self)])
        # Sort the frequency table by frequency (least to most frequent) (1 line)

        # Drop all but the top k from this counter (2 lines)
        # HINT: go from 0 to len(self)-top_k
        # HINT: use the pop() method; after all, counter is a dictionary!

class corpus(dict):
    nlp = spacy.load('en_core_web_md')          
                         
    def __init__(self, name=''):
        """Creates or extends a corpus.

        :param name: the name of this corpus
        :type name: str
        :returns: a corpus
        :rtype: corpus
        """
        super().__init__()
        # Set or update instance variables (1 line)
       
    def get_documents(self):
        """Gets the documents from the corpus.

        :returns: a list of spaCy documents
        :rtype: list
        """
        # Get a list of the documents in this corpus (1 line)
        # HINT: use a list comprehension
        return None # replace None
   
    def get_document(self, id):
        """Gets a document from the corpus.

        :param id: the document id to get
        :type id: str
        :returns: a spaCy document
        :rtype: (spaCy) doc
        """
        # Get a single document from the corpus (1 line)
        # HINT: check if id is in this corpus and if the item corresponding to id has a 'doc' key
        return None # replace None
                         
    def get_metadatas(self):
        """Gets the metadata for each document from the corpus.

        :returns: a list of metadata dictionaries
        :rtype: list[dict]
        """
        # Get all the metadata dictionaries from the corpus (1 line)
        # HINT: use a list comprehension
        return None # replace None

    def get_metadata(self, id):
        """Gets a document from the corpus.

        :param id: the document id to get
        :type id: str
        :returns: a spaCy document
        :rtype: (spaCy) doc
        """
        # Get a single document from the corpus (1 line)
        # HINT: check if id is in this corpus and if the item corresponding to id has a 'doc' key
        return None # replace None
                             
    def add_document(self, id, doc, metadata={}):
        """Adds a document to the corpus.

        :param id: the document id
        :type id: str
        :param doc: the document itself
        :type doc: (spaCy) doc
        :param metadata: the document metadata
        :type metadata: dict
        """
        # adds a document to the corpus
        self[id] = {'doc': self.nlp(doc), 'metadata': metadata}
        
    def get_token_counts(self, tags_to_exclude = ['PUNCT', 'SPACE'], top_k=-1):
        """Builds a token frequency table.

        :param tags_to_exclude: (Coarse-grained) part of speech tags to exclude from the results
        :type tags_to_exclude: list[string]
        :returns: a list of pairs (item, frequency)
        :rtype: list
        """
        # Make an empty list of tokens (1 line)
 
        # For each doc in the corpus, add its tokens to the list of tokens (2 lines)

        # Count the tokens using a counter object; return a list of pairs (item, frequency) (1 line)
        # HINT: use the counter class
        pass # remove pass

    def get_entity_counts(self, tags_to_exclude = ['QUANTITY'], top_k=-1):
        """Builds an entity frequency table.

        :param tags_to_exclude: named entity labels to exclude from the results
        :type tags_to_exclude: list[string]
        :returns: a list of pairs (item, frequency)
        :rtype: list
        """
        # Using get_token_counts as a model, define get_entity_counts using get_documents and a counter object (4 lines of code)

        return None # replace None
    
    def get_noun_chunk_counts(self, top_k=-1):
        """Builds a noun chunk frequency table.

        :returns: a list of pairs (item, frequency)
        :rtype: list
        """
        # Using get_token_counts as a model, define get_noun_chunk_counts using get_documents and a counter object (4 lines of code)

        return None # replace None

    def get_metadata_counts(self, key, top_k=-1):
        """Gets frequency data for the values of a particular metadata key.

        :param key: a key in the metadata dictionary
        :type key: str
        :returns: a list of pairs (item, frequency)
        :rtype: list
        """
        # Using get_token_counts as a model, define get_metadata_counts using get_metadatas and a counter object (2 lines of code)
        # HINT: use a list comprehension, the get_metadatas method, and then the counter class

        # return the metadata counts as a list of pairs
        return None # replace None

    def get_basic_statistics(self):
        """Prints summary statistics for the corpus.
        """
        # We want the same output as in project 3b, but using the corpus class methods
        pass # remove pass

    def plot_counts(self, counts, file_name):
        """Makes a bar chart for counts.

        :param counts: a list of item, count tuples
        :type counts: list
        :param file_name: where to save the plot
        :type file_name: string
        """
        plt.barh([x[0] for x in counts], [x[1] for x in counts])
        plt.rcParams.update({'axes.unicode_minus' : False})
        plt.tight_layout()
        plt.savefig(self.name + '_' + file_name)
        plt.clf()

    def plot_token_frequencies(self, tags_to_exclude=['PUNCT', 'SPACE'], top_k=25):
        """Makes a bar chart for the top k most frequent tokens in the corpus.
        
        :param top_k: the number to keep
        :type top_k: int
        :param tags_to_exclude: tags to exclude
        :type tags_to_exclude: list[str]
        """
        # Make a bar chart of the top most frequent tokens in the corpus (2 lines)
        # HINT: use the get_token_counts and plot_counts methods in corpus
        pass # remove pass

    def plot_entity_frequencies(self, tags_to_exclude=['QUANTITY'], top_k=25):
        """Makes a bar chart for the top k most frequent entities in the corpus.
        
        :param top_k: the number to keep
        :type top_k: int
        :param tags_to_exclude: tags to exclude
        :type tags_to_exclude: list[str]
       """
        # Make a bar chart of the top most frequent entities in the corpus (2 lines)

        pass # remove pass
   
    def plot_noun_chunk_frequencies(self, top_k=25):
        """Makes a bar chart for the top k most frequent noun chunks in the corpus.
        
        :param top_k: the number to keep
        :type top_k: int
        """
        # Make a bar chart of the top most frequent noun chunks in the corpus (2 lines)

        pass # remove pass
   
    def plot_metadata_frequencies(self, key, top_k=25):
        """Makes a bar chart for the frequencies of values of a metadata key in a corpus.

        :param key: a metadata key
        :type key: str        
        :param top_k: the number to keep
        :type top_k: int
        """
        # Make a bar chart of the top most frequent values for metadata key key (2 lines)
 
        pass # remove pass

    def plot_word_cloud(self, counts, file_name):
        """Plots a word cloud.

        :param counts: a list of item, count tuples
        :type counts: list
        :param file_name: where to save the plot
        :type file_name: string
        """
        try:
            # get rid of pesky newline characters
            counts = [(x[0].replace('\n', ''), x[1]) for x in counts]
            # make the word cloud
            wc = wordcloud.WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(dict(counts))
            # plot the word cloud
            plt.figure(figsize=(10, 10))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.savefig(self.name + '_' + file_name)
            plt.clf()
        except Exception as e:
            print('Couldn\'t make wordcloud', file_name, e)

    def plot_token_cloud(self, tags_to_exclude=['PUNCT', 'SPACE']):
        """Makes a word cloud for the frequencies of tokens in a corpus.

        :param tags_to_exclude: tags to exclude
        :type tags_to_exclude: list[str]
        """
        # Plot a word cloud for tokens (2 lines)
        
        pass # remove pass
 
    def plot_entity_cloud(self, tags_to_exclude=['QUANTITY']):
        """Makes a word cloud for the frequencies of entities in a corpus.
 
        :param tags_to_exclude: tags to exclude
        :type tags_to_exclude: list[str]
        """
        # Plot a word cloud for entities (2 lines)
        
        pass # remove pass

    def plot_noun_chunk_cloud(self):
        """Makes a word cloud for the frequencies of noun chunks in a corpus.
        """
        # Plot a word cloud for noun chunks (2 lines)
        
        pass # remove pass
        
    def render_doc_markdown(self, doc_id):
        """Render a document as markdown. From project 2a. 

        :param doc_id: the id of a spaCy doc made from the text in the document
        :type doc: str
        """
        doc = self.get_document(doc_id)
        # Same definition as in project 3b, but prefix the output file name with self.name to make it unique to this corpus

        # open an output file, named after the document with _text.md appended
        with open(self.name + '_' + doc_id.replace('/', '') + '_text.md', 'w') as outf:
            # write 'text'
            outf.write(text)

    def render_doc_table(self, doc_id):
        """Render a document's token and entity annotations as a table. From project 2a. 

        :param doc_id: the id of a spaCy doc made from the text in the document
        :type doc: str
        """
        doc = self.get_document(doc_id)
        # Same definition as in project 3b, but prefix the output file name with self.name to make it unique to this corpus

        # open an output file, named after the document with _table.md appended
        with open(self.name + '_' + doc_id.replace('/', '') + '_table.md', 'w') as outf:
            # write 'tokens_table'
            outf.write(tokens_table)
            outf.write('\n')
            # write 'entities_table'
            outf.write(entities_table)

    def render_doc_statistics(self, doc_id):
        """Render a document's token and entity counts as a table. From project 2a. 

        :param doc_id: the id of a spaCy doc made from the text in the document
        :type doc: str
        """
        doc = self.get_document(doc_id)
        # Same definition as in project 3b, but prefix the output file name with self.name to make it unique to this corpus

        # open an output file, named after the document with _stats.md appended
        with open(self.name + '_' + doc_id.replace('/', '') + '_stats.md', 'w') as outf:
            # write the header for a table of tokens/entities and counts
            outf.write('| Token/Entity | Count |\n | ------------ | ----- |\n')
            # print the key and count for each entry in 'stats'
            for key in sorted(stats.keys()):
                outf.write('| ' + key + ' | ' + str(stats[key]) + ' |\n')

    @classmethod
    def load_textfile(cls, file_name, my_corpus=None):
        """Loads a textfile into a corpus.

        :param file_name: the path to a text file
        :type file_name: string
        :param my_corpus: a corpus
        :type my_corpus: corpus
        :returns: a corpus
        :rtype: corpus
         """
        # make sure we have a corpus
        if my_corpus == None:
            my_corpus = corpus()
        # Mostly the same as in project 3b, but use the corpus class add method; don't forget to return my_corpus (3 lines of code)
        # open file_name as f

    @classmethod  
    def load_jsonl(cls, file_name, my_corpus=None):
        """Loads a jsonl file into a corpus.

        :param file_name: the path to a jsonl file
        :type file_name: string
        :param my_corpus: a my_corpus
        :type my_corpus: my_corpus
        :returns: a my_corpus
        :rtype: my_corpus
         """
        # make sure we have a my_corpus
        if my_corpus == None:
            my_corpus = corpus()
        # Most the same as in project 3b, but use the corpus add method; don't forget to return my_corpus (6 lines of code)

    @classmethod   
    def load_compressed(cls, file_name, my_corpus=None):
        """Loads a zipfile into a corpus.

        :param file_name: the path to a zipfile
        :type file_name: string
        :param my_corpus: a corpus
        :type my_corpus: corpus
        :returns: a corpus
        :rtype: corpus
       """
        # make sure we have a corpus
        if my_corpus == None:
            my_corpus = corpus()
        # Mostly the same as in project 3b; don't forget to return my_corpus (5 lines of code)

    @classmethod
    def build_corpus(cls, pattern, my_corpus=None):
        """Builds a corpus from a pattern that matches one or more compressed or text files.

        :param pattern: the pattern to match to find files to add to the corpus
        :type file_name: string
        :param my_corpus: a corpus
        :type my_corpus: corpus
        :returns: a corpus
        :rtype: corpus
         """
         # make sure we have a corpus
        if my_corpus == None:
            my_corpus = corpus(pattern)
       # Mostly the same as in project 3b; don't forget to return my_corpus (11 lines of code)

def main():
    """The main function. 
      First we ask the user for a pattern. 
      Then, we build a corpus. 
      Then, we let the user choose whether they want corpus statistics, plots of corpus wordcounts, or a wordcloud for the corpus.
    """
    # Same as in project 3b, but using the corpus class
    pass # remove pass

# this says, if executing this on the command line like python spacy-on-my_corpus.py, run main()    
if __name__ == "__main__":
    main()