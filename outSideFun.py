import pandas as pd
from enum import Enum
import os

class Selection(Enum):
    What_is_the_highest_price_of_a_diamond = 1

    What_is_the_average_price_of_a_diamond = 2

    How_many_Ideal_diamonds_exist = 3

    How_many_different_colors_do_the_diamonds_have_and_what_are_they = 4

    What_is_the_median_carat_of_Premium_diamonds = 5

    Create_the_average_carat_for_each_cut_type = 6

    Create_the_average_price_for_each_color_type = 7

    Exit = 8
    
def maine():
    for select in Selection:
        print(f"[{select.value}] -{select.name} ")
        
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_pries(type):
    typeCount=0
    sum=0
    df = pd.read_csv('diamonds.csv')
    filtered_df = df[df['color'] == type]
    
    for index, row in filtered_df.iterrows():
        typeCount += 1
        sum += row['price']
    avarge= sum / typeCount
    return print(f"The average of {type} price is {avarge}")


def find_carats(type): 
    typeCount=0
    sum=0
    df = pd.read_csv('diamonds.csv')
    filtered_df = df[df['cut'] == type]
    
    for index, row in filtered_df.iterrows():
        typeCount += 1
        sum += row['carat']
    avarge= sum / typeCount
    return print(f"The average of {type} carat is {avarge}")


def csvHandle(cohice):
    df = pd.read_csv('diamonds.csv')
    if cohice == 1:
        max = df['price'].max()
        print(f"{max} i the most expnsive")

    elif cohice == 2:
        totalPrice=0
        totalType=0
        for index, row in df.iterrows():
            totalPrice += row['price']
            totalType += 1
        sum = totalPrice / totalPrice
        print(f"The average price of diamond is {sum}")
    elif cohice == 3:
        totalIdeal = 0
        for type in df['cut']:
            if type == 'Ideal':
                totalIdeal += 1
        print(f"The average price of ideal diamonds is {totalIdeal}")
    
    elif cohice == 4:
        colors=[]
        sum = 0
        for index, row in df.iterrows():
            color = row['color']
            if color not in colors:
                colors.append(color)
        for color in colors:
            sum += 1
        print(f"the total type {sum} the types:")
        for i in colors:
            print(i)
        
    elif cohice == 5:
        premium_diamonds = df[df['cut'] == 'Premium']

        median_carat = premium_diamonds['carat'].median()

        print(f"The median carat of Premium diamonds is: {median_carat}")
    
    elif cohice == 6:
        typs=[]
        for index, row in df.iterrows():
            cut = row['cut']
            if cut not in typs:
                typs.append(cut)
        for type in typs:
            find_carats(type)
  


    elif cohice == 7:
       typs=[]
       for index, row in df.iterrows():
            color = row['color']
            if color not in typs:
                typs.append(color)
       for type in typs:
            find_pries(type)


