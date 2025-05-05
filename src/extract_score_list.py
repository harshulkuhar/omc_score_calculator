import re

data = """
1	
Beefwhistle 
Megaserver (EU)
 2  1  9  0	May 3, 2025 2:45 AM	13:11	171,655.0	Log
2	
Dragonia 
Megaserver (EU)
 1  2  9  0	Apr 21, 2025 12:15 AM	13:38	171,271.0	Log
3	
Campsite 
Megaserver (EU)
 2  1  9  0	Apr 26, 2025 2:45 AM	14:26	165,841.0	Log
4	
Harbingers of Dread 
Megaserver (EU)
 2  2  8  0	Apr 18, 2025 1:32 AM	21:17	151,228.0	Log
5	
Trials & Error 
Megaserver (NA)
 2  2  8  0	Mar 26, 2025 9:07 AM	23:49	132,311.0	Log
6	
Golden Ducks 
Megaserver (EU)
 2  2  8  0	Apr 5, 2025 5:39 AM	19:44	117,919.0	Leaderboard
7	
Online Athletes 
Megaserver (NA)
 2  2  8  0	Apr 6, 2025 11:14 AM	25:14	114,543.0	Log
8	
Bad Life 
Megaserver (EU)
 2  2  7  0	Mar 22, 2025 4:42 AM	31:52	110,467.0	Leaderboard
9	
Crochet Club 
Megaserver (EU)
 2  2  8  0	Apr 12, 2025 12:05 AM	32:48	109,891.0	Log
10	
Loot Goblins Of Tamriel 
Megaserver (NA)
 2  2  8  0	Mar 16, 2025 7:48 AM	33:09	109,672.0	Log
11	
Swamp Jelly Sanctuary 
Megaserver (NA)
 4  2  6  0	Apr 30, 2025 8:22 AM	46:21	101,560.0	Leaderboard
12	
The Official Sweetroll Brigade 
Megaserver (NA)
 2  2  8  0	Apr 6, 2025 9:24 AM	51:55	98,144.0	Log
13	
Heroes of Tamriel 
Megaserver (EU)
 2  2  8  0	Mar 25, 2025 1:47 AM	55:05	96,195.0	Log
14	
Fight, wipe and repeat 
Megaserver (EU)
 3  2  7  0	Mar 23, 2025 4:28 AM	1:08:18	93,027.0	Leaderboard
15	
EmberleyMarie 
Megaserver (NA)
 4  2  6  0	Mar 30, 2025 9:01 AM	1:29:37	74,982.0	Log
16	
Behold a Pale Order 
Megaserver (NA)
 3  2  7  0	Mar 24, 2025 9:09 AM	1:34:44	71,843.0	Log
17	
Die sieben Raben 
Megaserver (EU)
 2  2  8  0	Apr 4, 2025 1:15 AM	1:42:11	67,258.0	Log
18	
Sinta Elenarda 
Megaserver (EU)
 2  2  8  0	Mar 23, 2025 9:45 PM	1:43:56	66,186.0	Leaderboard
19	
Breath Of Kynareth 
Megaserver (NA)
 3  2  7  0	Mar 31, 2025 10:08 AM	2:14:06	47,648.0	Log
"""

# Find all numbers right before "Leaderboard" or "Log"
matches = re.findall(r'([\d,]+)\.\d+\s+(?:Leaderboard|Log)', data)

# Convert to integer list
numbers = [int(num.replace(',', '')) for num in matches]

print(numbers)
print(len(numbers))