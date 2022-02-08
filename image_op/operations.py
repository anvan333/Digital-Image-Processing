import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)

        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        # add your code here

        firstImage = image_left.copy()
        secondImage = image_right.copy()

        shiftRow = image_left.shape[0]
        shiftColumn = image_left.shape[1]

        for x in range(shiftRow):
            for y in range(shiftColumn):
                if y >= column:
                    firstImage[x][y] = secondImage[x][y]

        # Please do not change the structure
        return firstImage  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here

        output_image = input_image.copy()

        myRow = input_image.shape[0]
        myColumn = input_image.shape[1]

        for x in range(myRow):
            for y in range(myColumn):

                if y < column:
                    output_image[x][y] = input_image[x][y] * alpha

                elif y >= column:
                    output_image[x][y] = input_image[x][y] * beta

        # Please do not change the structure
        return output_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)
        input_image: the input image
        column: image column at which left section ends
        return: output_image
        """

        # add your code here

        output_image = np.zeros([350, 340], np.float64)

        myRow = input_image.shape[0]
        myColumn = input_image.shape[1]

        sum_right = 0
        sum_left = 0

        num_right = 0
        num_left = 0

        for x in range(myRow):
            for y in range(myColumn):
                if y < column:
                    num_left += 1
                    sum_left += input_image[x][y]
                elif y >= column:
                    num_right += 1
                    sum_right += input_image[x][y]

        intensity_left = sum_left / num_left
        intensity_right = sum_right / num_right

        offset_right = 128 - intensity_right
        offset_left = 128 - intensity_left

        for x in range(myRow):
            for y in range(myColumn):
                if y >= column:
                    output_image[x][y] = offset_right + input_image[x][y]
                elif y < column:
                    output_image[x][y] = offset_left + input_image[x][y]

        for x in range(myRow):
            for y in range(myColumn):
                if output_image[x][y] < 0:
                    output_image[x][y] = 0
                elif output_image[x][y] > 255:
                    output_image[x][y] = 255

        return output_image  # Currently the input image is returned, please replace this with the centralized image
