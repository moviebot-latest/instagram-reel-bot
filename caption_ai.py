import random
from hashtag_ai import generate_hashtags

hooks = [
"Wait for the last scene 😳",
"You won't expect this ending 🔥",
"This moment shocked everyone 😱"
]

def generate_caption():

    hook = random.choice(hooks)

    tags = generate_hashtags()

    return hook + "\n\n" + tags
