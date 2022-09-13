# Android **only** HTML viewer, always full screen.
#
# Back button or gesture has the usual browser behavior, except for the final
# back event which returns the UI to the view before the browser was opened.
#
# Base Class:  https://kivy.org/doc/stable/api-kivy.uix.modalview.html
#
# Requires: android.permissions = INTERNET
# Uses:     orientation = landscape, portrait, or all
# Arguments:
# url               : required string,  https://   file:// (content://  ?)
# enable_javascript : optional boolean, defaults False
# enable_downloads  : optional boolean, defaults False
# enable_zoom       : optional boolean, defaults False
#
# Downloads are delivered to app storage see downloads_directory() below.
#
# Tested on api=27 and api=30
#
# Note:
#    For api>27   http://  gives net::ERR_CLEARTEXT_NOT_PERMITTED
#    This is Android implemented behavior.
#
# Source https://github.com/Android-for-Python/Webview-Example

from android.runnable import run_on_ui_thread
from jnius import PythonJavaClass, autoclass, cast, java_method
from kivy.uix.modalview import ModalView

WebViewA = autoclass("android.webkit.WebView")
WebViewClient = autoclass("android.webkit.WebViewClient")
WebSettings = autoclass("android.webkit.WebSettings")
LayoutParams = autoclass("android.view.ViewGroup$LayoutParams")
LinearLayout = autoclass("android.widget.LinearLayout")
KeyEvent = autoclass("android.view.KeyEvent")
ViewGroup = autoclass("android.view.ViewGroup")
DownloadManager = autoclass("android.app.DownloadManager")
DownloadManagerRequest = autoclass("android.app.DownloadManager$Request")
Uri = autoclass("android.net.Uri")
Environment = autoclass("android.os.Environment")
Context = autoclass("android.content.Context")
PythonActivity = autoclass("org.kivy.android.PythonActivity")
Color = autoclass("android.graphics.Color")
View = autoclass("android.view.View")


class DownloadListener(PythonJavaClass):
    # https://stackoverflow.com/questions/10069050/download-file-inside-webview
    __javacontext__ = "app"
    __javainterfaces__ = ["android/webkit/DownloadListener"]

    @java_method(
        "(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V"
    )
    def onDownloadStart(self, url, userAgent, contentDisposition, mimetype, contentLength):
        mActivity = PythonActivity.mActivity
        context = mActivity.getApplicationContext()
        visibility = DownloadManagerRequest.VISIBILITY_VISIBLE_NOTIFY_COMPLETED
        dir_type = Environment.DIRECTORY_DOWNLOADS
        uri = Uri.parse(url)
        filepath = uri.getLastPathSegment()
        request = DownloadManagerRequest(uri)
        request.setNotificationVisibility(visibility)
        request.setDestinationInExternalFilesDir(context, dir_type, filepath)
        dm = cast(DownloadManager, mActivity.getSystemService(Context.DOWNLOAD_SERVICE))
        dm.enqueue(request)


class KeyListener(PythonJavaClass):
    __javacontext__ = "app"
    __javainterfaces__ = ["android/view/View$OnKeyListener"]

    def __init__(self, listener):
        super().__init__()
        self.listener = listener

    @java_method("(Landroid/view/View;ILandroid/view/KeyEvent;)Z")
    def onKey(self, v, key_code, event):
        if event.getAction() == KeyEvent.ACTION_DOWN and key_code == KeyEvent.KEYCODE_BACK:
            return self.listener()


class WebView(ModalView):
    # https://developer.android.com/reference/android/webkit/WebView

    def __init__(
        self,
        url,
        enable_javascript=False,
        enable_downloads=False,
        enable_zoom=False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.url = url
        self.enable_javascript = enable_javascript
        self.enable_downloads = enable_downloads
        self.enable_zoom = enable_zoom
        self.webview = None
        self.enable_dismiss = True
        self.open()

    @run_on_ui_thread
    def on_open(self):
        mActivity = PythonActivity.mActivity
        webview = WebViewA(mActivity)
        webview.setWebViewClient(WebViewClient())
        webview.getSettings().setJavaScriptEnabled(self.enable_javascript)
        webview.getSettings().setBuiltInZoomControls(self.enable_zoom)
        webview.getSettings().setDisplayZoomControls(False)
        webview.getSettings().setAllowFileAccess(True)  # default False api>29
        webview.getSettings().setCacheMode(
            WebSettings.LOAD_CACHE_ELSE_NETWORK
        )  # Enable Cache
        webview.setLayerType(View.LAYER_TYPE_HARDWARE, None)  # Enable hardware acceleration
        layout = LinearLayout(mActivity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.addView(webview, self.width, self.height)
        mActivity.addContentView(layout, LayoutParams(-1, -1))
        webview.setOnKeyListener(KeyListener(self._back_pressed))
        webview.setBackgroundColor(Color.BLACK)
        if self.enable_downloads:
            webview.setDownloadListener(DownloadListener())
        self.webview = webview
        self.layout = layout
        try:
            webview.loadUrl(self.url)
        except Exception as e:
            print("Webview.on_open(): " + str(e))
            self.dismiss()

    @run_on_ui_thread
    def on_dismiss(self):
        if self.enable_dismiss:
            self.enable_dismiss = False
            parent = cast(ViewGroup, self.layout.getParent())
            if parent is not None:
                parent.removeView(self.layout)
            self.webview.clearHistory()
            self.webview.clearCache(True)
            self.webview.clearFormData()
            self.webview.destroy()
            self.layout = None
            self.webview = None

    @run_on_ui_thread
    def on_size(self, instance, size):
        if self.webview:
            params = self.webview.getLayoutParams()
            params.width = self.width
            params.height = self.height
            self.webview.setLayoutParams(params)

    def pause(self):
        if self.webview:
            self.webview.pauseTimers()
            self.webview.onPause()

    def resume(self):
        if self.webview:
            self.webview.onResume()
            self.webview.resumeTimers()

    def downloads_directory(self):
        # e.g. Android/data/org.test.myapp/files/Download
        dir_type = Environment.DIRECTORY_DOWNLOADS
        context = PythonActivity.mActivity.getApplicationContext()
        directory = context.getExternalFilesDir(dir_type)
        return str(directory.getPath())

    def _back_pressed(self):
        if self.webview.canGoBack():
            self.webview.goBack()
        else:
            self.dismiss()
        return True
