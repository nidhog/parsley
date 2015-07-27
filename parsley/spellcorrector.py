# -*- coding: utf-8 -*-
"""
Spell correction

@author: ielouafiq
"""
import re
import collections


class SpellCorrector(object):
    """Spell Correction Object inspired from Peter Norvig, http://norvig.com
    """
    def __init__(self, dict_file = 'gutenberg.dict', 
                 alphabet = 'abcdefghijklmnopqrstuvwxyz'):
            self.dict_file = dict_file
            self.word_frequency_model = self.compute_word_frequency(self.words(file(self.dict_file).read()))
            self.alphabet = alphabet

    def preprocess(self, text):
        return text.lower()
    
    def words(self, text): 
        return re.findall('[a-z]+', self.preprocess(text))
    
    def compute_word_frequency(self, words):
        # Initialize word frequency Hash Table, set default value to 1
        freq_map = collections.defaultdict(lambda: 1)
        for word in words:
            freq_map[word] += 1
        return freq_map
        
    def change_dict_and_model(self, new_dict):
        self.dict_file = new_dict
        self.word_frequency_model = self.compute_word_frequency(self.words(file(self.dict_file).read()))
        
    def get_one_edit_away(self, word):
        splits      = [(word[:i], word[i:]) for i in range(len(word)+1)]
        deletes     = [ a+b[1:] for a, b in splits if b]
        transposes  = [ a+b[1]+b[0]+b[2:] for a,b in splits if len(b)>1] 
        replaces    = [ a+c+b[1:] for a,b in splits for c in self.alphabet if b]
        inserts     = [ a+c+b for a,b in splits for c in self.alphabet]
        return set(deletes+transposes+replaces+inserts)
    
    def get_two_edits_away(self, word):
        return set(change for change_word in self.get_one_edit_away(word) for change in self.get_one_edit_away(change_word))
        
    def get_edits_in_dict(self, word):
        return set(actual_word for edit_word in self.get_one_edit_away(word) 
        for actual_word in self.get_one_edit_away(edit_word) if actual_word in self.word_frequency_model)
        
    def get_dict_intersect(self, words):
        return set(word for word in words if word in self.word_frequency_model)
    
    def correct_word(self, word):
        candidate_words = self.get_dict_intersect([word]) or self.get_dict_intersect(self.get_one_edit_away(word)) or self.get_edits_in_dict(word) or [word]
        return max(candidate_words, key=self.word_frequency_model.get), candidate_words
        
if __name__== "__main__":
    s = raw_input().strip()
    spellCheck = SpellCorrector()
    print spellCheck.correct_word(s)