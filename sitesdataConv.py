import json

sitesdataConv = []

with open('sites.csv','r') as fi:
    for i, line in enumerate(fi):
        if i > 0:
            v = line.strip().split('\t')
            USAF = v[0]
            station_name = v[1]
            country_name = v[2]
            lat = float(v[3])
            lon = float(v[4])
            elev = float(v[5])

            sitesdataConv.append({
                    "ID": USAF,
                    "station_name": station_name,
                    "country_name": country_name,
                    "lon": lon,
                    "lat": lat,
                    "temps": {}
                })


for i in range(1,260):
    sitenum = -1
    with open('siteTemps/sitesTemps' + str(i) + '.csv','r') as fi:
        for j, line in enumerate(fi):
            if j > 0:
                if j == 1:
                    siteID = line.strip().split('\t')[0]
                    for k, s in enumerate(sitesdataConv):
                        if s["ID"] == siteID:
                            sitenum = k
                if sitenum > -1:
                    v = line.strip().split('\t')
                    ym = v[1] + "-" + v[2]
                    sitesdataConv[sitenum]["temps"][ym] = {
                            "ave": float(v[3]) / 10.0,
                            "max": float(v[4]) / 10.0,
                            "min": float(v[5]) / 10.0
                        }

with open('sites.json','w') as fo:
    fo.write(json.dumps(sitesdataConv))

