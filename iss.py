import requests
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import time

close_state = False


def track_iss():
    reply = requests.get("http://api.open-notify.org/iss-now.json")
    if reply.status_code == 200:
        data = reply.json()
        iss_pos = data["iss_position"]
        return iss_pos
    else:
        return None


def on_close(event):
    global close_state
    close_state = True


def iss_map():
    global close_state
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()
    (line,) = plt.plot([], [], color="blue", marker="o")
    ax.set_title("Current position of the ISS")
    # fig.show()
    close_state = False

    while True:
        if close_state:
            break
        iss_pos = track_iss()
        if iss_pos:
            lon = float(iss_pos["longitude"])
            lat = float(iss_pos["latitude"])
            line.set_data(lon, lat)
            plt.pause(1)  # Pause for 1 second to update the plot
            plt.draw()  # Redraw the plot
            fig.canvas.mpl_connect("close_event", on_close)
        else:
            print("Couldn't get information about the ISS position")
            break
    # plt.show()


if __name__ == "__main__":
    iss_map()
