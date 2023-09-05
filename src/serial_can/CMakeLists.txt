cmake_minimum_required(VERSION 3.8)
project(serial_can)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread") 
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fstack-protector-all")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wstack-protector")


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(serial REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(moveit_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

include_directories(include) 

add_executable(serial_can src/serial_can.cpp)
# add_executable(SingleCaninterface src/SingleCaninterface.cpp)
# add_executable(actuator_control_interface src/actuator_control_interface.cpp)
ament_target_dependencies(serial_can rclcpp moveit_msgs std_msgs serial sensor_msgs)

target_include_directories(serial_can PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)


install(FILES
lib/libcontrolcan.so
lib/libmylibscan.so
DESTINATION lib
)

install(TARGETS
serial_can
DESTINATION lib/${PROJECT_NAME})


target_link_libraries(serial_can
${CMAKE_CURRENT_SOURCE_DIR}/lib/libcontrolcan.so
${CMAKE_CURRENT_SOURCE_DIR}/lib/libmylibscan.so
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)

  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()  

ament_package()







