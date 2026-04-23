cmake_minimum_required(VERSION 3.8)

set(CMAKE_SUPPRESS_DEVELOPER_WARNINGS 1 CACHE INTERNAL "Suppress CMake developer warnings")

project(jimmbot_description)

set(CMAKE_POLICY_DEFAULT_CMP0009 NEW)

if(POLICY CMP0009)
  cmake_policy(SET CMP0009 NEW)
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
  PATTERN build EXCLUDE
  PATTERN install EXCLUDE
  PATTERN log EXCLUDE
)

ament_package()
