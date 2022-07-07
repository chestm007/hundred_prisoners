import sys
import random


class Boxes:
    def __init__(self, length):
        self.values = []
        self._fill_boxes(length)

    def _fill_boxes(self, length):
        def get_box_value():
            while True:
                num = random.randrange(1, length + 1)
                if num not in self.values:
                    break
            return num

        for i in range(length):
            self.values.append(get_box_value())

    def read_box(self, box):
        return self.values[box - 1]

    def read_loop(self, target_value):
        steps = 0
        cur_box = target_value
        while True:
            steps += 1
            if self.read_box(cur_box) == target_value:
                return steps
            else:
                cur_box = self.read_box(cur_box)


def main(num_boxes=100, samples=1000):
    success = 0
    for i in range(samples):
        boxes = Boxes(num_boxes)

        step_counts = [boxes.read_loop(i) for i in range(1, num_boxes + 1)]

        if max(step_counts) <= 50:
            success += 1

    print(success/samples)


if __name__ == '__main__':
    def wrong_args():
        print('wrong args, please pass number of boxes and sample size.\n eg: python box.py 100 1000')
    if len(sys.argv) == 1:
        main()
    else:
        try:
            _num_boxes = int(sys.argv[1])
            _samples = int(sys.argv[2])
        except IndexError:
            wrong_args()
            sys.exit(1)
        main(_num_boxes, _samples)
