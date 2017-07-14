### C++ Basic

https://learnxinyminutes.com/docs/c++/



### Cmake

```
cmake -G "MinGW Makefiles"

mingw32-make

ctest

mingw32-make install
```



### [mingw dll](http://www.mingw.org/wiki/sampleDLL)

```
// Build dll
g++ -c -DBUILDING_EXAMPLE_DLL example_dll.cpp
g++ -shared -o example_dll.dll example_dll.o -Wl,--out-implib,libexample_dll.a

// Use dll
g++ -c example_exe.cpp
g++ -o example_exe.exe example_exe.o example_dll.dll

```



