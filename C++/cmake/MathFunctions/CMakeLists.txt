# 1. build the MarkTable executable
add_executable(MakeTable MakeTable.cpp)

# 2. run MakeTable to product Table.h
add_custom_command (
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  DEPENDS MakeTable
)

include_directories( ${CMAKE_CURRENT_BINARY_DIR})
# 3. compile mysqrt which includes Table.h
add_library(MathFunctions mysqrt.cpp ${CMAKE_CURRENT_BINARY_DIR}/Table.h)

# determine where the files will be installed
install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)

