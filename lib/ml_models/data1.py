import csv
import pandas as pd


# Creating an expanded dataset for Gender-Based Insults
gender_based_insults = {
    'Gender-Based Insults': [
        "Feminazi", "Gold-digger", "Bimbo", "Bitchy", "Ballbuster",
        "Sugarbaby", "Catty", "Man-eater", "Cockblocker", "Drama queen",
        "Feminist bitch", "PMSing", "Sorority slut", "Trophy wife", "Homemaker",
        "Crybaby", "Housewife", "Weakling", "Bossy", "Attention whore",
        "Submissive", "Queen bee", "Diva", "Butterface", "Nag",
        "Henpecked", "Broflake", "Cuck", "Sissy boy", "Manchild",
        "Mansplainer", "Princess", "She-devil", "Shrew", "Harpy",
        "Fishwife", "Spinster", "Frigid", "Harridan", "Ladyboy",
        "Tomboy", "Butch", "Wench", "Tart", "Madam",
        "Ballbreaker", "Fish", "Sissy", "Pansy", "Alpha female",
        "Beta male", "Womanizer", "Girly", "Mommy's boy", "Daddy's girl",
        "Boy toy", "Slut-shamer", "Skirt chaser", "Cock tease", "Cougar",
        "Gigolo", "Jezebel", "Wife beater", "Whoremonger", "Lady killer",
        "Weak sauce", "Handmaiden", "Gold digger", "Spineless", "Miss priss",
        "Queen", "Peacock", "Flamboyant", "Macho man", "Chauvinist",
        "Sir", "Mister", "Master", "Old maid", "Baby doll",
        "Sexpot", "Cradle robber", "Pantywaist", "Mother hen", "Lady luck",
        "Bridezilla", "Tease", "Doormat", "Girlfriend experience", "Maiden",
        "Groomzilla", "Himbo", "Trophy husband", "Queen of the castle", "King of the castle",
        "Ballsy", "Lady's man", "Effeminate", "Softie", "Mama's boy",
        "Chick", "Doll", "Broad", "Dish", "Filly"
    ]
}

# Converting the dataset into a DataFrame
df_gender_based_insults = pd.DataFrame(gender_based_insults)

# Saving the dataset to a CSV file
csv_file_path_gender_insults = "term3.csv"
df_gender_based_insults.to_csv(csv_file_path_gender_insults, index=False)



