from rich.console import Console
import csv
import os

console = Console()

filename = "ai_student_discourse.csv"

# Create file with headers if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "id","platform","subreddit",
            "mentions_AI","AI_tool",
            "sentiment","mentions_grades","link"
        ])

console.print("Enter Reddit data", style="bold cyan")

while True:
    # auto-increment ID
    if os.path.exists(filename):
        with open(filename, "r") as file:
            row_count = sum(1 for row in file)
        id = row_count
    else:
        id = 1

    subreddit = input("Subreddit: ")
    mentions_AI = input("Mentions AI (yes/no): ")
    AI_tool = input("AI tool: ")
    sentiment = input("Sentiment: ")
    mentions_grades = input("Mentions grades (yes/no): ")
    link = input("Reddit link: ")

    console.print("\nYou entered:", style="bold yellow")
    console.print(f"{subreddit} | {link}")

    confirm = input("Is this correct? (yes/no): ")

    if confirm == "yes":
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                id,"Reddit",subreddit,
                mentions_AI,AI_tool,
                sentiment,mentions_grades,link
            ])
        console.print("Saved!\n", style="green")
    else:
        console.print("Re-enter data\n", style="red")

    more = input("Add another entry? (yes/no): ")
    if more != "yes":
        break
