cont_obs = 0
inferiores = 0
pior_estimativa = float(input())
estimativa = float(input())

while estimativa > 0:
    if pior_estimativa > estimativa:
        inferiores = inferiores + 1
    estimativa = float(input())
    cont_obs = cont_obs + 1

print(cont_obs, inferiores)