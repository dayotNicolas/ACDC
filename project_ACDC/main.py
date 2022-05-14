from subprocess import Popen, PIPE

import schedule
from api_handler import *

p = Popen("uvicorn project_ACDC.app:app ", shell=True, stdout=PIPE)

stderr = p.communicate()
if __name__ == "__main__":
    schedule.every().day.at("00:00").do(middleware_deces_age)
    schedule.every().day.at("00:00").do(
        middleware_professional_vaccin_percentage_department
    )
    schedule.every().day.at("00:00").do(middleware_hospitalisation_age)
    schedule.every().day.at("00:00").do(middleware_vaccination_rate)
