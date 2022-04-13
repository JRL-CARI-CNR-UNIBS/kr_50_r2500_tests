#!/usr/bin/env python3

import pymongo
import pprint
import rospy

from std_msgs.msg import String
from pymongo import MongoClient
from kr_50_r2500_tests.srv import SetParamByMongo
from kr_50_r2500_tests.srv import SetMongoByParam

def callback(data):
    return data.data

def set_mongo_by_param(srv):

    exec_params = rospy.get_param("/exec_params")
    if exec_params:
        exec_params_mongo = []
        for key_1 in exec_params.keys():
                for key_2 in exec_params[key_1].keys():
                        data = exec_params[key_1][key_2]
                        data["action_name"] = key_1
                        data["skill_name"]  = key_2
                        exec_params_mongo.append(data)

    exec_collection.delete_many({})
    exec_collection.insert_many(exec_params_mongo)

    policy_params = rospy.get_param("/policy_params")
    if policy_params:
        policy_params_mongo = []
        for key_1 in policy_params.keys():
            data = policy_params[key_1]
            data["action_name"] = key_1
            policy_params_mongo.append(data)

    policy_collection.delete_many({})
    policy_collection.insert_many(policy_params_mongo)

    arbitrator_params = rospy.get_param("/arbitrator_params")
    if arbitrator_params:
        arbitrator_params_mongo = []
        for key_1 in arbitrator_params.keys():
                for key_2 in arbitrator_params[key_1].keys():
                        data = arbitrator_params[key_1][key_2]
                        data["action_name"] = key_1
                        data["skill_name"]  = key_2
                        arbitrator_params_mongo.append(data)

    arbitrator_collection.delete_many({})
    arbitrator_collection.insert_many(arbitrator_params_mongo)

    learning_params = rospy.get_param("/learning_params")
    if learning_params:
        learning_params_mongo = []
        for key_1 in learning_params.keys():
                for key_2 in learning_params[key_1].keys():
                        data = learning_params[key_1][key_2]
                        data["action_name"] = key_1
                        data["skill_name"]  = key_2
                        learning_params_mongo.append(data)

    learning_collection.delete_many({})
    learning_collection.insert_many(learning_params_mongo)

    print('set_mongo_by_param finisced')
    return 'true'

def set_param_by_mongo(srv):
    exec_params       = list(exec_collection.find())
    policy_params     = list(policy_collection.find())
    arbitrator_params = list(arbitrator_collection.find())
    learning_params   = list(learning_collection.find())

    for exec_param in exec_params:
        str = "/"
        exec_str = "exec_params"
        action_name = exec_param["action_name"]
        skill_name  = exec_param["skill_name"]
        del exec_param["_id"]
        del exec_param["action_name"]
        del exec_param["skill_name"]
        for key in exec_param.keys():
            param_str = str+exec_str+str+action_name+str+skill_name+str+key
            rospy.set_param(param_str, exec_param[key])
        print('exec_parmas setted')

    for arbitrator_param in arbitrator_params:
        str = "/"
        arbitrator_str = "arbitrator_params"
        action_name = arbitrator_param["action_name"]
        skill_name  = arbitrator_param["skill_name"]
        del arbitrator_param["_id"]
        del arbitrator_param["action_name"]
        del arbitrator_param["skill_name"]
        for key in arbitrator_param.keys():
            param_str = str+arbitrator_str+str+action_name+str+skill_name+str+key
            rospy.set_param(param_str, arbitrator_param[key])
        print('arbitrator_params setted')

    for learning_param in learning_params:
        str = "/"
        learning_str = "learning_params"
        action_name = learning_param["action_name"]
        skill_name  = learning_param["skill_name"]
        del learning_param["_id"]
        del learning_param["action_name"]
        del learning_param["skill_name"]
        for key in learning_param.keys():
            param_str = str+learning_str+str+action_name+str+skill_name+str+key
            rospy.set_param(param_str, learning_param[key])
        print('learning_params setted')

    for policy_param in policy_params:
        str = "/"
        policy_str = "policy_params"
        action_name = policy_param["action_name"]
        del policy_param["_id"]
        del policy_param["action_name"]
        for key in policy_param.keys():
            param_str = str+policy_str+str+action_name+str+key
            rospy.set_param(param_str, policy_param[key])
        print('policy_params setted')

    return 'true'


def clear_param(srv):
    exec_collection.delete_many({})
    policy_collection.delete_many({})
    arbitrator_collection.delete_many({})
    learning_collection.delete_many({})
    print('Params cleared!')
    return 'true'

def server_launch():
    s = rospy.Service('/set_mongo_by_param', SetMongoByParam, set_mongo_by_param)
    s = rospy.Service('/set_param_by_mongo', SetParamByMongo, set_param_by_mongo)
    s = rospy.Service('clear_param_on_mongo', SetMongoByParam, clear_param)
    print("Ready to set.")
    rospy.spin()


client = MongoClient('localhost', 27017)

db_param = rospy.get_param("/collection_name")
db = client[db_param]

exec_collection       = db.exec_param
policy_collection     = db.policy_param
arbitrator_collection = db.arbitrator_param
learning_collection   = db.learning_param

if __name__ == '__main__':
    rospy.init_node('prova', anonymous=True)
    server_launch()
