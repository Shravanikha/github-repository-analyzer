# GitHub Repository Analyzer

I built this project using Python to explore how the GitHub API works and retrieve information about public repositories.

The application lets users enter a repository name and view its statistics. It also has a feature to compare two repositories and download the results as a CSV file.

## What it does

* Shows the number of stars, forks, and open issues.
* Displays the repository's main programming language.
* Shows repository statistics in a bar chart.
* Compares two GitHub repositories.
* Exports comparison results to a CSV file that can be opened in Excel.
* Handles invalid repository names and common API errors.

## Technologies used

* Python
* Streamlit
* Requests
* Pandas
* GitHub REST API

## How to run it

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd github-repository-analyzer
```

**3. Install the required libraries**

```bash
pip install streamlit requests pandas
```

**4. Start the application**

```bash
streamlit run dashboard.py
```

The application will open in your browser.

## What I learned

While building this project, I learned how to fetch data from an API using Python, handle API responses, display data in Streamlit, create charts, and export results to CSV.
