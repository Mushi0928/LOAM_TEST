# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ethan/Coding/loam_HSU/LOAM/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ethan/Coding/loam_HSU/LOAM/build

# Utility rule file for clean_test_results_loam_velodyne.

# Include the progress variables for this target.
include loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/progress.make

loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne:
	cd /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne && /usr/bin/python3 /opt/ros/noetic/share/catkin/cmake/test/remove_test_results.py /home/ethan/Coding/loam_HSU/LOAM/build/test_results/loam_velodyne

clean_test_results_loam_velodyne: loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne
clean_test_results_loam_velodyne: loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/build.make

.PHONY : clean_test_results_loam_velodyne

# Rule to build all files generated by this target.
loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/build: clean_test_results_loam_velodyne

.PHONY : loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/build

loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/clean:
	cd /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_loam_velodyne.dir/cmake_clean.cmake
.PHONY : loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/clean

loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/depend:
	cd /home/ethan/Coding/loam_HSU/LOAM/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ethan/Coding/loam_HSU/LOAM/src /home/ethan/Coding/loam_HSU/LOAM/src/loam_velodyne /home/ethan/Coding/loam_HSU/LOAM/build /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne /home/ethan/Coding/loam_HSU/LOAM/build/loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : loam_velodyne/CMakeFiles/clean_test_results_loam_velodyne.dir/depend

