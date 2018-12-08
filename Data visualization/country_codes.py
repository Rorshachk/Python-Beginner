from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
# for code, name in COUNTRIES.items():
  #  print(name + ' ' + code)

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
