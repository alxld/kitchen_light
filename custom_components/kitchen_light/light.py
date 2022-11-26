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
        self.entities["light.kitchen_group"] = None
        self.motion_sensors.append("Kitchen Motion Sensor")

        self.has_brightness_threshold = True
        self.brightness_threshold = 128
        self.motion_sensor_brightness = 170
