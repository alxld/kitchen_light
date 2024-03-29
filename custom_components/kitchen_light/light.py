"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = KitchenLight()
    add_entities([ent])


class KitchenLight(NewLight):
    """Kitchen Light."""

    def __init__(self) -> None:
        """Initialize Kitchen Light."""
        super(KitchenLight, self).__init__(
            "Kitchen", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.kitchen_chandeliers_group"] = None
        self.entities["light.kitchen_stairs_fixture_group"] = None
        self.entities["light.kitchen_ceiling_group"] = None
        self.entities["light.kitchen_under_cabinet_group"] = None
        self.entities_below_threshold = [
            "light.kitchen_chandeliers_group",
            "light.kitchen_stairs_fixture_group",
            "light.kitchen_under_cabinet_group",
        ]
        self.entities_above_threshold = ["light.kitchen_ceiling_group"]
        self.brightness_multiplier["light.kitchen_stairs_fixture_group"] = 0.6
        self.motion_sensors.append("Kitchen Motion Sensor")
        self.motion_sensors.append("Kitchen Stairs Motion Sensor")
        # self.motion_sensors.append("binary_sensor.kitchen_motion_sensor_occupancy_2")
        # self.motion_sensors.append(
        #    "binary_sensor.kitchen_stairs_motion_sensor_occupancy_2"
        # )

        self.switch = "Kitchen Switch"
        # self.switch = "00:17:88:01:0c:29:72:ff"

        self.has_brightness_threshold = True
        self.brightness_threshold = 128
        self.motion_sensor_brightness = 128
