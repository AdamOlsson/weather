# How to run
Use "crontab -e" to create a cron job to fetch weather data using "python3 get_weather_data.py". Once the cron job is running, start the nodejs server using "node server.js". Finally, using the command line open the index.html file using the browser.

The cron job needs to be started separately but the browser can be started using the start.sh script. You need to manually make sure that the browser is zoomed to 100% and that the nodejs server is running.