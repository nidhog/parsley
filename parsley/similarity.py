# -*- coding: utf-8 -*-
"""
Similarity Measure
Using APCA/SAX dimensionality reduction.
Considering strings as time series.

@author: ielouafiq
"""

class SimilarityMeasure(object):
	# Similarity measure generation factory
    def factory(similarity_measure_type):
        #return eval(type + "()")
        if similarity_measure_type == "APCA": return APCA()
        if similarity_measure_type == "SAX" : return SAX()
        assert 0, "Given similarity measure type is not handled: " + similarity_measure_type
    factory = staticmethod(factory)
		

class APCA(SimilarityMeasure):
	def __init__(self):
		pass
	def computeDistance(first_series, second_series):
		return 0
	
class SAX(SimilarityMeasure):
	def __init__(self):
		pass
	def computeDistance(first_series, second_series):
		return 0
