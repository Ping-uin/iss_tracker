# ISS Tracker
Just a small side project in python I was interested in
## How it works
- Using the iss-now API "http://api.open-notify.org/iss-now.json"
- Using mathplotlib and cartopy to display the current position on a world map
- Periodically updated

## Bugs
- The window close doen't close the program successfully anymore; worked without updating the plot in earlier versions
- new window opens after updating the plot but it's empty for some reason
- CTRL + C in terminal needed to fully close the program
