import re


ingredient = "2 tazas de pollo (450 g)"

if len(re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)) != 0:
        print( max(re.findall(r"[-+]?\d*\.\d+|\d+", ingredient)))