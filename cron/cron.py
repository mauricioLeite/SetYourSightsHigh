import time
import atexit
import smtplib
from datetime import datetime
from orbit_predictor.sources import get_predictor_from_tle_lines
from orbit_predictor.coordinate_systems import ecef_to_llh
from apscheduler.schedulers.background import BackgrounScheduler

def distCalculation():
	act = False
	flag = [0]*14
	dists_v = [0]*14
	i = 0
	
	with open('TLE.txt') as TLE:
		predictor = get_predictor_from_tle_lines(TLE)
		result = predictor.get_position(datetime.now())
		pos_ecef = result[1]
		#Rads
		lat, lon, h = ecef_to_llh(pos_ecef)
		#Degrees
		lat = lat*pi/180
		lon = lon*pi/180

		userLat = -22.412
		userLong = -45.46

		d = (sqrt(pow((userLat - lat)*60*1852, 2) + pow(userLong - lon*60*1852, 2))/1000);

		if(d > 20112):
			d = 40024 - d

		real_dist = sqrt(pow(d,2)+pow(h,2))
		if(real_dist < n):
			flag[i] = 1
			dists_v[i++] = real_dist
			act = True

	if(act):
		message = "Working....."
		
		password = "dupladecinco55"
		msgFrom = "dupladequatromaisum@gmail.com"
		msgTo = "vitaj@umail365.com"
	 
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		 
		server.login(msgFrom, password)
			 
		server.sendmail(msgFrom, msgTo, message)
		server.quit()

scheduler = BackgrounScheduler()
scheduler.add_job(func=distCalculus, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())