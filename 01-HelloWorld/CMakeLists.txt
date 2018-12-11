SET(MYSRC "hello")
SET(PRJ "01-HelloWorld")
message(STATUS "MYSRC = ${MYSRC}")
add_library(${MYSRC} SHARED ${MYSRC}.cpp)
target_link_libraries(${MYSRC} CONAN_PKG::boost_python)

FILE(COPY ${MYSRC}.py DESTINATION .)
ADD_TEST(NAME ${PRJ}
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/lib
  COMMAND ${PYTHON3_EXECUTABLE} ../${PRJ}/${MYSRC}.py)
