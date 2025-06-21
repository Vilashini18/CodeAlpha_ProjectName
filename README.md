# CodeAlpha_ProjectName

## Web Scraping Quotes - Data Analytics Internship Task

This project is a simple and effective Python-based web scraper that extracts inspirational quotes and their authors from [Quotes to Scrape](https://quotes.toscrape.com). It was completed as part of my Data Analytics internship with CodeAlpha.

---

## Objectives

- Learn and apply web scraping using Python
- Understand HTML structure and tags
- Convert unstructured data into a structured dataset
- Create a reusable script to generate datasets for analysis

---

## 🔧 Technologies Used

| Tool           | Purpose                          |
|----------------|----------------------------------|
| `Python 3.x`   | Programming language              |
| `requests`     | Fetch HTML content from website   |
| `BeautifulSoup`| Parse and extract HTML elements   |
| `pandas`       | Create and export structured CSV  |
| `GitHub`       | Host and version-control project  |

---

## How It Works

1. The script sends a GET request to `https://quotes.toscrape.com`
2. It parses the HTML using BeautifulSoup
3. It finds all `<div class="quote">` elements
4. For each quote block, it extracts:
   - The quote text (`<span class="text">`)
   - The author's name (`<small class="author">`)
5. It stores the data into a `pandas` DataFrame
6. Finally, it exports the data to a CSV file named `quotes_dataset.csv`

---

## Files Included

| File                 | Description                         |
|----------------------|-------------------------------------|
| `scrape_quotes.py`   | Main Python script for scraping     |
| `quotes_dataset.csv` | Final dataset with quotes and authors |
| `README.md`          | Project description and documentation |

---

## Output Sample

| Quote                                       | Author           |
|--------------------------------------------|------------------|
| "The world as we have created it..."       | Albert Einstein  |
| "It is our choices, Harry..."              | J.K. Rowling     |

---

## Status

✔️ Completed and submitted as Task 1 for the Data Analytics Internship.

---

## 📬 Contact

**Vilashini V**  
Intern at CodeAlpha  
📧 vilashiniv11a2@gmail.com 
🌐 [GitHub Profile](https://github.com/Vilashini18)
