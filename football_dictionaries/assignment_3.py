from .assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
  players_dict = {} # empty dict
  for eachplayer in players_as_dictionaries(squads_list):
    country=eachplayer['country']
    position=eachplayer['position']
    # create empty dict for each country
    countries = players_dict.get(country, None) 
    if countries == None:
      players_dict[country]= {}
    # create empty list for each position within each country
    positions = players_dict[country].get(position, None) 
    if positions == None:
      players_dict[country][position] = []
    players_dict[country][position].append(eachplayer)
  return players_dict 