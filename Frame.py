import os
import time
import wx
import MplayerCtrl as mpc
import wx.lib.buttons as buttons


dirName = os.path.dirname(os.path.abspath(__file__));
bitmapDir = os.path.join(dirName, 'bitmaps');


class Frame(wx.Frame):
    def __init__(self, parent, id, title, mplayer):
        wx.Frame.__init__(self, parent,id, title)
        self.panel = wx.Panel(self)

        sp = wx.StandardPaths.Get()
        self.currentFolder = sp.GetDocumentsDir()
        self.currentVolume = 50
        self.create_menu()
