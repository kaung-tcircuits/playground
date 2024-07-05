min_baldwin = float('inf')
max_baldwin = -float('inf')

min_surface_predict = float('inf')
max_surface_predict = -float('inf')

min_spt = float('inf')
max_spt = -float('inf')


with open("../meat-dagger-firmware/firmware/debug_log.txt", "r") as debug_output:
    for line in debug_output:
        if "Baldwin optimize" in line:
            val = int(line.split()[4])
            if val < min_baldwin: min_baldwin = val
            if val > max_baldwin: max_baldwin = val
        elif "Surface predictor" in line:
            val = int(line.split()[4])
            if val < min_surface_predict: min_surface_predict = val
            if val > max_surface_predict: max_surface_predict = val
        elif "SPT predict" in line:
            val = int(line.split()[4])
            if val < min_spt: min_spt = val
            if val > max_spt: max_spt = val


print(min_baldwin, max_baldwin, min_surface_predict, max_surface_predict, min_spt, max_spt)