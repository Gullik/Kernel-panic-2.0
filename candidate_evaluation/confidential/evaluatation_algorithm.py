# Copyright (C) SaaS Systems, Inc - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited. Only authorized SaaS personal is allowed access to this file.
# Proprietary and strictly confidential

import time
import random

MINIMUM_AGE = 3
MAXIMUM_AGE = 35



def verify_age_requirment(user_Data):
    """ Algorithm for selecting cadnidates within the desired age limits.  """
    if(user_Data["age"] > MAXIMUM_AGE):
        #print("Applicant <"+str(user_Data["name"])+"> is older than the required age limit of <"+str(MAXIMUM_AGE)+ " YEARS>")
        return False
    elif(user_Data["age"] < MINIMUM_AGE):
        #print("Applicant <"+str(user_Data["name"])+"> is younger than the minimum required age limit of <"+str(MINIMUM_AGE)+ " YEARS>")
        return False
    else:
        #print("Applicant <"+str(user_Data["name"])+"> is within the designated age")
        return True


def set_n_threads(count,status):
    # return
    time.sleep(0.1+random.randint(0,10) / 10.0)

    for h in range(0,count):
        time.sleep(0.1 + random.randint(0,10)/10.0)
        print("  ",random.randint(h*10,(h+1)*10) ,"%", status )
    time.sleep(0.1+random.randint(0,10) / 10.0)
    print("  ",100,"%", status)
    time.sleep(0.1+random.randint(0,10) / 10.0)

def evaluate_candidate(candiate):
    print(" ")
    print("Starting evaluation for applicant <"+str(candiate["name"]) +">")
    print(" ")
    print("[Loading evaluation system]")
    set_n_threads(10," loading")
    print("  ",100,"% loaded ")
    print("[Evaluation system loaded]")
    print(" ")
    print("[Starting evaluation system]")
    time.sleep(0.1+random.randint(0,10) / 10.0)

    candidate_approved = verify_age_requirment(candiate)

    set_n_threads(5," Processing applicant")
    time.sleep(2.0+random.randint(0,10) / 10.0)

    if(candidate_approved):
        evalaution_Score = random.randint(800,1000)/1000.0
    else:
        evalaution_Score = random.randint(0,500) / 1000.0



    return candidate_approved, evalaution_Score


