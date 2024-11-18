
continent_countries_dict = {
    'Africa': ['Nigeria', 'Kenya', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['Germany', 'France', 'Italy'],
    'North America': ['USA', 'Canada', 'Mexico'],
    'South America': ['Brazil', 'Argentina', 'Colombia'],
    'Oceania': ['Australia', 'New Zealand', 'Fiji']
}


print("Entire dictionary:", continent_countries_dict)


fourth_continent_countries = list(continent_countries_dict.items())[3]
print("Countries of the 4th continent:", fourth_continent_countries)


continent_countries_dict['South America'] = ['Chile', 'Peru', 'Ecuador']


del continent_countries_dict['Oceania']


last_continent_countries = list(continent_countries_dict.items())[-1]
print("Last key-value pair:", last_continent_countries)
