import pandas as pd
import numpy as np
from scipy.stats import gmean
import matplotlib.pyplot as plt

def calculate_cgar(returns):
    """
    Calculate the Compound Growth Annual Return (CGAR)
    """
    return gmean(1 + returns) ** (1 / len(returns)) - 1

def plot_cgar_bar_chart(cgars, labels):
    """
    Plot a bar chart of CGARs
    """
    plt.bar(labels, cgars)
    plt.xlabel('Period')
    plt.ylabel('CGAR')
    plt.title('Compound Growth Annual Return (CGAR)')
    plt.show()

def assist_with_cgar(data):
    """
    Assist with calculating and plotting CGAR
    """
    cgars = []
    labels = []
    for period, group in data.groupby('Period'):
        returns = group['Returns']
        cgar = calculate_cgar(returns)
        cgars.append(cgar)
        labels.append(period)
    print("CGARs:")
    for period, cgar in zip(labels, cgars):
        print(f"{period}: {cgar:.2f}")
    plot_cgar_bar_chart(cgars, labels)

def main():
    # Sample data
    data = pd.DataFrame({
        'Period': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Returns': [[0.01, 0.02, 0.03], [0.04, 0.05, 0.06], [0.07, 0.08, 0.09], [0.10, 0.11, 0.12]]
    })
    data = data.explode('Returns')
    
    assist_with_cgar(data)

if __name__ == "__main__":
    main()
