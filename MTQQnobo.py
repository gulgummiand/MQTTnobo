#!/usr/bin/python3

# MQTT Client for Nobø Energy Control
from pynobo.nobo import nobo

glen = nobo('102000074129', '192.168.1.178', False)
zones = []
print("Connected.")
print("All zone info:")
print(glen.zones)
print("Zones:")
for z in glen.zones:
    print(z)
    zones.append(z)
print("Overrides:")
print(glen.overrides)
# In overrides there will only be one target_type=0, which wil be the global override. This gets a new override_id each time it's set.
# To find if a local zone has an override, check for override_id higher than the last override with target_type=0.
print("Temperatures:")
print(glen.temperatures)
# print("Press a key to list zones..")
# input()
# for z in zones:
#     print(z)

""" print("Press a key to set override..")
input()
glen.create_override(glen.API.OVERRIDE_MODE_AWAY,
                        glen.API.OVERRIDE_TYPE_NOW,
                        glen.API.OVERRIDE_TARGET_GLOBAL) """


    