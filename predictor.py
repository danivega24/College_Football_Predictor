import unittest
import os
import csv

def cfb1_setup(f13):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f13)

    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = []
        for row in r:
            rows.append(row)
    
    header = rows[0]

    data = {}
    team_names = []

    for team in rows[1:]:
        data[team[0]] = {}
        team_names.append(team[0])
        for i in range(1, len(header)):
            data[team[0]][header[i]] = team[i]
    
    return (data, team_names)

def cfb2_setup(f13):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f13)

    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = []
        for row in r:
            rows.append(row)
    
    header = rows[0]
    data = {}
    team_names = []

    for team in rows[1:]:
        data[team[1]] = {}
        team_names.append(team[1])
        for i in range(2, len(header)): 
            data[team[1]][header[i]] = team[i]
    
    return(data, team_names)

def cfb3_setup(f13):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f13)

    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = []
        for row in r:
            rows.append(row)
    
    header = rows[0]
    data = {}
    team_names = []

    for team in rows[1:]:
        data[team[2]] = {}
        team_names.append(team[1])
        for i in range(1, len(header)): 
            if i == 2:
                continue
            data[team[2]][header[i]] = team[i]
    
    return(data, team_names)
def main():

    all_data = {}

    f13 = 'cfb13.csv'
    f14 = 'cfb14.csv'
    f15 = 'cfb15.csv'
    f16 = 'cfb16.csv'
    f17 = 'cfb17.csv'
    f18 = 'cfb18.csv'
    f19 = 'cfb19.csv'
    f20 = 'cfb20.csv'
    f21 = 'cfb21.csv'
    f22 = 'cfb22.csv'


    all_data['13'] = cfb1_setup(f13)[0]
    all_data['14'] = cfb1_setup(f14)[0]
    all_data['15'] = cfb1_setup(f15)[0]
    all_data['16'] = cfb1_setup(f16)[0]
    all_data['17'] = cfb1_setup(f17)[0]
    all_data['18'] = cfb1_setup(f18)[0]
    all_data['19'] = cfb1_setup(f19)[0]
    all_data['20'] = cfb1_setup(f20)[0]

    all_data['21'] = cfb2_setup(f21)[0]
    all_data['22'] = cfb3_setup(f22)[0]

    #print(    "--------------- 2021 ---------------\n\n", all_data['21'])
    print("\n\n--------------- 2022 ---------------\n\n", all_data['22'])


    print("\n\n-----------------AKRON STATS-----------------\n\n")
    print(all_data['21']['Akron (MAC)'])
    print("\n\n-----------------MICHIGAN STATS-----------------\n\n")
    print(all_data['22']['Michigan (Big Ten)']['Def Rank'])


main()

