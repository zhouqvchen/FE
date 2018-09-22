import numpy as np
import random

def Calibration():

    rate = []

    alpha = []
    sigma = []
    rate_error = 100
    real_alpha= 0.0
    real_sigma = 0.0 
    real_zero = [0.0236,0.025,0.026,0.028,0.0285,0.0286]




    # Potental sigma and alpha range from 0-1 with step 0.01
    for i in range (0,100):
        alpha.append(i*0.01+0.01)
        sigma.append(i*0.01+0.01)

    # construct 25 paths of random normal distribution ie dwt 
    normal = []
    for i in range (0,25):
        test = []
        L = np.random.normal(0,1,5)
        for j in range(0,5):
            test.append(L[j])

        normal.append(test)

    # find optimal sigma and alpha 
    for i in range (0,100):
        current_alpha = alpha[i]
        for j in range (0,100):
            current_sigma = sigma[j]

            current_path = [0.0236,0,0,0,0,0]
            #print (current_alpha)
            random_number = random.randint(0,24)
            # randomly select a normal distribution of path ie dwt 

            dwt = normal[random_number]
            current_rate_error = 0
            #print (dwt)
            for k in range(0,5):
                # construct one path of rates 
                current_rate = current_path[k]
                dr = current_alpha*(real_zero[k]-current_rate)*0.25 + current_sigma*dwt[k]
                new_rate = current_rate + dr
                current_path[k+1] = new_rate
            for m in range (0,5):
                current_rate_error+=(abs(current_path[m]-real_zero[m])) 
           

            if current_rate_error< rate_error:
                # keep track of the sigma and alpha with lowest error rate.
                rate_error = current_rate_error
                real_sigma = current_sigma
                real_alpha = current_alpha
            rate.append(current_path)

    print(real_sigma,real_alpha)




    





Calibration()