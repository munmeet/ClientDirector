name = $2
address = $1
pstn = $3
X = $0
import time
Y = time.mktime(X)
import beatrice
Z = beatrice.electronicMail(name)
#
#Copyright ® 2024, munmeet § BAUJI SERVICES
script = beatrice.geo(pstn)