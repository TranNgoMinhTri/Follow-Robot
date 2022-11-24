import os
import sys
import argparse

from matplotlib.pyplot import box
from vision.ssd.mobilenet_v2_ssd_lite import create_mobilenetv2_ssd_lite, create_mobilenetv2_ssd_lite_predictor
from vision.utils.misc import Timer
import cv2
import sys
from lib.test.evaluation import Tracker
# model_path = sys.argv[1]
# label_path = sys.argv[2]
def detect():
    label_path = '/home/minhtri2001/Desktop/combine /models/voc-model-labels.txt'
    model_path = '/home/minhtri2001/Desktop/combine /models/mb2-ssd-lite-mp-0_686.pth'
    # if len(sys.argv) >= 5:
    #     cap = cv2.VideoCapture(sys.argv[4])  # capture from file
    # else:
    cap = cv2.VideoCapture(0)   # capture from camera
    cap.set(3, 1920)
    cap.set(4, 1080)

    class_names = [name.strip() for name in open(label_path).readlines()]
    num_classes = len(class_names)
    net = create_mobilenetv2_ssd_lite(len(class_names), is_test=True)
    net.load(model_path)
    predictor = create_mobilenetv2_ssd_lite_predictor(net, candidate_size=200)
    prj_path = os.path.join(os.path.dirname(__file__), '..')
    if prj_path not in sys.path:
        sys.path.append(prj_path)
    timer = Timer()
    cv2.namedWindow('annotated', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow('annotated', 960, 720)
    while True:
        ret, orig_image = cap.read()
        if orig_image is None:
            continue
        orig_image  = cv2.resize(orig_image, (640,480))
        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        timer.start()
        boxes, labels, probs = predictor.predict(image, 10, 0.4)
        interval = timer.end()
        # print('Time: {:.2f}s, Detect Objects: {:d}.'.format(interval, labels.size(0)))
        for i in range(boxes.size(0)):
            # print('boxes: {}, labels: {}, probs: {}.'.format(boxes.shape, type(labels), probs.shape))
            box = boxes[i, :]
            print(labels[i])
            label = f"{class_names[labels[i]]}: {probs[i]:.2f}"
            cv2.rectangle(orig_image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 255, 0), 4)

            cv2.putText(orig_image, label,
                        (int(box[0])+20, int(box[1])+40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,  # font scale
                        (255, 0, 255),
                        2)  # line type
            cv2.putText(orig_image, 'Press Q to start tracking', (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),3)
            
            if labels[i] == 15:
                x1,y1,x2,y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        cv2.imshow('annotated', orig_image)
        print(orig_image.shape)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    # cv2.destroyAllWindows()
    return x1,y1,x2,y2


def run_video(tracker_name, tracker_param, videofile, optional_box=None, debug=None, save_results=False, box = []):
    """Run the tracker on your webcam.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        debug: Debug level.
    """
    tracker = Tracker(tracker_name, tracker_param, "video")
    tracker.run_video(videofilepath=videofile,box=box , optional_box=optional_box, debug=debug, save_results=save_results)


def main():
    parser = argparse.ArgumentParser(description='Run the tracker on your webcam.')
    parser.add_argument('tracker_name',type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param',type=str, help='Name of parameter file.')
    parser.add_argument('videofile', default= '0',type=str, help='path to a video file.')
    parser.add_argument('--optional_box', type=float, default=None, nargs="+", help='optional_box with format x y w h.')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--save_results', dest='save', action='store_true', help='Save bounding boxes')
    parser.set_defaults(save_results=True)

    args = parser.parse_args()
    x1,y1,x2,y2 = detect()
    box = [x1,y1,x2,y2]
    run_video(args.tracker_name, args.tracker_param, args.videofile, args.optional_box, args.debug, args.save_results, box=box)


if __name__ == '__main__':
    main()
