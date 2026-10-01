import os
import requests
import pandas as pd


BASE_URL = "https://jsonplaceholder.typicode.com"


def main():
    # Extract
    users_response = requests.get(f"{BASE_URL}/users", timeout=5)
    posts_response = requests.get(f"{BASE_URL}/posts", timeout=5)

    users_response.raise_for_status()
    posts_response.raise_for_status()

    users = users_response.json()
    posts = posts_response.json()

    # Transform
    users_df = pd.DataFrame(users)
    posts_df = pd.DataFrame(posts)

    #a) Users DataFrame
    print("Users:", len(users_df))

    #b) Add word_count
    posts_df["word_count"] = posts_df["body"].apply(
        lambda x: len(x.split())
    )

    #c) Merge users and posts
    merged_df = pd.merge(
        posts_df,
        users_df,
        left_on="userId",
        right_on="id",
        suffixes=("_post", "_user")
    )

    #d) Filter word_count > 30
    filtered_df = merged_df[merged_df["word_count"] > 30].copy()

    #e) Add category
    def get_category(word_count):
        if word_count <= 10:
            return "Short"
        elif word_count <= 30:
            return "Medium"
        else:
            return "Long"

    filtered_df["category"] = filtered_df["word_count"].apply(get_category)

    # Load
    os.makedirs("output", exist_ok=True)

    output_file = "output/etl_result.csv"
    filtered_df.to_csv(output_file, index=False)

    print(
        f"ETL completed: {len(users_df)} users, "
        f"{len(posts_df)} posts, "
        f"{len(filtered_df)} filtered posts"
    )


if __name__ == "__main__":
    main()