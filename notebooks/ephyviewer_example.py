# from ephyviewer import mkQApp, MainViewer, TraceViewer
# import numpy as np

# app = mkQApp()

# #fake sigs
# sigs = np.random.rand(1_000_000,16)
# sample_rate = 1000.
# t_start = 0.

# #Create the main window that can contain several viewers
# win = MainViewer()
# view1 = TraceViewer.from_numpy(sigs, sample_rate, t_start, 'Signals')
# win.add_view(view1)

# #Parameters can be set in script
# view1.params['scale_mode'] = 'same_for_all'
# view1.params['display_labels'] = True
# #And also parameters for each channel
# view1.by_channel_params['ch0', 'visible'] = False
# view1.by_channel_params['ch15', 'color'] = '#FF00AA'

# #Run
# win.show()
# app.exec()


import ephyviewer

#for this example we use fake source construct by theses function
from  ephyviewer.tests.testing_tools import make_fake_video_source
from  ephyviewer.tests.testing_tools import make_fake_signals
from  ephyviewer.tests.testing_tools import make_fake_event_source
from  ephyviewer.tests.testing_tools import make_fake_epoch_source

sig_source = make_fake_signals()
event_source = make_fake_event_source()
epoch_source = make_fake_epoch_source()
video_source = make_fake_video_source()



app = ephyviewer.mkQApp()
view1 = ephyviewer.TraceViewer(source=sig_source, name='signals')
view2 = ephyviewer.VideoViewer(source=video_source, name='video')
view3 = ephyviewer.EventList(source=event_source, name='events')
view4 = ephyviewer.EpochViewer(source=epoch_source, name='epoch')
view5 = ephyviewer.TimeFreqViewer(source=sig_source, name='timefreq')


win = ephyviewer.MainViewer(debug=True, settings_name='test1', show_global_xsize=True, show_auto_scale=True)

win.add_view(view1)
win.add_view(view5, split_with='signals')
win.add_view(view2)
win.add_view(view4)
win.add_view(view3, location='bottom',  orientation='horizontal')

win.show()

win.auto_scale()

app.exec()
