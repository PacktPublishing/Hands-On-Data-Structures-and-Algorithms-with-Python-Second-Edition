import collections
from collections import ChainMap

dict1= {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5}
chainmap = collections.ChainMap(dict1, dict2)  # linking two dictionaries
print("print two lined dictionaries", chainmap)

print("print maps for chainmap", chainmap.maps)

print("print values for chainmap", chainmap.values)

print("print value for key 'b'- ",chainmap['b'])   #accessing values 

print("print value for key 'e'- ", chainmap['e'])


defaults= {'theme':'Default','language':'eng','showIndex':True, 'showFooter':True}

cm= ChainMap(defaults)   #creates a chainMap with defaults configuration
print("print maps for chainmap", cm.maps)

print("print values for chainmap", cm.values())

cm2= cm.new_child({'theme':'bluesky'}) # create a new chainMap with a child that overrides the parent.

print("print value for a value theme is", cm2['theme'])  #returns the overridden theme

print("print the entry for 'theme' key", cm2.pop('theme'))  # removes the child theme value

print("print updated chainmap", cm2['theme'])


print("print maps for another chainmap", cm2.maps)

print("print parent of chainmap2- ",cm2.parents)
