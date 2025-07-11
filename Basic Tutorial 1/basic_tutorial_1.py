import os
os.add_dll_directory(r"C:\Program Files\gstreamer\1.0\msvc_x86_64\bin") 

import sys
import gi

gi.require_version('GLib', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')

from gi.repository import Gst

pipeline = None
bus = None
message = None

# initialize GStreamer
Gst.init(sys.argv[1:])

# build the pipeline
# A chain of steps (elements) that process media (like video/audio)
pipeline = Gst.parse_launch(
    "playbin uri=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm"
)
# Gst.parse_launch(...) -> builds a pipeline — like a flowchart for media processing.
# playbin -> is a magic player that handles everything: loading, decoding, and playing the video.

# start playing
pipeline.set_state(Gst.State.PLAYING)

# wait until EOS or error
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(
    Gst.CLOCK_TIME_NONE,
    Gst.MessageType.ERROR | Gst.MessageType.EOS
)
# This line waits until -> The video finishes (EOS = End Of Stream), or An error happens

# free resources
pipeline.set_state(Gst.State.NULL)
# This stops everything properly so no memory is wasted.