import pandas as pd
from prophet import Prophet

def load_data(file_path):
    """
    Load time series data from a CSV file
    """
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    return data

def prepare_data(data):
    """
    Prepare data for Prophet forecasting
    """
    data.reset_index(inplace=True)
    data.rename(columns={'date': 'ds', 'value': 'y'}, inplace=True)
    return data

def create_prophet_model(data):
    """
    Create a Prophet model
    """
    model = Prophet()
    model.fit(data)
    return model

def make_forecast(model, periods):
    """
    Make a forecast for a specified number of periods
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def plot_forecast(model, forecast):
    """
    Plot the forecast
    """
    model.plot(forecast)
    plt.show()

def main():
    # Load data
    file_path = 'data.csv'
    data = load_data(file_path)
    
    # Prepare data
    data = prepare_data(data)
    
    # Create Prophet model
    model = create_prophet_model(data)
    
    # Make forecast
    periods = 30
    forecast = make_forecast(model, periods)
    
    # Plot forecast
    plot_forecast(model, forecast)

if __name__ == "__main__":
    main()
