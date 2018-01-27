# coding: utf8
import utils
import download_regions_champ as dr
import json

OUTPUT_PATH = utils.OUTPUT_PATH + 'regions_champs'
REGIONS_CHAMPS_KEY = 'general_information_url'

def main():
  links = json.load(open(utils.LINKS_JSON_PATH, 'r'))
  for year in links:
    if REGIONS_CHAMPS_KEY in links[year]:
      dr.download_regions_champions_data(links[year][REGIONS_CHAMPS_KEY], '%s/%s.csv' % (OUTPUT_PATH, year))
    else:
      print "Ignoring %s because the general information url doesn't exist :(" % year

if __name__ == '__main__':
  main()
