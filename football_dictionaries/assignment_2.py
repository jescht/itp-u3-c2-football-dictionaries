from .assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    gk_list=[]
    df_list=[]
    mf_list=[]
    fw_list=[]
    list_of_players=players_as_dictionaries(squads_list)
    for eachplayer in list_of_players:
        if eachplayer['position']=='GK':
            gk_list.append(eachplayer)
        elif eachplayer['position']=='DF': 
            df_list.append(eachplayer)
        elif eachplayer['position']=='MF':
            mf_list.append(eachplayer)
        elif eachplayer['position']=='FW':
            fw_list.append(eachplayer)
            
    positions={}
    #If list is not empty, add list to the positions dictionary. 
    if gk_list:                            
      positions['GK']=gk_list
    if df_list: 
      positions['DF']=df_list
    if mf_list:
      positions['MF']=mf_list
    if fw_list:
      positions['FW']=fw_list
    return positions
 