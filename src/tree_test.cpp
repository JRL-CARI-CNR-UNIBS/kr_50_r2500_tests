#include <ros/ros.h>
#include <behaviortree_cpp_v3/bt_factory.h>
#include <skills_executer/bt_skills_classes.h>
#include <kr_50_r2500_tests/bt_goto_class.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "tree_test");
    ros::NodeHandle nh("tree_test_server");

    ROS_INFO("Tree test start");

    BT::BehaviorTreeFactory factory;

    ROS_INFO("Factory created");

    factory.registerNodeType<SkillActionNode>("SkillActionNode");
    ROS_INFO("SkillActionNode registered");

    factory.registerNodeType<GoToActionNode>("GoToActionNode");
    ROS_INFO("GoToActionNode registered");

    ROS_INFO("Pre action tree");

    BT::Tree action_tree = factory.createTreeFromFile("/home/gauss/projects/planning_ws/src/kr_50_r2500_tests/config/trees/action1_tree.xml");

    ROS_INFO("Post action tree");

    ROS_INFO("Pre tree");

    BT::Tree tree = factory.createTreeFromFile("/home/gauss/projects/planning_ws/src/kr_50_r2500_tests/config/trees/main_tree.xml");

    ROS_INFO("Post tree");

//    BT::Tree tree = factory.createTreeFromFile("/home/gauss/projects/planning_ws/src/kr_50_r2500_tests/config/trees/test_tree.xml");

    ROS_INFO("Tree created");

    tree.tickRoot();

    ROS_INFO("Tree test finish");
}
