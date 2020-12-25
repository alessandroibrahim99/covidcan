
import pandas as pd

df_cases1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")
df_deaths1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", sep=",")
dtf_cases = df_cases1.loc[df_cases1['Country/Region']== 'Canada']
dtf_cases = dtf_cases.loc[dtf_cases['Province/State']!= 'Diamond Princess']
dtf_cases = dtf_cases.loc[dtf_cases['Province/State']!= 'Grand Princess']
dtf_cases = dtf_cases.loc[dtf_cases['Province/State']!= 'Repatriated Travellers']
dtf_deaths = df_deaths1.loc[df_deaths1['Country/Region']== 'Canada']

class Data():
    
    def get_data(self):
        #self.dtf_cases = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")
        #self.dtf_deaths = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", sep=",")
        self.dtf_cases = dtf_cases
        self.dtf_deaths = dtf_deaths
        #self.countrylist = ["World"] + self.dtf_cases["Country/Region"].unique().tolist()
        self.countrylist = ["Canada"] + self.dtf_cases["Province/State"].unique().tolist()

    
    @staticmethod
    def group_by_country(dtf, country):
        #dtf = dtf.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T
        dtf = dtf.drop(['Country/Region','Lat','Long'], axis=1).groupby("Province/State").sum().T
        #dtf["World"] = dtf.sum(axis=1)
        dtf["Canada"] = dtf.sum(axis=1)
        dtf = dtf[country]
        dtf.index = pd.to_datetime(dtf.index, infer_datetime_format=True)
        ts = pd.DataFrame(index=dtf.index, data=dtf.values, columns=["data"])
        return ts
    
    @staticmethod
    def calculate_mortality(ts_deaths, ts_cases):
        last_deaths = ts_deaths["data"].iloc[-1]
        last_cases = ts_cases["data"].iloc[-1]
        mortality = last_deaths / last_cases
        return mortality
    
    
    def process_data(self, country):
        self.dtf = self.group_by_country(self.dtf_cases, country)
        deaths = self.group_by_country(self.dtf_deaths, country)
        self.dtf["deaths"] = deaths
        self.mortality = self.calculate_mortality(deaths, self.dtf)
