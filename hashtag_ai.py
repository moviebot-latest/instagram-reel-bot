import random

hashtags = [
"#viralreels",
"#fyp",
"#movieclip",
"#movielover",
"#cinema",
"#reelsviral",
"#hollywoodscene",
"#bollywoodscene"
]

def generate_hashtags():

    return " ".join(random.sample(hashtags,4))
