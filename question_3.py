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



jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}
CALLS_M = 10
MEETINGS_M = 30
SALES_M = 100
BONUS = 100
score = 0
score = score + jordan_belfort['calls']*CALLS_M
score = score + jordan_belfort['meetings']*MEETINGS_M
score = score + jordan_belfort['sales']*SALES_M
if jordan_belfort['calls']>150:
    score = score + BONUS
if jordan_belfort['meetings']>20:
    score = score + BONUS
if jordan_belfort['sales']>5:
    score = score + BONUS


jordan_belfort['score'] = score








