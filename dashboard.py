
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="GitHub Analyzer", page_icon="📊", layout="wide")

st.title("📊 GitHub Repository Analyzer")
st.write("Analyze and compare public GitHub repositories.")

def get_repo(repo):
    repo = repo.strip()
    if not repo or len(repo.split("/")) != 2:
        return None

    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        st.error(f"Repository not found: {repo}")
    elif response.status_code == 403:
        st.error("GitHub API rate limit reached. Try again later.")
    else:
        st.error(f"GitHub API error: {response.status_code}")

    return None

tab1, tab2 = st.tabs(["Repository Analysis", "Compare Repositories"])

with tab1:
    repo = st.text_input("Repository (owner/name)", "psf/requests")

    if st.button("Analyze Repository"):
        try:
            data = get_repo(repo)

            if data:
                st.success("Repository found!")
                st.subheader(data["full_name"])
                st.write(data.get("description") or "No description available.")

                c1, c2, c3, c4 = st.columns(4)
                c1.metric("⭐ Stars", f'{data["stargazers_count"]:,}')
                c2.metric("🍴 Forks", f'{data["forks_count"]:,}')
                c3.metric("📌 Open Issues", f'{data["open_issues_count"]:,}')
                c4.metric("💻 Language", data.get("language") or "Unknown")

                chart = pd.DataFrame({
                    "Metric": ["Stars", "Forks", "Open Issues"],
                    "Count": [
                        data["stargazers_count"],
                        data["forks_count"],
                        data["open_issues_count"]
                    ]
                })
                st.subheader("Repository Statistics")
                st.bar_chart(chart, x="Metric", y="Count")

                st.link_button("Open on GitHub", data["html_url"])

        except requests.exceptions.RequestException:
            st.error("Network error. Check your internet connection.")

with tab2:
    repo1 = st.text_input("First repository", "psf/requests")
    repo2 = st.text_input("Second repository", "streamlit/streamlit")

    if st.button("Compare Repositories"):
        try:
            data1 = get_repo(repo1)
            data2 = get_repo(repo2)

            if data1 and data2:
                comparison = pd.DataFrame([
                    {
                        "Repository": data1["full_name"],
                        "Stars": data1["stargazers_count"],
                        "Forks": data1["forks_count"],
                        "Open Issues": data1["open_issues_count"]
                    },
                    {
                        "Repository": data2["full_name"],
                        "Stars": data2["stargazers_count"],
                        "Forks": data2["forks_count"],
                        "Open Issues": data2["open_issues_count"]
                    }
                ])

                st.subheader("Comparison Results")
                st.dataframe(comparison, use_container_width=True)

                st.subheader("Stars Comparison")
                st.bar_chart(comparison, x="Repository", y="Stars")

                st.subheader("Forks Comparison")
                st.bar_chart(comparison, x="Repository", y="Forks")

                csv = comparison.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download Comparison as CSV",
                    data=csv,
                    file_name="github_comparison.csv",
                    mime="text/csv"
                )

        except requests.exceptions.RequestException:
            st.error("Network error. Check your internet connection.")