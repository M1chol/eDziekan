import handle_requests as hr
import credentials
import handle_html
import os
import wx

if __name__ == "__main__":
    
    
    session = hr.edziekanSession()
    session.loadCredentials(*credentials.load())
    session.Init(log=True)
    session.Login()
    session.requestScheduleTxt()
    #handle_html.convert()
    
    # Clean up temp files
    #os.remove(hr.target_name)
    #os.remove(handle_html.temp_img_name)
    
    # app = wx.App(False)
    # frame = wx.Frame(None, wx.ID_ANY, "Hello")
    # frame.Show(True)
    # app.MainLoop()
