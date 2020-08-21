Jordan_belfort = {"calls": 178, "meetings":17,  "sales":6}
score = 0

if "calls" in Jordan_belfort:
    score += Jordan_belfort["calls"] * 10

    if Jordan_belfort["calls"] > 150:
        score += 100

if "meetings" in Jordan_belfort:
    score += Jordan_belfort["meetings"]* 30

    if Jordan_belfort["meetings"] > 20:
        score += 100  

if "sale" in Jordan_belfort:
    score += Jordan_belfort["sale"]* 100           

    if Jordan_belfort["sale"] > 5:
        score += 100  



print(score)        

