#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"


int main(int argc, char** argv)
{
    cv::Mat img = cv::imread("/Volumes/HGSTHDD/EXT4_CODE/cvtoolbox/im.jpg");

    cv::Mat img_small;

    cv::resize(img, img_small, cv::Size(200, 300));


    cv::imshow("img_small", img_small);
    cv::waitKey(0);
    
    return 0;
}

