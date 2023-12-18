from algoliasearch.search_client import SearchClient

client = SearchClient.create('0ID4OD4XQ9', '')
index = client.init_index('restaurantINFO')


index.set_settings({
    "searchableAttributes": ["name", "address", "dining_style"],
    "customRanking": ["desc(reviews_count)"],
    'attributesForFaceting': [
        'filterOnly(price_range)',
        'filterOnly(stars_count)',
        'filterOnly(food_type)',
        'searchable(city)',
        'searchable(country)'
    ]
})

query = "restaurant"
filters = "available = 1 AND (food_type:French) AND stars_count > 3.5"

result_search = index.search('query', {
    'filters': filters
})
result_facet = index.search_for_facet_values('city', 'New York')
result_geo = index.search('query', {
    'aroundLatLng': '48.84, -2.38'
})

print(result_search)
print(result_facet)
print(result_geo)
