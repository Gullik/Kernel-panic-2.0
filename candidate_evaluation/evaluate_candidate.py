# Copyright (C) SaaS Systems, Inc - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited. Only authorized SaaS personal is allowed access to this file.
# Proprietary and strictly confidential



from confidential.evaluatation_algorithm import evaluate_candidate


def get_test_user():

    user_Data = {}
    user_Data["name"] = "Bob"
    user_Data["age"] = 38
    user_Data["weight"] = 100
    user_Data["gender"] = "person"
    user_Data["age"] = 38


    return user_Data



def evaluate(person):
    candidate_approved, evalaution_Score = evaluate_candidate(person)

    print("")
    print("#################################")
    if(candidate_approved):
        print("#  APPLICATION APPROVED         #")
        print("#  SCORE:",evalaution_Score,"                #" )
        #print("#  PROCEED TO LAUNCH FACILITES  #")
    else:
        print("#  APPLICATION REJECTED         #")
        print("#  SCORE:",evalaution_Score,"                #")
        #print("#  PROCEED TO LAUNCH FACILITES  #")
    print("#################################")

    return candidate_approved, evalaution_Score






if __name__ == '__main__':
    test = get_test_user()
    evaluate(test)

# user_Data["age"] = 2
# evaluate_candidate(user_Data)
#
#
# user_Data["age"] = 16
# evaluate_candidate(user_Data)

