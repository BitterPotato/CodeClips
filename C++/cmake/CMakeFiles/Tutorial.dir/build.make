# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.9

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\ProgramComputer\cmake-3.9.0-rc6-win64-x64\bin\cmake.exe

# The command to remove a file.
RM = C:\ProgramComputer\cmake-3.9.0-rc6-win64-x64\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "E:\My Workspace\CodeClips\C++\cmake"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "E:\My Workspace\CodeClips\C++\cmake"

# Include any dependencies generated for this target.
include CMakeFiles/Tutorial.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Tutorial.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Tutorial.dir/flags.make

CMakeFiles/Tutorial.dir/tutorial.cpp.obj: CMakeFiles/Tutorial.dir/flags.make
CMakeFiles/Tutorial.dir/tutorial.cpp.obj: CMakeFiles/Tutorial.dir/includes_CXX.rsp
CMakeFiles/Tutorial.dir/tutorial.cpp.obj: tutorial.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="E:\My Workspace\CodeClips\C++\cmake\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Tutorial.dir/tutorial.cpp.obj"
	C:\ProgramComputer\TDM-GCC-64\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\Tutorial.dir\tutorial.cpp.obj -c "E:\My Workspace\CodeClips\C++\cmake\tutorial.cpp"

CMakeFiles/Tutorial.dir/tutorial.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Tutorial.dir/tutorial.cpp.i"
	C:\ProgramComputer\TDM-GCC-64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "E:\My Workspace\CodeClips\C++\cmake\tutorial.cpp" > CMakeFiles\Tutorial.dir\tutorial.cpp.i

CMakeFiles/Tutorial.dir/tutorial.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Tutorial.dir/tutorial.cpp.s"
	C:\ProgramComputer\TDM-GCC-64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "E:\My Workspace\CodeClips\C++\cmake\tutorial.cpp" -o CMakeFiles\Tutorial.dir\tutorial.cpp.s

CMakeFiles/Tutorial.dir/tutorial.cpp.obj.requires:

.PHONY : CMakeFiles/Tutorial.dir/tutorial.cpp.obj.requires

CMakeFiles/Tutorial.dir/tutorial.cpp.obj.provides: CMakeFiles/Tutorial.dir/tutorial.cpp.obj.requires
	$(MAKE) -f CMakeFiles\Tutorial.dir\build.make CMakeFiles/Tutorial.dir/tutorial.cpp.obj.provides.build
.PHONY : CMakeFiles/Tutorial.dir/tutorial.cpp.obj.provides

CMakeFiles/Tutorial.dir/tutorial.cpp.obj.provides.build: CMakeFiles/Tutorial.dir/tutorial.cpp.obj


# Object files for target Tutorial
Tutorial_OBJECTS = \
"CMakeFiles/Tutorial.dir/tutorial.cpp.obj"

# External object files for target Tutorial
Tutorial_EXTERNAL_OBJECTS =

Tutorial.exe: CMakeFiles/Tutorial.dir/tutorial.cpp.obj
Tutorial.exe: CMakeFiles/Tutorial.dir/build.make
Tutorial.exe: MathFunctions/libMathFunctions.a
Tutorial.exe: CMakeFiles/Tutorial.dir/linklibs.rsp
Tutorial.exe: CMakeFiles/Tutorial.dir/objects1.rsp
Tutorial.exe: CMakeFiles/Tutorial.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="E:\My Workspace\CodeClips\C++\cmake\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Tutorial.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Tutorial.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Tutorial.dir/build: Tutorial.exe

.PHONY : CMakeFiles/Tutorial.dir/build

CMakeFiles/Tutorial.dir/requires: CMakeFiles/Tutorial.dir/tutorial.cpp.obj.requires

.PHONY : CMakeFiles/Tutorial.dir/requires

CMakeFiles/Tutorial.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Tutorial.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Tutorial.dir/clean

CMakeFiles/Tutorial.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "E:\My Workspace\CodeClips\C++\cmake" "E:\My Workspace\CodeClips\C++\cmake" "E:\My Workspace\CodeClips\C++\cmake" "E:\My Workspace\CodeClips\C++\cmake" "E:\My Workspace\CodeClips\C++\cmake\CMakeFiles\Tutorial.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Tutorial.dir/depend

