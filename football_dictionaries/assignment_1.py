def players_as_dictionaries(squads_list):
    new_list=[]
    for player in squads_list:
        new_dict= {}
        new_dict['number']=player[0]
        new_dict['position']=player[1]
        new_dict['name']=player[2]
        new_dict['date_of_birth']=player[3]
        new_dict['caps']=player[4]
        new_dict['club']=player[5]
        new_dict['country']=player[6]
        new_dict['club_country']=player[7]
        new_dict['year']=player[8]
        new_list.append(new_dict)
    return new_list

