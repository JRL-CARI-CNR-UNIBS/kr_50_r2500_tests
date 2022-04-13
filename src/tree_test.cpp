#include <behaviortree_cpp_v3/bt_factory.h>
#include <action_learning_tests/skills_classes.h>

int main()
{
    BT::BehaviorTreeFactory factory;

    factory.registerNodeType<SkillActionNode>("SkillActionNode");

    auto tree = factory.createTreeFromFile("~/projects/planning_ws/src/kr_50_r2500/kr_50_r2500_tests/trees/test_tree.xml");

    tree.tickRoot();
}
