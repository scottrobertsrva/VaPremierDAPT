Scott Roberts
DAPT 2019 - VaPremier Project

Notes:

Flu Season Exp Visualization tool is hosted on AWS
http://http://54.152.92.119

contact robertssd@vcu.edu for login info

Folder: PythonScripts
    - Contains it's own ReadMe 

Folder VaPremier:
    - Top Level Settings and Configurations for Flu Season Django App

Folder vpApp:
    - urls.py -> url routing for App
    - views.py -> main controller functions
    - models.py -> models for flu data

Folder vpApp/static/vpApp
    - static js and css used in site
    - siteScript.js -> Main javascript file with d3 code to generate map

Folder vpApp//templates/vpApp
    - base_generic.html -> main html
    - index.html -> home block

Purpose:
    The tool is meant to visualize the distribution of flu expenses by week and location.
    The number of reporting counties and expenses in a week are used as indicators to monitor the flu season 
    and determine when best to begin and end marketing compaigns. 