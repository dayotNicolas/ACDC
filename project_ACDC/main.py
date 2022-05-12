import subprocess as sp

import schedule
import popen as p
from api_handler import *

sp.Popen("uvicorn project_ACDC.app:app",shell=True)

if __name__ == '__main__':
    schedule.every(24).hours.do(middleware_deces_age)
    schedule.every(24).hours.do(middleware_professional_vaccin_percentage_department)
    schedule.every(24).hours.do(middleware_hospitalisation_age)
    schedule.every(24).hours.do(middleware_vaccination_rate)