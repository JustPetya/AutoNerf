import os
import sys
import time


import cv2
from detection.object import CVDetect

from PySide6.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot

from bluepy import btle
from mapping import distance


def main():

    handler = Handler()
    pan, tilt = None, None
    while True:
        left_xy, right_xy = handler.lastposition()

        left_new, right_new = handler.newposition()
        print(left_xy, right_xy)
        if left_new and right_new:
            pan, tilt = distance.target_angels_turret(
                left_xy[0], right_xy[0], (left_xy[1]+right_xy[1])/2)
            handler.setold()

            print(pan, tilt)

            if pan and tilt:
                list = [1, pan, tilt]
                # iterable as source
                tosend = bytearray(list)
                handler.sendBLE(tosend)
        time.sleep(1.5)


#    video_capture = cv2.VideoCapture(2)
#
#    while True:
#        result, video_frame = video_capture.read()  # read frames from the video
#        if result is False:
#            break  # terminate the loop if the frame is not read successfully
#
#        print("cool")
#
#        img_name = "cool.png"
#        cv2.imwrite(img_name, video_frame)
#        print(img_name)
#
#        break
#
#    video_capture.release()
#    cv2.destroyAllWindows()
class Handler():
    def __init__(self):
        self.threadpool = QThreadPool()
        print(
            "Multithreading with Maximum %d threads" % self.threadpool.maxThreadCount())
        self.startBLE()
        self.startCVDetect()

    def startCVDetect(self):
        # linke Kamera oben , rechte Unten , USB Grau
        cam_l = 0
        cam_r = 2

        self.workerCVDetect_L = CVDetect(cam_l)
        self.workerCVDetect_R = CVDetect(cam_r)

        self.threadpool.start(self.workerCVDetect_L)
        self.threadpool.start(self.workerCVDetect_R)

    def startBLE(self):
        self.workerBLE = WorkerBLE()
        self.workerBLE.signals.signalMsg.connect(self.slotMsg)
        self.workerBLE.signals.signalRes.connect(self.slotRes)
        self.threadpool.start(self.workerBLE)

    def sendBLE(self, byteArrayToSend):

        self.workerBLE.toSendBLE(byteArrayToSend)

    def slotMsg(self, msg):
        print(msg)

    def slotRes(self, res):
        self.console.appendPlainText(res)

    def setold(self):
        self.workerCVDetect_L.newCoord = False
        self.workerCVDetect_R.newCoord = False

    def lastposition(self):
        return self.workerCVDetect_L.position(), self.workerCVDetect_R.position()

    def newposition(self):
        return self.workerCVDetect_L.newData(), self.workerCVDetect_R.newData()


class WorkerSignals(QObject):
    signalMsg = Signal(str)
    signalRes = Signal(str)


class MyDelegate(btle.DefaultDelegate):

    def __init__(self, sgn):
        btle.DefaultDelegate.__init__(self)
        self.sgn = sgn

    def handleNotification(self, cHandle, data):

        try:
            dataDecoded = bytes(data)
            self.sgn.signalRes.emit(dataDecoded)
        except UnicodeError:
            print("UnicodeError: ", data)


class WorkerBLE(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.rqsToSend = False

    @Slot()
    def run(self):
        print("WorkerBLE start")

        # ---------------------------------------------
        p = btle.Peripheral("D4:8A:FC:A4:80:7A")
        p.setDelegate(MyDelegate(self.signals))

        svc = p.getServiceByUUID("8ebaf998-8c59-46da-91de-3a3dae4c224f")
        self.ch_Tx = svc.getCharacteristics(
            "bc4b69c4-4a1d-4d20-b829-ad92cd2888b6")[0]
        ch_Rx = svc.getCharacteristics(
            "98ba9b1f-5341-4264-b895-7ff33fe15fcc")[0]

        setup_data = b"\x01\00"
        p.writeCharacteristic(ch_Rx.valHandle+1, setup_data)

        # BLE loop --------

        while True:
            """
            if p.waitForNotifications(1.0):
                # handleNotification() was called
                continue

            print("Waiting...")
            """

            p.waitForNotifications(1.0)

            if self.rqsToSend:
                self.rqsToSend = False

                try:
                    self.ch_Tx.write(self.bytestosend, True)
                except btle.BTLEException:
                    print("btle.BTLEException")

        # ---------------------------------------------hellohello
        self.signals.signalMsg.emit("WorkerBLE end")

    def toSendBLE(self, tosend):
        self.bytestosend = tosend
        self.rqsToSend = True
        """
        try:
            self.ch_Tx.write(bytestosend, True)
        except BTLEException:
            print("BTLEException");
        """


if __name__ == "__main__":
    # if os.name in ("nt", "dos"):
    #    os.system("cls")
    # else:
    #    os.system("clear")
    main()
