## 📊 AWS Industrial Machine Failure Analysis  
End-to-end AWS data engineering pipeline using S3, Glue Crawler, Athena, and QuickSight to analyze industrial IoT machine failure data (AI4I dataset).

---

## 🏗️ Architecture Overview
![architecture](https://raw.githubusercontent.com/Sampreethi66/aws-industrial-machine-failure-analysis/main/assets/architecture.png)

---

## 🚀 Key Features
- Ingested the AI4I industrial dataset into Amazon S3  
- Converted raw CSV → optimized Parquet for analytics  
- Built AWS Glue Crawler to infer schema into Data Catalog  
- Queried data using Amazon Athena SQL  
- Designed and published a QuickSight dashboard with failure insights  
- Automated refresh through QuickSight SPICE  

---

## 📁 Dataset
AI4I Industrial IoT dataset (10,000 rows) containing sensor values:
- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  
- Machine failure (target)

---

## 🛠️ AWS Services Used
| Service | Purpose |
|--------|---------|
| **S3** | Stores raw + curated data |
| **Glue Crawler** | Creates schema in Glue Data Catalog |
| **Athena** | SQL queries on S3 parquet |
| **QuickSight** | Dashboard + insights |
| **IAM** | Secure access between services |

---

## 📊 Dashboard Preview
![dashboard](https://raw.githubusercontent.com/Sampreethi66/aws-industrial-machine-failure-analysis/main/assets/dashboard.png)

---

## 🐝 Glue Crawler Result
![glue_crawler](https://raw.githubusercontent.com/Sampreethi66/aws-industrial-machine-failure-analysis/main/assets/glue_crawler.png)

---

## 🔍 Athena Query Output
![athena_query](https://raw.githubusercontent.com/Sampreethi66/aws-industrial-machine-failure-analysis/main/assets/athena_query.png)

---

## 📈 Insights Discovered
- Majority of machines **do not fail**, but failed machines show high torque & tool wear  
- Higher **process temperature (K)** correlates with greater failure risk  
- Machines with high **rotational speed** and **torque fluctuations** are more failure-prone  
- Tool wear shows a linear degradation trend leading to failures  

---

## 🧠 Future Work (Optional Enhancements)
- Build ML failure prediction model  
- Automate pipeline using Lambda + Step Functions  
- Build anomaly detection via Amazon Lookout for Equipment  

---

## 📝 Author
Sampreethi Bokka  
UT Dallas — Data Engineering & Machine Learning Projects  
