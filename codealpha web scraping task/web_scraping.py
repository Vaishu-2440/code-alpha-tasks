import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find job cards
job_cards = soup.find_all("div", class_="card-content")

# Store job data
jobs = []

# Extract details
for job in job_cards:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()

    jobs.append({
        "Job Title": title,
        "Company": company,
        "Location": location,
        "Description": description
    })

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("job_listings.csv", index=False)

print("Web scraping completed successfully!")
