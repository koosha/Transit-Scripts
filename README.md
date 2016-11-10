# Transit-Scripts

@Parameters

modes = ["driving", "walking", "bicycling", "transit"]
departures = []# hours 8:00, 13:00, 16:30 on June 29, 2016

csv_columns = ["source", "destination", "time duration", "distance", "duration_in_traffic"] # note duration in traffic is only available for driving mode


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


@results
table1 = (origins=sources,destinations=destinations,mode=mode, departure_time=0800)
table2 = (origins=destinations,destinations=sources,mode=mode, departure_time=1630)
table3A = (origins=sources,destinations=destinations,mode=mode, departure_time=1300)
result3B = (origins=destinations,destinations=origins,mode=mode, departure_time=1300)



