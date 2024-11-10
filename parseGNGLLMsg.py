def parse_gnrmc_line(line):
    parts = line.split(',')
    if len(parts) < 6:
        return None, None
    
    # Latitude
    lat_raw = parts[3]
    lat_deg = float(lat_raw[:2])
    lat_min = float(lat_raw[2:])
    lat = lat_deg + (lat_min / 60.0)
    if parts[4] == 'S':
        lat = -lat
    
    # Longitude
    lon_raw = parts[5]
    lon_deg = float(lon_raw[:3])
    lon_min = float(lon_raw[3:])
    lon = lon_deg + (lon_min / 60.0)
    if parts[6] == 'W':
        lon = -lon
    
    return lat, lon

def extract_coordinates(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            if '$GNRMC' in line:
                timestamp = line.split()[0]  # Extract timestamp from the beginning of the line
                lat, lon = parse_gnrmc_line(line)
                if lat is not None and lon is not None:
                    outfile.write(f"{timestamp}: Latitude: {lat}, Longitude: {lon}\n")

# Example usage
extract_coordinates('BASESTATION2.txt', 'parsed2.txt')