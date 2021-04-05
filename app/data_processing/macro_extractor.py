from utils import *
from equivalences import equivalences
import pandas as pd


def macro_extractor(nv):
    nv["grasa_cals_pctg"] = round((nv["grasa"]*9/4) / (nv["grasa"]*9/4 + nv["proteina"] + nv["carbohidratos"])*100,1)
    nv["proteina_cals_pctg"] =  round((nv["proteina"]) / (nv["grasa"]*9/4 + nv["proteina"] + nv["carbohidratos"])*100,1)
    nv["carbos_cals_pctg"] =  round((nv["carbohidratos"]) / (nv["grasa"]*9/4 + nv["proteina"] + nv["carbohidratos"])*100,1)
    return nv





if __name__ == "__main__":
    nutritional_values = pd.read_csv('../../data/nutritional_values.csv')
    nutri_values = macro_extractor(nutritional_values)
    nutri_values.to_csv('../../data/nutritional_values_macros.csv', index=True)
