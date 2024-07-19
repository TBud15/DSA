# A set union means “combine both sets.”
# • A set intersection means “find the items that show up in both sets” 
# (in this case, just the tomato).
# • A set difference means “subtract the items in one set from the items 
# in the other set

#Sets are like lists, except sets can't have duplicates.


fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])
fruits | vegetables #This is a set union.
set(["avocado", "beets", "carrots", "tomato", "banana"])
fruits & vegetables #This is a set intersection.
set(["tomato"])
fruits – vegetables #This is a set difference.
set(["avocado", "banana"])
vegetables – fruitss