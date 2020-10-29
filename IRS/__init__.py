import datetime
import logging
import json
from pymongo import MongoClient, TEXT
from .irs_scraper import start
import azure.functions as func

def main(mytimer: func.TimerRequest, context: func.Context) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    with open(context.function_directory + '\config.json', 'r') as con:
        config = json.load(con)

    start(config, 'tmpIRS2') 

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function for IRS Scraping ran at utc: %s', utc_timestamp)