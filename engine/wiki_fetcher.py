import json

import wikipediaapi


def fetch_and_save_articles(articles, output_file="wiki_articles.json"):
    wiki_wiki = wikipediaapi.Wikipedia('MyCoolScript', extract_format=wikipediaapi.ExtractFormat.WIKI)

    with open(output_file, "w", encoding="utf-8") as file:
        for title in articles:
            page = wiki_wiki.page(title)
            if page.exists():
                # Replace newline characters with \\n
                escaped_text = page.text.replace('\n', '\\n')
                # Create a dictionary for the JSON object
                article_data = {
                    "article_name": title,
                    "link": f"https://en.wikipedia.org/wiki/{title}",
                    "text_content": escaped_text
                }
                file.write(json.dumps(article_data) + "\n")
            else:
                file.write(json.dumps({"error": f"Page '{title}' does not exist."}) + "\n")


if __name__ == "__main__":
    # List of specified articles
    specified_articles = [
        "Python_(programming_language)",
        "Artificial_intelligence",
        "SpaceX",
        "Mars",
        "Leonardo_da_Vinci",
        "Quantum_mechanics",
        "Global_warming",
        "Nelson_Mandela",
        "Music",
        "Ancient_Egypt",
        "Cancer",
        "Black_hole",
        "Apollo_11",
        "Renaissance",
        "Einstein",
        "Climate_change",
        "The_Great_Gatsby",
        "Neptune",
        "Human_evolution",
        "Steve_Jobs"
    ]

    fetch_and_save_articles(specified_articles)
