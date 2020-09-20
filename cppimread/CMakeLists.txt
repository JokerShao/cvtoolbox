cmake_minimum_required (VERSION 2.8)

project (cppimread)

# set (OpenCV_DIR /Users/zexi/codelib/opencv_ins/share/OpenCV)
set (OpenCV_DIR /Volumes/HGSTHDD/CodeLib/opencv_ins/share/OpenCV)
find_package( OpenCV REQUIRED
   )

add_executable(cppimread main.cpp)

target_link_libraries( cppimread ${OpenCV_LIBS} )

