import numpy as np
import pandas as pd

class CovidCaseStatus:
    """
    Base Class- Analysing COVID-19 case status data.
    """
    def __init__(self, df):
        self.df = df

    def summarize_cases_by_region(self):
        """
        Summarizes total confirmed, deaths, and recovered cases by region.
        """
        summary = self.df.groupby(["WHO Region"])[['Confirmed', 'Deaths', 'Recovered']].sum()
             
        return summary
    
    def filter_low_case_records(self, threshold):
        """
        Exclude entries where confirmed cases are < 10
        """
        filtered_df = self.df[self.df['Confirmed'] >= threshold]
        return filtered_df
    
    def region_highest_confirmed(self):
        """
        Identify the region with the highest number of confirmed cases.
        """
        region_cases = self.df.groupby(["WHO Region"])['Confirmed'].sum()
        max_region = region_cases.idxmax()
        max_value = region_cases.max()
        return max_region, max_value

    def sort_by_confirmed_cases(self):
        """
        Sort the data by confirmed cases in descending order and save it to csv file.
        """
        sorted_cases = self.df.sort_values(by='Confirmed', ascending=False)

        sorted_cases.to_csv('sorted_covid_cases.csv', index=False)
        return sorted_cases
    
    def top_countries_by_cases(self, n):
        """
        Get top N countries with the highest confirmed cases.
        """
        top_countries = self.df[['Country/Region', 'Confirmed']].sort_values(by='Confirmed', ascending=False).head(n)
        return top_countries
    
    def region_lowest_deaths(self):
        """
        Identify the region with the lowest number of deaths.
        """
        region_deaths = self.df.groupby(["WHO Region"])['Deaths'].sum()
        min_region = region_deaths.idxmin()
        min_value = region_deaths.min()
        return min_region, min_value

    def country_case_summary(self,country_name='default'):
        """
        Summarizes total confirmed, deaths, and recovered cases by country.
        """
        country_summary = self.df[self.df['Country/Region'] == country_name]
        return country_summary[['Confirmed', 'Deaths', 'Recovered']]
    
    def mortality_rate_by_region(self):
        """
        Calculate mortality rate (deaths/confirmed) by region.
        """
        region_summary = self.df.groupby("WHO Region")[['Confirmed', 'Deaths']].sum()
        region_summary['Mortality Rate'] = (region_summary['Deaths'] / region_summary['Confirmed']) * 100
        return region_summary[['Mortality Rate']]
    
    def recovery_rate_by_region(self):
        """
        Calculate recovery rate (recovered/confirmed) by region.
        """
        region_summary = self.df.groupby("WHO Region")[['Confirmed', 'Recovered']].sum()
        region_summary['Recovery Rate'] = (region_summary['Recovered'] / region_summary['Confirmed']) * 100
        return region_summary[['Recovery Rate']]
    
    def group_by_country_region(self):
        """
        Group data by country and region.
        """
        grouped = self.df.groupby(['WHO Region', 'Country/Region'])[['Confirmed', 'Deaths', 'Recovered']].sum()
        return grouped
          
    def regions_zero_recovery(self):
        """
        Identify regions with zero recovered cases.
        """
        region_summary = self.df.groupby("WHO Region")[['Recovered']].sum()
        zero_recovery_regions = region_summary[region_summary== 0].index.tolist()
        return zero_recovery_regions