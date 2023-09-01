def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    sum_m = (given_mass1 / molar_mass1) + (given_mass2 / molar_mass2)
    temp = temp + 273.15
    R = 0.082
    p_total = sum_m * R * temp / volume
    return p_total