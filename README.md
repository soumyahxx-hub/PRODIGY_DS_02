🧠 PRODIGY_DS_02 — Bank Marketing Data Analysis
📌 Project Overview

This project explores the Bank Marketing Dataset to analyze customer behavior and predict subscription trends for term deposits.
It uses data analysis, visualization, and trend exploration techniques to uncover key business insights.

The goal of this project is to understand which customer attributes and marketing strategies lead to successful term deposit subscriptions.

⚙️ Tech Stack

🐍 Python 3.10+

📊 Pandas — Data manipulation & analysis

🔢 NumPy — Numerical operations

📈 Matplotlib / Seaborn — Data visualization

🧠 Scikit-learn (optional) — For modeling and correlations
📁 Project Structure
bank-marketing-tree/
│
├── bank_marketing_data/
│   ├── bank_data/                      # Original dataset (bank.csv, etc.)
│   └── bank_additional_data/           # Additional dataset (bank-additional-full.csv)
│
├── analyze_bank_data.py                # Loads and previews dataset
├── analyze_bank_insights.py            # Generates visual insights
├── analyze_bank_trends.py              # Trend analysis and correlation plots
│
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Files ignored in version control
└── README.md                           # Project documentation
🚀 How to Run

1️⃣ Clone the repository
git clone https://github.com/soumyahxx-hub/PRODIGY_DS_02.git
cd PRODIGY_DS_02
2️⃣ Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate     # (Windows)
3️⃣ Install required packages
pip install -r requirements.txt
4️⃣ Run analysis scripts
python analyze_bank_data.py
python analyze_bank_insights.py
python analyze_bank_trends.py

📊 Key Insights
Education & Job Influence: Higher education and certain job types are more likely to subscribe to term deposits.

Campaign Efficiency: Too many contacts per campaign reduce success probability.

Balance & Age Trends: Customers with higher balances and specific age groups respond better to marketing efforts.

Correlation Heatmap: Displays relationships among numeric features like duration, campaign count, and previous outcomes.

🧩 Visualizations
Includes:

Count plots for subscription rates

Education vs Subscription trends


Correlation heatmap for numeric features
🏁 Future Enhancements

Integrate machine learning models (e.g., logistic regression, random forest).

Automate insight generation.

Deploy interactive dashboards using Streamlit.

🧑‍💻 Author

Soumyadeep Guha
📧 GitHub Profile →

🎯 Data Science | Machine Learning | Analytics

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.
