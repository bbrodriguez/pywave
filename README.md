pywave
======

Python Home Automation

This project takes the heavy lifting done under PyIrToy and hackpump by https://github.com/crleblanc and provides a simple web app for IR controlling devices.

It uses the cherrypy web framework along with JQuery and JQuerymobile to presnt a clean interface for local control of your IR devices.

It is lacking IR device state-tracking and might be nicely extended with this along with an abstract interface configuration file.

Use record_codes.py from hackpump to save a JSON file containing your named IR Codes, and assign those values to HTML objects in pywave.html.

Put appropriate icons in /media/icons if you want to save this as a webapp on your iOS or other tough device.

