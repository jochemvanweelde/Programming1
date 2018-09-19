cijferICOR = 6.5
cijferPROG = 7.8
cijferCSN = 6.9
gemiddelde = (cijferICOR + cijferPROG + cijferCSN)/3
beloning = gemiddelde * 30 * 3
import math
gemiddeldeG = (math.floor(gemiddelde*10)/10)
beloningG = round(beloning, 1)
print('Mijn cijfers (gemiddeld een ', gemiddeldeG, ') leveren een beloning op van ', beloningG, 'euro!')


#Mijn cijfers (gemiddeld een  7.0 ) leveren een beloning op van  636.0 euro!