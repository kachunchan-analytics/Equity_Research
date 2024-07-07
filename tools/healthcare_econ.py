import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import requests

def get_world_bank_data(indicator, country, start_year, end_year):
    """
    Get data from the World Bank API.

    Parameters:
    indicator (str): The indicator code (e.g. 'SP.POP.TOTL' for total population)
    country (str): The country code (e.g. 'USA' for United States)
    start_year (int): The start year for the data
    end_year (int): The end year for the data

    Returns:
    pandas.DataFrame: The data from the World Bank API
    """
    url = f'http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=1000&date={start_year}:{end_year}'
    response = requests.get(url)
    data = response.json()[1]
    df = pd.DataFrame(data)
    return df

def calculate_healthcare_costs(resistance_rate, population, avg_treatment_cost):
    """
    Calculate the cumulative annual healthcare costs for treating drug-resistant bacterial infections.

    Parameters:
    resistance_rate (float): The rate of antimicrobial resistance (e.g. 0.2 for 20%)
    population (int): The population of the country/region
    avg_treatment_cost (float): The average cost of treating a drug-resistant bacterial infection

    Returns:
    float: The cumulative annual healthcare costs
    """
    return resistance_rate * population * avg_treatment_cost

def estimate_market_size(year, growth_rate, initial_market_size):
    """
    Estimate the market size for novel antibacterial therapies.

    Parameters:
    year (int): The year for which to estimate the market size
    growth_rate (float): The annual growth rate of the market (e.g. 0.1 for 10%)
    initial_market_size (float): The initial market size

    Returns:
    float: The estimated market size for the given year
    """
    return initial_market_size * (1 + growth_rate) ** (year - 2023)

def job_creation_estimate(market_size, job_creation_rate):
    """
    Estimate the number of jobs created in the biotechnology and pharmaceutical industries.

    Parameters:
    market_size (float): The estimated market size for novel antibacterial therapies
    job_creation_rate (float): The rate of job creation per dollar of market size (e.g. 0.01 for 1%)

    Returns:
    int: The estimated number of jobs created
    """
    return int(market_size * job_creation_rate)

def plot_healthcare_costs(years, healthcare_costs):
    """
    Plot the cumulative annual healthcare costs over time.

    Parameters:
    years (list): The years for which to plot the data
    healthcare_costs (list): The cumulative annual healthcare costs for each year
    """
    plt.plot(years, healthcare_costs)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Annual Healthcare Costs (billions USD)')
    plt.title('Cumulative Annual Healthcare Costs for Treating Drug-Resistant Bacterial Infections')
    plt.show()

def main():
    # Get population data from the World Bank API
    population_df = get_world_bank_data('SP.POP.TOTL', 'USA', 2010, 2030)
    population = population_df['value'].iloc[-1]

    # Example usage:
    resistance_rate = 0.2  # 20% antimicrobial resistance rate
    avg_treatment_cost = 10000  # average cost of treating a drug-resistant bacterial infection

    healthcare_costs = []
    years = list(range(2023, 2031))
    for year in years:
        healthcare_cost = calculate_healthcare_costs(resistance_rate, population, avg_treatment_cost)
        healthcare_costs.append(healthcare_cost)

    print(f"Cumulative annual healthcare costs: ${healthcare_costs[-1]:.2f} billion")

    # Plot the cumulative annual healthcare costs
    plot_healthcare_costs(years, healthcare_costs)

    initial_market_size = 1e9  # initial market size for novel antibacterial therapies (2023)
    growth_rate = 0.1  # 10% annual growth rate

    market_size = estimate_market_size(2030, growth_rate, initial_market_size)
    print(f"Estimated market size for novel antibacterial therapies in 2030: ${market_size:.2f} billion")

    job_creation_rate = 0.01  # 1% job creation rate per dollar of market size
    jobs_created = job_creation_estimate(market_size, job_creation_rate)
    print(f"Estimated number of jobs created in biotechnology and pharmaceutical industries: {jobs_created:,}")

if __name__ == "__main__":
    main()
