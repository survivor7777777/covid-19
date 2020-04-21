
# done
def f"actual_R"(i, new_infection[]): # G -> I
    if new_infection[i]<10 or new_infection[i+1] == NaN:
        actual_R[i] = NaN
    else:
        actual_R[i] = new_infection[i+1]/new_infection[i]

# done
def f"actual_doubling_time_in_days"(i, actual_R): # H -> G
    if actual_R[i] == NaN:
        actual_doubling_time_in_days[i] = NaN
    elif actual_R[i] <= 1:
        actual_doubling_time_in_days[i] = Infinity
    else:
        actual_doubling_time_in_days[i] = serial * np.log(2) / np.log(cumulative_infection[i]/cumulative_infection[i-1])

# done
def f"new_infection"(i, ...): # I -> W, V, J
    if i == 0:
        new_infection[i] = initial_infection
    else:
        new_infection[i] = round(susceptible[i-1]*(1 - (1 - ((target_R[i-1] * (1-cumulative_infection[i-1]/population)**cluster)/population))^new_infection[i-1]))
        new_infection[i] = round(susceptible[i-1]*(1 - (1 - ((target_R[i-1] * (susceptible[i-1]/population)**cluster)/population))^new_infection[i-1]))

# done
def f"cumulative_infection"(i, new_infection[]): # J -> I
    cumulative_infection[i] = new_infection[0:i+1].sum()

def f"observed_R"(i, ): # L -> N
    if N[i]<10 or N[i+1] == NaN:
        observed_R[i] = NaN
    else:
        observed_R[i] = new_detected_cases[i+1]/new_detected_cases[i]

def f"detected_doubling_time"(i, ...): # M -> O
    if O[i+1]/O[i]) < 1:
        detected_doubling_time[i] = Infinity
    else:
        detected_doubling_time[i] = serial * log(2) / log(O[i+1]/O[i])

def f"new_detected_cases"(i, reported_new_positive): # N -> BM
    if Not exists(reported_new_positive[i-delay]):
        new_detected_cases[i] = 0
    else:
        new_detected_cases[i] = reported_new_positive[i-delay]

def f"cumulative_detected_cases"(i, new_detected_cases): # O -> N
    cumulative_detected_cases[i] = new_detected_cases[0:i+1].sum()

def f"detection_rate"(i, cumulative_detected_cases, cumulative_infection): # Q -> O, J
    dtection_rate[i] = cumulative_detected_cases[i] / cumulative_infection[i]

def f"new_tests_reported"(i, ...): # S -> BA, BB, BC
    if i < delay:
        new_tests_reported[i] = 0
    else:
        new_tests_reported]i] = total_test_conducted_severe[i-delay] + total_test_conducted_mild[i-delay] - total_test_conducted_asymptomatic[i-delay]

def f"share_positive"(i, ...): # T -> N, S
    if new_tests_reported[i] == 0:
        share_positive[i] = NaN
    else:
        share_positive[i] = new_detected_cases[i] / new_tests_reported[i]

# done
def f"target_R"(i, ...): # V ->
    if begin_lockdown != None and i >= begin_lockdoown:
        target_R[i] = R_lockdown
    elif begin_intermediate != None and i >= begin_intermediate:
        target_R[i] = R_intermediate
    else:
        target_R[i] = R_uncontolled

# done
def f"susceptible"(i, cumulative_infection[]): # W -> J
    suceptible[i] = population - cumulative_infection[i]

def f"new_infection_severe": # Y
    pass

def f"new_infection_mild" # Z
    pass

def f"new_infection_asymptomatic" # AA
    pass

def f"desiring_test_severe"(): # AG
    pass

def f"desiring_test_mild"(): # AH
    pass

def f"desiring_test_asymtomatic"(): # AI
    pass

# done
def f"test_available"(i, ...): # AK -> None
    if i == 0:
        test_available[i] = 0
    elif i == 1:
        test_available[i] = initial_tests
    elif i >= ramp_period:
        test_available[i] = round(min(tests_max, test_available[i-1] * (1+test_growth_rate)))
    else:
        test_available[i] = test_available[i-1]

# not necessary
def f"rationed_tests"(i, ...): # AL -> AK
    rationed_tests[i] = round(AK[i]*rationed_tests)

def f"on_demand_tests"(i, ...): # AM
    pass

def f"allocation_of_rationed_test_severe"(i, ...): # AO -> AL, AG
    allocation_of_rationed_test_severe[i] = min(rationed_tests[i], desiring_test_severe[i])

def f"allocation_of_rationed_test_mild"(i, ...): # AP -> AH, AL, AO
    allocation_of_rationed_test_mild[i] = min(desiring_test_mild[i], rationed_test[i]-allocation_of_rationed_test_severe[i])

def f"allocation_of_rationed_test_asymptomatic"(i, ...): # AQ -> AP, AO
    allocation_of_rationed_test_mild[i] = min(desiring_test_asymptomatic[i], rationed_test[i]-allocation_of_rationed_test_severe[i]-allocation_of_rationed_test_mild[i])

def f"unfilled_test_demand_severe"(): # AS -> AG, AO
    desiring_test_severe[i] - allocation_of_rationed_test_severe[i]
    
def f"total_test_conducted_severe"(i, ...): # BA -> AW, AO
    total_test_conducted_severe[i] = allocation_of_on_demand_test_severe[i] + allocation_of_rationed_test_severe[i]

def f"total_test_conducted_mild"(i, ...): # BB -> AX, AP
    total_test_conducted_mild[i] = allocation_of_on_demand_test_mild[i] + allocation_of_rationed_test_mild[i]
    
def f"total_test_conducted_asymptomatic"(i, ...): # BC -> AY, AQ
    total_test_conducted_asymptmatic[i] = allocation_of_rationed_test_asymptomatic[i] + allocation_of_rationed_test_asymptomatic[i]

def f"share_severe"(): # BE
    new_infected_severe / severe
    
def f"positive_tests_severe"(i, ...): # BI -> BA, BE
    round(total_tests_conducted_severe[i]*BE[i]*(1 - false_negative))+round(BB[i]*(1-BF[i])*false_positive))


def f"reported_new_positives"(i, ...): # BM -> BI, BJ, BK
    return BI[i]+BJ[i]+BK[i]
