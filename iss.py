import requests
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import time


def track_iss():
    reply = requests.get("http://api.open-notify.org/iss-now.json")
    if reply.status_code == 200:
        data = reply.json()
        iss_pos = data["iss_position"]
        return iss_pos
    else:
        return None


def iss_map():
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()
    (line,) = plt.plot([], [], color="blue", marker="o")
    ax.set_title("Current position of the ISS")

    while True:
        iss_pos = track_iss()
        if iss_pos:
            lon = float(iss_pos["longitude"])
            lat = float(iss_pos["latitude"])
            line.set_data(lon, lat)
            plt.pause(1)  # Pause for 1 second to update the plot
            plt.draw()  # Redraw the plot
        else:
            print("Couldn't get information about the ISS position")
            break
    plt.show()


if __name__ == "__main__":
    iss_map()
