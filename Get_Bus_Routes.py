all_stops = open("all_stops.txt","w")
with open('BusStops_AC.txt') as f:
    stop_list = [1000]
    stop_list[0] = 'Kempegowda Bus Station'
    all_stops.write(stop_list[0])
    all_stops.write("\n")
    for flines in f:
        flines = flines.strip()
        if (flines.find('Route =') < 0):
            list_stop = 0
            if(flines.find("(") >= 0):
                flines = flines.split("(")
                flines = flines[0].strip()
            if(flines.find(",") >= 0):
                flines = flines.split(",")
                flines = flines[0].strip()              
            for i in range(0,len(stop_list)):
                if(stop_list[i] == flines):
                    list_stop = 1
            if((list_stop == 0)and(flines != "")):
               all_stops.write(flines)
               all_stops.write("\n")              
               stop_list.append(flines)
all_stops.close()

all_stops = open("all_stops.txt","r")
stops_routes = open("stops_routes.txt","w")
for stops in all_stops:
    bus_stops = open("BusStops_AC.txt","r")
    stops = stops.strip()
    stops_routes.write(stops)
    stops_routes.write(" : ")
    for flines in bus_stops:
        if(flines.find("Route =") >= 0):
            flines = flines.split("=")
            route = flines[1]
            route = route.strip()
        else:
            if(flines.find(stops) >= 0):
                stops_routes.write(route) 
                stops_routes.write(", ")
    stops_routes.write("\n")
    bus_stops.close()
all_stops.close()
stops_routes.close()
        
        
    


                                           
            
