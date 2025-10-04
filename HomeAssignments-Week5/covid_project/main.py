from data_loader import DataLoader
from covid_case_status import CovidCaseStatus
from covid_visualization import CovidVisualization

def main():
    path = 'country_wise_latest.csv'

    loader = DataLoader(path)
    data = loader.load_data()
    #print(data.head())

    stats = CovidCaseStatus(data)
    
    # 1. Summarize by region
    print("---- Summary by Region ----")
    summary = stats.summarize_cases_by_region()
    print(summary)
        
    # 2. Filter records with confirmed cases < 10
    print("\n---- Filtered Records (Confirmed Cases >= 10) ----")
    filtered_data = stats.filter_low_case_records(threshold=10)
    print(filtered_data)

    # 3. Region with highest confirmed cases
    print("\n---- Region with Highest Confirmed Cases ----")
    region, cases = stats.region_highest_confirmed()
    print(f"Region: {region}, Confirmed Cases: {cases}")

    # 4. Sort by confirmed cases and save to CSV
    print("\n---- Sorted by Confirmed Cases ----")
    sorted_data = stats.sort_by_confirmed_cases()
    print(sorted_data)

    # 5. Top 5 countries with highest confirmed cases
    print("\n---- Top 5 Countries by Confirmed Cases ----")
    top_countries = stats.top_countries_by_cases(n=5)
    print(top_countries)

    # 6. Region with lowest deaths
    print("\n---- Region with Lowest Deaths ----")
    region, deaths = stats.region_lowest_deaths()
    print(f"Region: {region}, Deaths: {deaths}")

    # 7. Country case summary
    country_name = 'India' 
    print(f"\n---- Case Summary for {country_name} ----")

    summary = stats.country_case_summary(country_name=country_name)
    print(summary)

    # 8. Mortality rate by country
    print("\n---- Mortality Rate by Region ----")   
    mortality_rate = stats.mortality_rate_by_region()
    print(mortality_rate)

    # 9. Recovered rate by country
    print("\n---- Recovered Rate by Region ----")
    recovered_rate = stats.recovery_rate_by_region()
    print(recovered_rate)

    # 10. Group by Country/Region and summarize
    print("\n---- Grouped Summary by Country/Region ----")
    summary = stats.group_by_country_region()
    print(summary)
    
    # 11. Group by zero recovered cases
    print("\n---- Countries with Zero Recovered Cases ----")    
    zero_recovered = stats.regions_zero_recovery()
    print(zero_recovered)

    # Visualization
    viz = CovidVisualization(data)
    viz.bar_top10_confirmed()
    viz.pie_deaths_by_region()
    viz.line_confirmed_vs_deaths_top5()
    viz.scatter_confirmed_vs_recovered()
    viz.histogram_death_counts()
    viz.stacked_bar_selected_countries(['India', 'Australia', 'Brazil', 'Russia', 'China'])
    viz.boxplot_confirmed_by_region()
    viz.trendline_india_vs_country('USA')





if __name__ == "__main__":
    main()