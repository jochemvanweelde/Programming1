def lang_genoeg(lengte):
    if lengte < 120:
        return 'Sorry, je bent te klein' #kleiner dan 120cm
    else:
        return 'Je bent lang genoeg voor de attractie!' #120 cm of langer

print(lang_genoeg(120))
#Je bent lang genoeg voor de attractie!