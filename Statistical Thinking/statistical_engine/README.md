# Statistical Engine Project

## Project Overview
The **Statistical Engine** project is a Python-based tool for calculating descriptive statistics and performing Monte Carlo simulations.  
It can compute **mean, median, mode, variance, standard deviation, and outliers** for a dataset, and simulate crash probabilities using Monte Carlo methods.  
This tool is robust to handle invalid data types and empty datasets gracefully.

---

## Mathematical Logic

1. **Mean (Average):**  
\[
\text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
\]

2. **Median:**  
- Sort the data.  
- **Odd-sized dataset:** middle value is the median.  
- **Even-sized dataset:** average of the two middle values.

3. **Mode:**  
- Value(s) that occur most frequently. Returns "No mode" if all values are unique.

4. **Variance (Dispersion):**  
- **Sample variance:**  
\[
s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}
\]  
- **Population variance:**  
\[
\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}
\]

5. **Standard Deviation:**  
\[
\text{Std Dev} = \sqrt{\text{Variance}}
\]

6. **Outliers (Z-score method):**  
\[
z = \frac{|x_i - \bar{x}|}{\text{Std Dev}}
\]  
- Values with \(z > \text{threshold}\) are considered outliers.

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone <https://github.com/FrehiwetZ/Datascience-Bootcamp-Projects>
cd <Stastical thinking>/statistical_engine
