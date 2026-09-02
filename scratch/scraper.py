import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

base_url = "https://lpx.thedpp.com"
pages = [
    "/introduction/",
    "/introduction/why/",
    "/introduction/model/",
    "/introduction/json/",
    "/introduction/example/",
    "/introduction/iptc/",
    "/schema/",
    "/schema/administrative/",
    "/schema/rights/",
    "/schema/events/",
    "/schema/editorial/",
    "/schema/renditions/",
    "/schema/json/",
    "/examples/",
    "/examples/reuters/",
    "/examples/reuters/example_event/",
    "/examples/reuters/cancelled_event/",
    "/examples/reuters/planned_event/",
    "/about/",
    "/about/acknowledgements/",
    "/about/license/",
    "/api/",
    "/api/recommendations/",
    "/api/graph/",
    "/api/rest/"
]

output_dir = "C:/Users/ajolley/lpx-website/src/content/docs"

for page in pages:
    url = f"{base_url}{page}"
    print(f"Fetching {url}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # The main content is in a div with class "td-content"
            content_div = soup.find('div', class_='td-content')
            if content_div:
                markdown = md(str(content_div), heading_style="ATX")
                
                # Cleanup the markdown a bit (remove the "Pageinfo" block if we want, or leave it)
                # Create the directory structure
                parts = [p for p in page.split('/') if p]
                if not parts:
                    continue # Skip root
                
                # if the page is just /introduction/ we name it introduction/index.md
                if page.endswith('/'):
                    dir_path = os.path.join(output_dir, *parts)
                    os.makedirs(dir_path, exist_ok=True)
                    file_path = os.path.join(dir_path, "index.md")
                else:
                    dir_path = os.path.join(output_dir, *parts[:-1])
                    os.makedirs(dir_path, exist_ok=True)
                    file_path = os.path.join(dir_path, f"{parts[-1]}.md")
                
                # write Frontmatter
                title = parts[-1].replace('_', ' ').title() if parts else "Docs"
                # try to get actual title from h1
                h1 = soup.find('h1')
                if h1:
                    title = h1.get_text().strip()
                
                frontmatter = f"---\ntitle: {title}\n---\n\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(frontmatter + markdown)
                print(f"Saved to {file_path}")
            else:
                print(f"No td-content found for {url}")
        else:
            print(f"Failed to fetch {url}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print("Scraping complete.")
