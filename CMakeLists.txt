cmake_minimum_required(VERSION 3.0.2)
project(kr_50_r2500_tests)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
  behaviortree_cpp_v3
  skills_executer
  skills_executer_msgs
  manipulation_msgs
  actionlib_msgs
  actionlib
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  SetMongoByParam.srv
  SetParamByMongo.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
 INCLUDE_DIRS include
 LIBRARIES ${PROJECT_NAME}
 CATKIN_DEPENDS   roscpp
 rospy
 std_msgs
 behaviortree_cpp_v3
 skills_executer
 skills_executer_msgs
 manipulation_msgs
 actionlib_msgs
 actionlib
 DEPENDS
)

include_directories(
include
  ${catkin_INCLUDE_DIRS}
)

add_library(${PROJECT_NAME}
  src/kr_50_r2500_tests/bt_goto_class.cpp
)

add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})

install(TARGETS ${PROJECT_NAME}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
        FILES_MATCHING PATTERN "*.h"
        PATTERN ".svn" EXCLUDE
)

add_executable(        tree_test src/tree_test.cpp)
add_dependencies(      tree_test ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries( tree_test
        ${catkin_LIBRARIES}
        ${PROJECT_NAME}
)
