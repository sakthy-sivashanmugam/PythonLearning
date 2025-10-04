import matplotlib.pyplot as plt
import pandas as pd

from covid_case_status import CovidCaseStatus

class CovidVisualization(CovidCaseStatus):

    """
    COVID-19 data visualization and exploratory data analysis.
    """

    def bar_top10_confirmed(self):
        """
        Bar Chart of Top 10 Countries by Confirmed Cases.
        """
        top10 = self.df.nlargest(10, 'Confirmed')
        #plt.figure(figsize=(10,6))
        plt.bar(top10['Country/Region'], top10['Confirmed'], color='orange')
        plt.title("Top 10 Countries by Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.show()

    def pie_deaths_by_region(self):
        """
        Pie Chart of Global Death Distribution by Region.
        """
        region_deaths = self.df.groupby("WHO Region")['Deaths'].sum()
        #plt.figure(figsize=(8,8))
        plt.pie(region_deaths, labels=region_deaths.index, autopct="%1.1f%%", startangle=140)
        plt.title("Global Death Distribution by Region")
        plt.show()

    def line_confirmed_vs_deaths_top5(self):
        """
        Line Chart comparing Confirmed and Deaths for Top 5 Countries.
    
     """
        top5 = self.df.nlargest(5, 'Confirmed')

        plt.figure(figsize=(10,6))

        # Plot confirmed and deaths side by side for each country
        plt.plot(top5['Country/Region'], top5['Confirmed'], marker='o', label="Confirmed")
        plt.plot(top5['Country/Region'], top5['Deaths'], marker='x', linestyle='--', label="Deaths")

        plt.title("Confirmed vs Deaths for Top 5 Countries")
        plt.xlabel("Country")
        plt.ylabel("Cases")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def scatter_confirmed_vs_recovered(self):
        """
        Scatter Plot of Confirmed Cases vs Recovered Cases.
        """
        plt.figure(figsize=(8,6))
        plt.scatter(self.df['Confirmed'], self.df['Recovered'], alpha=0.6, c='green')
        plt.title("Confirmed vs Recovered Cases")
        plt.xlabel("Confirmed")
        plt.ylabel("Recovered")
        plt.show()

    def histogram_death_counts(self):
        """
        Histogram of Death Counts across all Regions.
        """
        plt.figure(figsize=(10,6))
        plt.hist(self.df['Deaths'], bins=30, color='red', alpha=0.7)
        plt.title("Distribution of Death Counts")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.show()

    def stacked_bar_selected_countries(self, countries):
        """
        Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries.
        """
        data = self.df[self.df['Country/Region'].isin(countries)]
        data_grouped = data.groupby("Country/Region")[['Confirmed','Deaths','Recovered']].sum()

        data_grouped.plot(kind="bar", stacked=True, figsize=(10,6))
        plt.title("COVID Cases by Country (Stacked)")
        plt.ylabel("Counts")
        plt.show()

    def boxplot_confirmed_by_region(self):
        """
        Box Plot of Confirmed Cases across Regions.
        """
        region_confirmed = [group['Confirmed'].values for _, group in self.df.groupby("WHO Region")]
        plt.figure(figsize=(10,6))
        plt.boxplot(region_confirmed, labels=self.df['WHO Region'].unique())
        plt.title("Box Plot of Confirmed Cases by Region")
        plt.ylabel("Confirmed Cases")
        plt.xticks(rotation=45)
        plt.show()

    def trendline_india_vs_country(self, other_country):
        """
        Trend Line: Plot Confirmed cases for India vs another chosen country.
        """
        india = self.df[self.df['Country/Region'] == "India"]
        other = self.df[self.df['Country/Region'] == other_country]

        plt.figure(figsize=(10,6))
        plt.plot(india['Confirmed'].values, label="India", color='blue')
        plt.plot(other['Confirmed'].values, label=other_country, color='orange')
        plt.title(f"Trend: India vs {other_country}")
        plt.xlabel("Index (Time)")
        plt.ylabel("Confirmed Cases")
        plt.legend()
        plt.show()