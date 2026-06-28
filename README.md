 Healthcare Lead Generation System – Indore

 Overview

The Healthcare Lead Generation System is a data-driven project developed to identify potential business leads among healthcare businesses in Indore. The system automatically collects healthcare business information, checks their online presence, analyzes website quality, extracts publicly available contact details, and categorizes businesses based on lead potential.
The objective of the project is to help sales and marketing teams identify healthcare businesses that may benefit from digital services by highlighting clinics, hospitals, pharmacies, dentists, diagnostic centers, and other healthcare providers with limited online visibility.
This project was developed as part of practical training in Data Analytics and Lead Intelligence using Python and free open-source tools.

Project Workflow

The system follows a multi-step pipeline:

1. Collects healthcare business data from OpenStreetMap.
2. Searches each healthcare business online using DuckDuckGo Search.
3. Checks whether the business has an official website or mainly depends on referral/listing platforms.
4. Analyzes website quality and classifies it as No Website, Poor Website, or Good Website.
5. Extracts publicly available contact details such as phone number, email address, LinkedIn profile, and owner/founder name if available.
6. Assigns a lead score based on digital presence and outreach opportunity.
7. Categorizes businesses into High, Medium, or Low potential leads.
8. Stores the final structured results in CSV format.
9. Displays the results through an interactive Streamlit dashboard.



Lead Classification

Businesses are categorized according to their online presence, website quality, and opportunity potential.

 High Potential

Businesses with no official website, poor website quality, weak online visibility, or heavy dependency on third-party listing platforms.

 Medium Potential

Businesses with some online presence but still showing gaps in website quality, contact availability, or digital visibility.

 Low Potential

Businesses that already have stronger online presence, a good website, and fewer visible gaps for digital improvement.

 Website Classification

The system classifies websites into three basic categories:

 No Website

No official website was found for the business.

Poor Website

A website exists but has digital quality issues such as missing contact page, missing services page, weak content, poor accessibility, or technical issues.

 Good Website

The business has a properly working website with HTTPS, useful content, contact/appointment page, and service-related information.

---

 Technologies Used

The project was built using the following technologies:

* Python
* Google Colab
* OpenStreetMap
* Overpy
* DuckDuckGo Search
* DDGS
* Requests
* BeautifulSoup
* Pandas
* Streamlit
* CSV data storage



 Project Structure

```text
healthcare_lead_gen_project/
│
├── config.py
├── osm_scraper.py
├── online_presence_checker.py
├── website_analyzer.py
├── scorer.py
├── contact_extractor.py
├── merge_final.py
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    ├── healthcare_osm_raw.csv
    ├── healthcare_online_presence.csv
    ├── healthcare_website_analysis.csv
    ├── healthcare_scored_leads.csv
    ├── healthcare_contact_enriched.csv
    └── healthcare_leads_final.csv
```

Each script performs a specific task in the lead generation pipeline, from data collection to final dashboard visualization.



 File Description

 osm_scraper.py

Collects healthcare business data from OpenStreetMap using Overpy.

 online_presence_checker.py

Searches each business online using DuckDuckGo Search and identifies official websites or referral platform presence.

 website_analyzer.py

Checks website quality and classifies websites as No Website, Poor Website, or Good Website.

 scorer.py

Assigns lead scores and business potential categories based on website quality, online presence, and contact availability.

 contact_extractor.py

Extracts publicly available phone numbers, email addresses, LinkedIn profiles, and owner/founder names where available.

 merge_final.py

Combines all processed data into one final clean CSV file.

 app.py

Runs the Streamlit dashboard for viewing, filtering, sorting, and downloading healthcare leads.



 Running the Project

 Clone the Repository

```bash
git clone https://github.com/YOURUSERNAME/healthcare-lead-generation-system.git
cd healthcare-lead-generation-system
```

 Install Dependencies

```bash
pip install -r requirements.txt
```
 Execute the Data Pipeline

Run the scripts in this order:

```bash
python osm_scraper.py
python online_presence_checker.py
python website_analyzer.py
python scorer.py
python contact_extractor.py
python merge_final.py
```
 Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will be available locally in your browser.

 Running in Google Colab

This project can also be executed in Google Colab.

Basic Colab flow:

1. Mount Google Drive.
2. Create the project folder.
3. Create `config.py`.
4. Run each project script step by step.
5. Generate the final CSV file.
6. Launch the Streamlit dashboard using LocalTunnel.


Dashboard Features

The Streamlit dashboard provides:

* Total healthcare leads count
* High potential lead count
* Medium potential lead count
* Website availability count
* Phone number availability count
* Search functionality
* Category-based filtering
* Lead score sorting
* Rows-per-page selection
* Paginated lead table
* Add lead form
* CSV export functionality


Final Output Columns

The final dataset contains the following important columns:

* Business Name
* Industry Category
* Business Description
* Location
* Google Maps Profile Link
* OpenStreetMap Link
* Website URL
* Website Classification
* Website Status Code
* HTTPS Used
* Contact Page Found
* Services Page Found
* Website Analysis Reason
* Online Presence Type
* Referral Platform Links
* Phone Number
* Email Address
* Owner / Founder Name
* LinkedIn Profile
* Lead Score
* Business Potential Category
* Reason for Classification
* Detailed Score Reason
* Source
* Scrape Status
* Created Date


Dependencies

Required Python libraries include:

```text
pandas
overpy
requests
beautifulsoup4
ddgs
duckduckgo-search
tldextract
streamlit
selenium
```

Limitations

* The system only collects publicly available business information.
* Some healthcare businesses may not have complete data on OpenStreetMap.
* Online search results may vary depending on availability and search engine response.
* Owner/founder names and LinkedIn profiles are extracted only if publicly visible.
* The project does not collect or process any private patient or medical data.


Future Scope

Future improvements may include:

* Google Sheets integration
* Automated scheduled data updates
* Better AI-based business description generation
* More advanced website quality scoring
* Location-wise lead heatmaps
* Deployment of Streamlit dashboard online
* Integration with CRM tools


Author
Manas Kanungo
Data Analytics Intern

This project was developed for learning and internship purposes as part of practical training in Data Analytics, Web Scraping, Lead Generation, and Business Intelligence.
