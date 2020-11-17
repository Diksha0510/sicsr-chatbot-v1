# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.actions import FormPolicy
from rasa_sdk.events import SlotSet

class ActionAdminFeature(Action):

    def name(self) -> Text:
        return "action_admin_feature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # print("Course :", tracker.get_slot('course')
        program=""
        c=0
        course_type=tracker.get_slot("course")
        if(course_type == ""):
            c=1
        # program=tracker.get_slot("admissions")
        # if(program == ""):
        #     c=0
        feature=tracker.get_slot("admin_feature")
        flag=1
        if(course_type == "BCA" or program == "UG admissions"):
            url="https://www.sicsr.ac.in/ug-admissions/admissions"
        elif(course_type == "BBA-IT" or program == "UG admissions"):
            url="https://www.sicsr.ac.in/ug-admissions/admissions"
        elif(course_type == "MSC-CA" or program == "MSC admissions"):
            url="https://www.sicsr.ac.in/msc-admissions/"
        elif(course_type == "MSC-SS" or program == "MSC admissions"):
            url="https://www.sicsr.ac.in/msc-admissions/"
        elif(course_type == "MBA-IT" or program == "MSC admissions"):
            url="https://www.sicsr.ac.in/admissions/postgraduate/mba-it?_ga=2.179587366.300715909.1588679721-664504023.1588679721"
        else:
            dispatcher.utter_message("Invalid Input")
            flag=0
        if(flag!=0 and c==0):
            dispatcher.utter_message("Click on the url to get the {} of {}:\n{}".format(feature,course_type, url))
        elif(flag!=0 and c==1):
            dispatcher.utter_message("Click on the url to get the {} of {}:\n{}".format(feature,program, url))
        # dispatcher.utter_message("Hello {}".format(tracker.get_slot("course")))
        SlotSet("course", None)
        SlotSet("admin_feature", None)
        return []

class ActionCourseFeature(Action):

    def name(self) -> Text:
        return "action_course_feature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        flag=1
        course_type=tracker.get_slot("course")
        feature=tracker.get_slot("course_feature")
        if(course_type == "BCA"):
            url="https://www.sicsr.ac.in/programmes/bca?_ga=2.108676096.300715909.1588679721-664504023.1588679721"
        elif(course_type == "BBA-IT"):
            url="https://www.sicsr.ac.in/programmes/bba-it?_ga=2.179446822.300715909.1588679721-664504023.1588679721"
        elif(course_type == "MSC-CA"):
            url="https://www.sicsr.ac.in/programmes/msc-ca?_ga=2.213010454.300715909.1588679721-664504023.1588679721"
        elif(course_type == "MSC-SS"):
            url="https://www.sicsr.ac.in/programmes/msc-ss?_ga=2.184157348.300715909.1588679721-664504023.1588679721"
        elif(course_type == "MBA-IT"):
            url="https://www.sicsr.ac.in/programmes/mba-it?_ga=2.208407568.300715909.1588679721-664504023.1588679721"
        else:
            dispatcher.utter_message("Invalid Input")
            flag=0
        if(flag!=0):
            dispatcher.utter_message("Click on the url to get the {} of {}:\n{}".format(feature,course_type, url))
        SlotSet("course", None)
        SlotSet("course_feature", None)
        return []

# class ActionFormInfo(FormAction):
#     def name(self) -> Text:
#         return "course_form"
#
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["course"]
#
#     def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
#         return[]
