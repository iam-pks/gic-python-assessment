import matplotlib.pyplot as plt
import seaborn as sns

def plot_rating_distribution(df):
    plt.figure(figsize=(6,4))
    sns.histplot(df["rating"], bins=10, kde=True)
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.savefig("rating_distribution.png")
    print("Saved plot as rating_distribution.png")
