# Experiment with wxPython's HtmlWindow
# tested with Python24 and wxPython26    vegaseat   17may2006
import wx
import wx.html


class MyHtmlPanel(wx.Panel):
    """
    class MyHtmlPanel inherits wx.Panel and adds a button and HtmlWindow
    """

    def __init__(self, parent, id):
        # default pos is (0, 0) and size is (-1, -1) which fills the frame
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("yellow")
        self.html1 = wx.html.HtmlWindow(self, id, pos=(0, 30), size=(602, 310))

        self.btn1 = wx.Button(self, -1, "Load Html File", pos=(0, 0))
        self.btn1.Bind(wx.EVT_BUTTON, self.OnLoadFile)

        self.btn2 = wx.Button(self, -1, "Clear Page", pos=(120, 0))
        self.btn2.Bind(wx.EVT_BUTTON, self.OnClearPage)

    def OnLoadFile(self, event):
        dlg = wx.FileDialog(self, wildcard='*.htm*')
        if dlg.ShowModal():
            path = dlg.GetPath()
            self.html1.LoadPage(path)
        dlg.Destroy()

    def OnClearPage(self, event):
        self.html1.SetPage("")


app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID, title, size
frame = wx.Frame(None, -1, "HtmlWindow()", size=(610, 380))
# call the derived class, -1 is default ID
MyHtmlPanel(frame, -1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()