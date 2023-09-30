from fetch_data import get_data
from generate_hash import generate_hash
from database import add, add_tracking_data
from dump_json import dump_json

def load_json():

    # load and return json data
    return get_data()
    
def create_key(
    country,
):
       
    # generate a 3-character hash key + country name seperated by a '-' character
    return generate_hash(4)[:3]+'-'+country

def extract_row(data):

    # extract all keys from 1 dictionary entry
    continent = data['continent']
    country = data['country']
    population = data['population']
    new_cases = data['cases']['new']
    active_cases = data['cases']['active']
    critical_cases = data['cases']['critical']
    recovered = data['cases']['recovered']
    recovered_1m_pop = data['cases']['1M_pop']
    recovered_total = data['cases']['total']
    new_deaths = data['deaths']['new']
    deaths_1m_pop = data['deaths']['1M_pop']
    deaths_total = data['deaths']['total']
    tests_1m_pop = data['tests']['1M_pop']
    tests_total = data['tests']['total']
    date_time = data['time']
    id = create_key(country)

    # return extracted keys
    return {
        "id":id,
        "continent":continent,
        "country":country,
        "population":population,
        "new_cases":new_cases,
        "new_deaths":new_deaths,
        "active_cases":active_cases,
        "critical_cases":critical_cases,
        "recovered":recovered,
        "recovered_1m_pop":recovered_1m_pop,
        "recovered_total":recovered_total,
        "deaths_1m_pop":deaths_1m_pop,
        "deaths_total":deaths_total,
        "tests_1m_pop":tests_1m_pop,
        "tests_total":tests_total,
        "date_time":date_time
    }

def process_json(
  raw_json
):
  
  filename,time_extracted = dump_json(raw_json)
  for dict in raw_json['response']:
    data = extract_row(dict)
    add(
        data["id"],
        data["continent"],
        data["country"],
        data["population"],
        data["new_cases"],
        data["new_deaths"],
        data["active_cases"],
        data["critical_cases"],
        data["recovered"],
        data["recovered_1m_pop"],
        data["recovered_total"],
        data["deaths_1m_pop"],
        data["deaths_total"],
        data["tests_1m_pop"],
        data["tests_total"],
        data["date_time"],
        time_extracted
    )


def extract_tracking_data(raw_json):
   
   # get filename
   filename = dump_json()

   # get hash id of json
   id = filename[-3:]

   # processed is 1 by default, as sqlite does not have a default boolean datatype
   # we opt to take 1 as True and 0 as False
   processed = 1

   # extract datetime of json
   time_processed = filename[:10]

   # return extracted keys
   return [
      id,
      processed,
      time_processed
   ]

def process_tracking_data(
      raw_json
):
   
   # extract tracking data from filename of json
   data = extract_tracking_data(raw_json)

   # insert into json_log table in database
   add_tracking_data(
      data[0],
      data[1],
      data[2]
   )

process_json(get_data())

    