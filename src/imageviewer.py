from PyQt5.QtCore import Qt, QSize, QEasingCurve
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QScrollArea, QLabel, QSizePolicy, QScroller, QScrollerProperties as QSP
import res


class ImageZoomState:
    FIT_TO_CONTAINER = 0  # the default state where the image is fit into the container
    FULL_SIZE = 1  # full size of the image
    ARBITRARY = -1  # any other zoom level


class ImageViewer(QScrollArea):
    def __init__(self, parent=None, enable_scrollbars=False, enable_tooltip=True):
        super().__init__(parent)
        self._image_label = QLabel(self)
        self._image_label.setAlignment(Qt.AlignCenter)
        self._image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._image_label.setScaledContents(True)
        self._pixmap = QPixmap()
        self.setWidget(self._image_label)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if not enable_scrollbars:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        if enable_tooltip:
            self.setToolTip("> Drag to pan\n"
                            "> Double-click to toggle between full size and default size\n"
                            "> Scroll mouse wheel to zoom in or out")
        self._failed_img_shown = False
        self._zoom_in_factor = 1.25
        self._zoom_out_factor = 1 / self._zoom_in_factor
        self._min_zoom = 0.1  # 10 %
        self._max_zoom = 4.0  # 400 %
        self._zoom_state = ImageZoomState.FIT_TO_CONTAINER

        QScroller.grabGesture(self.viewport(), QScroller.LeftMouseButtonGesture)
        scroller_properties = QScroller.scroller(self.viewport()).scrollerProperties()
        scroller_properties.setScrollMetric(QSP.VerticalOvershootPolicy, QSP.OvershootAlwaysOff)
        scroller_properties.setScrollMetric(QSP.HorizontalOvershootPolicy, QSP.OvershootAlwaysOff)
        # scroller_properties.setScrollMetric(QSP.FrameRate, QSP.Fps30)
        scroller_properties.setScrollMetric(QSP.ScrollingCurve, QEasingCurve.Linear)
        QScroller.scroller(self.viewport()).setScrollerProperties(scroller_properties)

    def resizeEvent(self, event):
        if self._zoom_state == ImageZoomState.FIT_TO_CONTAINER:
            self.fit_to_container()

    def mouseDoubleClickEvent(self, event):
        if self._zoom_state == ImageZoomState.FIT_TO_CONTAINER:
            self._image_label.resize(self._pixmap.size())
            self._zoom_state = ImageZoomState.FULL_SIZE
        else:
            self.fit_to_container()
            self._zoom_state = ImageZoomState.FIT_TO_CONTAINER

    def wheelEvent(self, event):
        if self._failed_img_shown:
            return
        if event.angleDelta().y() > 0:
            self.scale_image(self._zoom_in_factor, self._zoom_in_factor)
        else:
            self.scale_image(self._zoom_out_factor, self._zoom_out_factor)

    def set_image(self, filename):
        if not self._pixmap.load(filename):
            self._pixmap.load(":/failed_img_t.png")
            self._failed_img_shown = True
        else:
            self._failed_img_shown = False
        self._image_label.setPixmap(self._pixmap)
        self.fit_to_container()

    def clear_image(self):
        self._image_label.clear()
        self._pixmap = QPixmap()

    def rotate_image(self):
        if self._failed_img_shown or self._zoom_state != ImageZoomState.FIT_TO_CONTAINER:
            return
        self._pixmap = self._pixmap.transformed(QTransform().rotate(90))
        self._image_label.setPixmap(self._pixmap)
        self.update_image()

    def update_image(self):
        if self._zoom_state == ImageZoomState.FIT_TO_CONTAINER:
            self.fit_to_container()

    def fit_to_container(self):
        self._image_label.resize(self._pixmap.size().scaled(self.size(), Qt.KeepAspectRatio))
        self._zoom_state = ImageZoomState.FIT_TO_CONTAINER

    def scale_image(self, width_factor, height_factor):
        target_width = self._image_label.size().width() * width_factor
        if (target_width / self._pixmap.width()) > self._max_zoom or \
                (target_width / self._pixmap.width()) < self._min_zoom:
            return
        self._image_label.resize(
            QSize(target_width, self._image_label.size().height() * height_factor))
        self._zoom_state = ImageZoomState.ARBITRARY

    @property
    def label(self):
        """In case you need to grab a handle to the QLabel of this ImageViewer"""
        return self._image_label

    @property
    def width_height(self):
        sz = self._pixmap.size()
        return sz.width(), sz.height()
