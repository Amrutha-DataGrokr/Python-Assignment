import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    #a) Fetch all 100 posts
    response=requests.get(url,timeout=5)
    response.raise_for_status()
    posts=response.json()
    print("Total posts:",len(posts))
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")
except json.JSONDecodeError:
    print("Error: Could not decode the JSON response.")

#b) Print title and body of posts 1, 25, 50 and 100
for post_number in [1,25,50,100]:
    post=posts[post_number-1]
    print(f"\nPost {post_number}")
    print("Title:",post["title"])
    print("Body:",post["body"])

#c) Filter posts where body contains more than 5 words
filtered_posts = [
    post for post in posts
    if len(post["body"].split()) > 5
]

print("\nPosts with more than 5 words:", len(filtered_posts))


#d) Build {userId: [list of post titles]}
posts_by_user = {}

for post in posts:
    user_id = post["userId"]

    if user_id not in posts_by_user:
        posts_by_user[user_id] = []

    posts_by_user[user_id].append(post["title"])


# Save to JSON file
with open("posts_by_user.json", "w") as file:
    json.dump(posts_by_user, file, indent=2)

print("Saved posts_by_user.json")