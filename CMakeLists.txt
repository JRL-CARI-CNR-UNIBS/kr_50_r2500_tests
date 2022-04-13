cmake_minimum_required(VERSION 3.0.2)
project(kr_50_r2500_tests)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
  behaviortree_cpp_v3
  action_learning_tests
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
 LIBRARIES
 CATKIN_DEPENDS roscpp rospy std_msgs
 DEPENDS
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
#
# add_executable(        tree_test src/tree_test.cpp)
# add_dependencies(      tree_test ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# target_link_libraries( tree_test
#         ${catkin_LIBRARIES}
# )
