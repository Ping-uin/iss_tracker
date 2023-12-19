import requests
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def track_iss():
    reply = requests.get("http://api.open-notify.org/iss-now.json")
    if reply.status_code == 200:
        data = reply.json()
        iss_pos = data["iss_position"]
        return iss_pos
    else:
        return None
    
def iss_map():
    iss_pos = track_iss()
    if iss_pos:
        lon = float(iss_pos['longitude'])
        lat = float(iss_pos['latitude'])
        
        fig = plt.figure(figsize=(8, 8))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.stock_img()
        # ax.plot(lon, lat, 'ro', markersize=10, transform=ccrs.PlateCarree()) 
        plt.plot(lon, lat, color='blue', marker='o')
        # ax.coastlines()
        # ax.gridlines(draw_labels=False)
        ax.set_title("Current position of the ISS")
        plt.show() 
        
    else:
        print("Couldn't get information about the ISS position")

if __name__ == "__main__":
    iss_map()
