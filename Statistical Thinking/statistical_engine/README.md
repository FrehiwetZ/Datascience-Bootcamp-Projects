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
git clone <https://github.com/FrehiwetZ/Datascience-Bootcamp-Projects/tree/main/Statistical%20Thinking/statistical_engine>
cd <Stastical thinking>/statistical_engine
```
## Testing

Unit tests are included in `test_stat_engine.py` using Python’s built-in `unittest` framework.

### How to Execute the Test Suite:
```bash
python -m unittest test_stat_engine.py
```
Tests cover:

Correct mean and median calculations for odd and even-length lists.
Handling of empty datasets (raises ValueError).
Correct mapping of standard deviation to known outcomes.
Accurate calculation of sample vs population variance.
Ensures mode is returned correctly or indicates "No mode." 


#Acceptance criteria checklist
The following checklist demonstrates that the project meets all required functionality and edge-case handling:
| Requirement                                           | Status |
| ----------------------------------------------------- | ------ |
| Handles empty lists gracefully (raises `ValueError`)  | ✅      |
| Ignores invalid data types (raises `TypeError`)       | ✅      |
| Calculates mean correctly for any dataset             | ✅      |
| Calculates median correctly for even and odd datasets | ✅      |
| Returns mode or "No mode" if all elements are unique  | ✅      |
| Calculates sample and population variance accurately  | ✅      |
| Computes standard deviation correctly                 | ✅      |
| Detects outliers using Z-score method                 | ✅      |
| Monte Carlo simulation runs for multiple day ranges   | ✅      |
| All unit tests pass                                   | ✅      |

#Author
Name: Frehiwet Zerihun
Date:April 7,2026G.c
