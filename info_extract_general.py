import urllib.request
# Bus Page links to be read is given as input
bus_page_links = open("GenBusLinks.txt","r")
for page_links in bus_page_links:
    # Open link and Page Source
    page_links = page_links.strip()
    response = urllib.request.urlopen(page_links)
    page_source = response.read()
    page_main_temp_w = open("page_main_temp.txt","w")
    page_source = str(page_source)
    page_main_temp_w.write(page_source)
    page_main_temp_w.close()

    # Rewrite Page Source into readable form
    page_main_temp_r = open("page_main_temp.txt","r")
    page_main_w = open("page_main.txt","w")

    for lines in page_main_temp_r:
        lines = lines.strip()
        page_lines = lines.split("\\n")

    for i in range(1,len(page_lines)):
        page_main_w.write(page_lines[i])
        page_main_w.write("\n")

    page_main_temp_r.close()
    page_main_w.close()

    # Extract Route links from Page Source
    page_main_r = open("page_main.txt","r")
    links = open("links.txt","w")
    for lines in page_main_r:
        if(lines.find("Route NO:")>=0):
            lines_split = lines.split("\\'")
            if(lines_split[13].find("http")>=0):
                links.write(lines_split[13])
            else:
                links.write(lines_split[11])                
            lines_split = lines_split[2].split("</b>")
            lines_split = lines_split[1].split("</p>")
            links.write(lines_split[0])        
            links.write('\n')
    page_main_r.close()
    links.close()

    # Parse route links to extract bus stops
    links = open("links.txt","r")
    for lines in links:
        lines = lines.split()
        # Read page Source
        response = urllib.request.urlopen(lines[0])
        route = lines[1]
        page_source = response.read()
        page_temp_w = open("page_temp.txt","w")
        page_source = str(page_source)
        page_temp_w.write(page_source)
        page_temp_w.close()
        page_temp_r = open("page_temp.txt","r")
        page_w = open("page.txt","w")

        #Rewrite page source 
        for lines in page_temp_r:
            lines = lines.strip()
            page_lines = lines.split("\\n")

        for i in range(1,len(page_lines)):
            page_w.write(page_lines[i])
            page_w.write("\n")

        page_temp_r.close()
        page_w.close()

        # List all bus stops for a particular route
        page_r = open("page.txt","r")
        busstops = open("BusStops_Gen.txt","a")
        busstops.write("Route = ")
        busstops.write(route)
        busstops.write("\n")    
        for stops in page_r:
            if(stops.find("bulletlist.png")>=0):
                stops = stops.split("</span>")
                for i in range(0,len(stops)-1):
                    stop_name = stops[i].split("busstop_name\\'>")           
                    busstops.write(stop_name[1])
                    busstops.write("\n")
        busstops.write("\n\n\n") 
        page_r.close()
        busstops.close()
bus_page_links.close()
