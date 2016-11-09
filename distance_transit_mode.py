from datetime import datetime, timedelta
from time import mktime
import csv


import googlemaps
import pandas as pd


import urllib, json
import pprint




def get_dist_matrix(points, ggmaps):
    matrix_range = len(points)

    dist_matrix_arr = [[0 for x in range(matrix_range)] for x in range(matrix_range)]
    try:
        for i in range(0, matrix_range):
            for j in range(0,i+1):
                if i == j:
                    dist_matrix_arr[i][j] = 0
                else:
                    result1 = ggmaps.distance_matrix(origins=points[i],destinations=points[j])
                    d = result1['rows'][0]['elements'][0]['distance']['value']
                    dist_matrix_arr[i][j] = d
                    dist_matrix_arr[j][i] = d
                    print ("T{0} , T{1}".format(i,j))
    except Exception as e:
        print ('Error in getting distance between %s and %s' % (points[i], points[j]))
    return dist_matrix_arr



def write_to_file(fname, jsn, transport_mode):

    x = json.loads(jsn)

    f = csv.writer(open(fname, "wb+"))

    # Write CSV Header, If you dont need that, remove this line
    if transport_mode == 'driving':
        f.writerow(["source", "destination", "time duration", "distance", "duration_in_traffic"])

        for origin in range(len(x['origin_addresses'])):
            for dest in range(len(x['destination_addresses'])):
                f.writerow([x['origin_addresses'][origin],
                            x['destination_addresses'][dest],
                            x['rows'][origin]['elements'][dest]['duration']['text'], # time
                            x['rows'][origin]['elements'][dest]['distance']['text'], # distance
                            x['rows'][origin]['elements'][dest]['duration_in_traffic']['text'] # duration_in_traffic
                ])
    else:
        f.writerow(["source", "destination", "time duration", "distance"])

        for origin in range(len(x['origin_addresses'])):
            for dest in range(len(x['destination_addresses'])):
                f.writerow([x['origin_addresses'][origin],
                            x['destination_addresses'][dest],
                            x['rows'][origin]['elements'][dest]['duration']['text'], # time
                            x['rows'][origin]['elements'][dest]['distance']['text'] # distance
                ])





if __name__ == '__main__':

    sources = [
        "258 Rhatigan Road East NW, Edmonton, AB T6R 2P7"
        ,"750 Leger Way NW, Edmonton, AB T6R 3H4"
        ,"5320 143 Street NW, Edmonton, AB"
        ,"1751 Towne Centre Blvd NW, Edmonton, AB T6R 3N9"
        ,"3250 132A Ave NW, Edmonton, AB T5A 3T1"
        ,"5911 19a Ave NW, Edmonton, AB T6L 4J8"
        ,"14830 118 Street NW, Edmonton, AB T5X 1T4"
    ]

    destinations=[
        "T6G2R3"
        ,"11762 106 St NW, Edmonton, AB T5G 3H6"
        ,"10535 108 St NW, Edmonton, AB T5H 2Z8"
        ,"104 Street & Jasper Avenue, Edmonton, AB"
        ,"11000 Stadium Rd, Edmonton, AB T5H 4E2"
        ,"7515 118 Ave NW, Edmonton, AB T5B 4X5"
        ,"11211 142 St, Edmonton, AB T5M 4A1"
        ,"16940 87 Ave NW, Edmonton, AB T5R 4H5"
    ]



    google_key = "AIzaSyBIrorNpUJ_RyaxZ-8PxC0ZXZ818hRc5hM"
    gmaps = googlemaps.Client(key=google_key)

    # convert_time_to_utc('sth')

    modes = ["driving", "walking", "bicycling", "transit"]

    input_date = "20160629"
    departures = ['0700', '1200', '1530' ]# the order is hours: 800, 1300, 1630 on May 18, 2016

    # during the summer because of daylight saving you need to subtract an hour from times

    utc_times = []
    for dep in departures:
        tmp = mktime(datetime.utctimetuple(
            datetime.strptime(input_date+'_'+dep,"%Y%m%d_%H%M")))
        utc_times.append(tmp)







    for mode in modes:

        result1 = gmaps.distance_matrix(origins=sources,destinations=destinations,
                                    mode=mode, departure_time=utc_times[0]) #hour 0800
        jsonResponse1 = json.dumps(result1, ensure_ascii=True)
        write_to_file('table1_'+mode+'.csv', jsonResponse1, mode)


        result2 = gmaps.distance_matrix(origins=destinations,destinations=sources,
                                    mode=mode, departure_time=utc_times[2]) # hour 1630
        jsonResponse1 = json.dumps(result2, ensure_ascii=True)
        write_to_file('table2_'+mode+'.csv', jsonResponse1, mode)


        result3A = gmaps.distance_matrix(origins=sources,destinations=destinations,
                                    mode=mode, departure_time=utc_times[1]) # hour 1300
        jsonResponse1 = json.dumps(result3A, ensure_ascii=True)
        write_to_file('table3A_'+mode+'.csv', jsonResponse1, mode)


        result3B = gmaps.distance_matrix(origins=destinations,destinations=sources,
                                    mode=mode, departure_time=utc_times[1]) # hour 1300
        jsonResponse1 = json.dumps(result3B, ensure_ascii=True)
        write_to_file('table3B_'+mode+'.csv', jsonResponse1, mode)



print ("end of process")




"""
        with open('table1_'+mode+'.txt', 'w') as outfile:
            outfile.write(jsonResponse1+'\n')
        with open('table2_'+mode+'.txt', 'w') as outfile:
            outfile.write(jsonResponse2+'\n')
        with open('table3A_'+mode+'.txt', 'w') as outfile:
            outfile.write(jsonResponse3A+'\n')
        with open('table3B_'+mode+'.txt', 'w') as outfile:
            outfile.write(jsonResponse3B+'\n')

"""


