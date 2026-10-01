"""
(e) Predict the Output:
The following code calculates the word count for each post and counts 
how many posts have more than 3 words."""
import pandas as pd

posts = [
    {'userId': 1, 'body': 'hello world foo bar'},
    {'userId': 1, 'body': 'hi'},
    {'userId': 2, 'body': 'a b c d e f g h'}
]

df = pd.DataFrame(posts)

df['wc'] = df['body'].apply(lambda x: len(x.split()))

print(df['wc'].tolist())
print(len(df[df['wc'] > 3]))