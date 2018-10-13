#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:54:49 2017

@author: sufiyan

This is a text summarizer which creates a 
summary of the article in the file
'document.txt'. Example output can be 
found in the file 'output.txt'
"""

import nltk
from nltk import *

def read_tokens():
    f = open("document.txt")
    raw = f.read()
    return raw
    
def find_keywords(raw_data):
    tokens = word_tokenize(raw_data)
    tokens = [w for w in tokens if w.isalpha()]
    tagged_tokens = nltk.pos_tag(tokens)
    noun_tokens = [w[0] for w in tagged_tokens if w[1]=="NN" or w[1]=="NNS"]
    word_freq = nltk.FreqDist(noun_tokens)
    keywords = [w[0] for w in word_freq.most_common(3) if len(w[0])>3]
    return keywords

def split_sents(raw_data):
    delimiter = '.'
    split_data = raw_data.split(delimiter)
    return split_data
    
def get_misc_sents(sents):
    misc_data = [line for line in sents[1:-3]]
    misc_data.remove(max(misc_data))
    return misc_data



def keyword_lookup(kw, misc_sents):
    match = []
    delimiter = '.'
    for line in misc_sents:
        if kw[0] and kw[1] and kw[2] in line:
            match += line + delimiter
    return match

def generate_summary(sents, matching_sents):
    delimiter = '.'
    summary = sents[0] + delimiter
    summary += max(sents) + delimiter
    summary += ''.join(matching_sents)
    summary += sents[-2] + delimiter
    return summary
   
raw_data = read_tokens()
keywords = find_keywords(raw_data)
print("The keywords are: [" + ', '.join(keywords) + "]\n\n")
sents = split_sents(raw_data)
misc_sents = get_misc_sents(sents)
matching_sents = keyword_lookup(keywords, misc_sents)
summarized_data = generate_summary(sents, matching_sents)
print("The summarized data is as follows: " + "\n")
print(summarized_data)