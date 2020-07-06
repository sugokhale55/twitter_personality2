from django.db import models
from crypto2.models import Event
event1 = Event(name="lll", event_date="2018-12-17",
venue="test venue", manager="Bob")


event1.save()