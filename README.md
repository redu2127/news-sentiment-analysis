# 10 Academy AI Mastery – Week 1 Challenge

## Financial News Sentiment Analysis 

## Project Overview

This project analyzes financial news headlines and historical stock price data to support predictive analytics for investment decision-making. The objective is to explore whether financial news sentiment can provide useful signals for stock market movement.

The work is framed around Nova Financial Solutions' goal of improving forecasting accuracy and supporting investment teams with data-driven insights.

## Tasks Completed

### Task 1: Exploratory Data Analysis

- Loaded and inspected the financial news dataset
- Cleaned date and headline fields
- Analyzed headline length distribution
- Identified top publishers
- Analyzed publication trends over time
- Extracted frequent keywords
- Applied topic modeling using LDA

### Task 2: Quantitative Analysis

- Loaded historical stock price data
- Handled missing values
- Computed technical indicators:
  - SMA
  - EMA
  - RSI
  - MACD
- Visualized stock price trends and indicators

### Task 3: Sentiment and Correlation Analysis

- Applied TextBlob sentiment scoring to financial news headlines
- Aggregated sentiment by day
- Calculated daily stock returns
- Merged sentiment scores with stock returns
- Computed Pearson correlation
- Visualized sentiment-return relationships

## Project Structure

```text
news-sentiment-analysis/
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   └── raw/
├── notebooks/
│   ├── task_1_eda.ipynb
│   ├── task_2_quantitative_analysis.ipynb
│   └── task_3_sentiment_correlation.ipynb
├── scripts/
│   ├── __init__.py
│   └── run_analysis.py
├── src/
│   ├── __init__.py
│   └── technical_indicators.py
├── tests/
│   ├── __init__.py
│   └── test_technical_indicators.py
├── requirements.txt
└── README.md