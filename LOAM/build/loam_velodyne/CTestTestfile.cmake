# CMake generated Testfile for 
# Source directory: /home/ethan/Coding/loam_HSU/LOAM/src/loam_velodyne
# Build directory: /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_loam_velodyne_rostest_test_loam.test "/home/ethan/Coding/loam_HSU/LOAM/build/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/ethan/Coding/loam_HSU/LOAM/build/test_results/loam_velodyne/rostest-test_loam.xml" "--return-code" "/usr/bin/python3 /opt/ros/noetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ethan/Coding/loam_HSU/LOAM/src/loam_velodyne --package=loam_velodyne --results-filename test_loam.xml --results-base-dir \"/home/ethan/Coding/loam_HSU/LOAM/build/test_results\" /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne/test/loam.test ")
set_tests_properties(_ctest_loam_velodyne_rostest_test_loam.test PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/rostest/cmake/rostest-extras.cmake;52;catkin_run_tests_target;/home/ethan/Coding/loam_HSU/LOAM/src/loam_velodyne/CMakeLists.txt;64;add_rostest;/home/ethan/Coding/loam_HSU/LOAM/src/loam_velodyne/CMakeLists.txt;0;")
subdirs("src/lib")
