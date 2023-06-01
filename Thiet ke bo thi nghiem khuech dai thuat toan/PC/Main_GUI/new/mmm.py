import numpy as np
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsProxyWidget, QLabel
import pyqtgraph as pg


class GuiWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.サイン波を作成()
        self.グラフを描画()
        self.クロスヘアを設置()
        self.文字表示版を設置()
        self.マウス移動時の処理を設定()

    def サイン波を作成(self):
        self.freq = 1    # サイン波の周波数 [Hz]
        self.Ts = 0.001  # サンプリング周期 [秒]
        self.Ns = 1000   # サンプリング点数 [個]
        self.ns = np.arange(0, self.Ns)  # サンプル番号
        self.time = self.ns * self.Ts
        self.sin = 10 * np.sin(2 * np.pi * self.freq * (self.ns * self.Ts))

    def グラフを描画(self):
        self.graph = pg.GraphicsLayoutWidget(show=True)
        self.p0 = self.graph.addPlot(row=0, colspan=3)
        self.p0.plot(x=self.time, y=self.sin, pen=pg.mkPen((255,255,0), width=10))

    def クロスヘアを設置(self):                         # ? 1
        self.クロスヘア_v = pg.InfiniteLine(angle=90,movable=False, pen=(127,127,127))
        self.クロスヘア_h = pg.InfiniteLine(angle=0, movable=False, pen=(127,127,127))
        self.p0.addItem(self.クロスヘア_v, ignoreBounds=True)
        self.p0.addItem(self.クロスヘア_h, ignoreBounds=True)
        self.クロスヘア_v.setPos(0)
        self.クロスヘア_h.setPos(0)

    def 文字表示版を設置(self):
        self.文字表示版_項目_x = FlexibleSpace(app=self, win=self.graph, row=1, col=0, h=25, w=50, text='x : ')
        self.文字表示版_項目_y = FlexibleSpace(app=self, win=self.graph, row=2, col=0, h=25, w=50, text='y : ')
        self.文字表示版_値_x  = FlexibleSpace(app=self, win=self.graph, row=1, col=1, h=25, w=100)
        self.文字表示版_値_y  = FlexibleSpace(app=self, win=self.graph, row=2, col=1, h=25, w=100)
        self.スペーサー1      = FlexibleSpace(app=self, win=self.graph, row=1, col=2, h=25)
        self.スペーサー2      = FlexibleSpace(app=self, win=self.graph, row=2, col=2, h=25)

    def マウス移動時の処理を設定(self):      
        def クロスヘアを更新():                       # ? 2
            self.クロスヘア_x値_インデックス = int(round(self.cursor.x()/self.Ts))
            self.クロスヘア_x値 = round(self.クロスヘア_x値_インデックス * self.Ts, 3)
            self.クロスヘア_y値 = round(self.sin[self.クロスヘア_x値_インデックス], 3)
            self.クロスヘア_v.setPos(self.クロスヘア_x値)
            self.クロスヘア_h.setPos(self.クロスヘア_y値)

        def 文字表示版を更新():                       # ? 3
            self.文字表示版_値_x.setInnerText(str(self.クロスヘア_x値))
            self.文字表示版_値_y.setInnerText(str(self.クロスヘア_y値))

        def mouseMoved(evt):                       # ? 4
            self.pos = evt[0]  # マウス位置
            if self.p0.sceneBoundingRect().contains(self.pos):  # マウスがプロットエリアにあれば
                self.cursor = self.vb0.mapSceneToView(self.pos)  # マウス座標を取得
                if self.cursor.x() >= 0 and self.cursor.x() < self.Ts * self.Ns :
                    クロスヘアを更新()
                    文字表示版を更新()

        self.vb0 = self.p0.vb
        self.proxy = pg.SignalProxy(self.p0.scene().sigMouseMoved,
                                    rateLimit=60, slot=mouseMoved)


class FlexibleSpace(QWidget):
    def __init__(self, app, win, row, col, rowspan=1, colspan=1, w=0, h=0, name='', text=''):
        super().__init__()
        self.set_layout(win=win, row=row, col=col, rowspan=rowspan, colspan=colspan)
        self.set_object(app=app, w=w, h=h, name=name, text=text)
        self.set_proxy()
        self.setInnerText(text=text)

    def set_layout(self, win, row, col, rowspan, colspan):
        self.p = win.addLayout(row=row, col=col, rowspan=rowspan, colspan=colspan)
        self.p.setContentsMargins(10,0,10,0)  # 左,上,右,下

    def set_object(self, app, w, h, name, text):
        def make_object():
            self.object = QLabel()

        def set_style():
            style = ('QLabel{'
                    'background-color: rgba(0,0,0,0);'
                    'color: darkgray;'
                    '}')
            self.object.setStyleSheet(style)

        def set_size(w, h):
            def set_wsize(w):
                self.object.setMinimumWidth(w)
                self.object.setMaximumWidth(w)

            def set_hsize(h):
                self.object.setMinimumHeight(h)
                self.object.setMaximumHeight(h)

            if w > 0:
                set_wsize(w)
            else:
                pass  # free size
            if h > 0:
                set_hsize(h)
            else:
                pass  # free size

        make_object()
        set_style()
        set_size(w=w, h=h)

    def set_proxy(self):
        self.proxy = QGraphicsProxyWidget()
        self.item = self.p.addItem(self.proxy)
        self.proxy.setWidget(self.object)

    def setInnerText(self, text):
        self.object.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GuiWindow()
    sys.exit(app.exec())