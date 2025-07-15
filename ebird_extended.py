import os
from ebird.api import (
    get_observations,
    get_nearby_observations,
    get_species_observations,
    get_nearby_species,
    get_notable_observations,
    get_nearby_notable,
    get_top_100,
    get_totals,
    get_taxonomy,
    get_taxonomy_forms,
    get_visits,
    get_checklist,
    get_hotspots,
    get_nearby_hotspots,
    get_hotspot,
    get_regions,
    get_adjacent_regions,
    get_region,
    )

api_key = os.getenv("EBIRD_API_KEY")

def observations_by_region(region_code, back=7, detail="simple"):
    return get_observations(api_key, region_code, back=back, detail=detail)

def nearby_observations(lat, lng, dist=10, back=7):
    return get_nearby_observations(api_key, lat, lng, dist=dist, back=back)

def observations_for_species(species_code, region_code, back=30):
    return get_species_observations(api_key, species_code, region_code, back=back)

def nearby_species_observations(species_code, lat, lng, back=7):
    return get_nearby_species(api_key, species_code, lat, lng, back=back)

def notable_in_region(region_code):
    return get_notable_observations(api_key, region_code)

def nearby_notable(lat, lng, dist=50):
    return get_nearby_notable(api_key, lat, lng, dist=dist)

def checklist_visits(region_code, date=None):
    return get_visits(api_key, region_code, date=date)

def checklist_detail(checklist_id):
    return get_checklist(api_key, checklist_id)

def get_region_hotspots(region_code, back=None):
    return get_hotspots(api_key, region_code, back=back)

def get_nearby_hotspots(lat, lng, dist=50):
    return get_nearby_hotspots(api_key, lat, lng, dist=dist)

def get_hotspot_info(loc_id):
    return get_hotspot(api_key, loc_id)

def get_country_list():
    return get_regions(api_key, "country", "world")

def get_states(country_code="US"):
    return get_regions(api_key, "subnational1", country_code)

def get_counties(state_code):
    return get_regions(api_key, "subnational2", state_code)

def get_adjacent(state_code):
    return get_adjacent_regions(api_key, state_code)

def get_region_bounds(region_code):
    return get_region(api_key, region_code)

def get_taxonomy_all(locale=None):
    return get_taxonomy(api_key, locale=locale)

def get_species_taxonomy(species_code):
    return get_taxonomy(api_key, species=species_code)

def get_species_forms(species_code):
    return get_taxonomy_forms(api_key, species_code)

def get_taxonomy_versions():
    return get_taxonomy_versions(api_key)

def get_region_top_100(region_code, date):
    return get_top_100(api_key, region_code, date)

def get_region_totals(region_code, for_date):
    return get_totals(api_key, region_code, for_date)