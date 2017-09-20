import settings
from packets import Packets
from operator import itemgetter
def sortnetworkbuffer():
    settings.networkbuffer.sort(key=itemgetter("timestamp"))

    settings.networkbuffer = sorted(settings.networkbuffer, key=lambda Packets: Packets.timestamp)
