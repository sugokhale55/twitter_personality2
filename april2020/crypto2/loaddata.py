

from crypto2.models import Event
from crypto2.apps import Event
event1 = Event(name="new_pne", event_date="2018-12-17",
venue="test venue", manager="Bob")


event1.save()


